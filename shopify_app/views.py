from django.shortcuts import render, render_to_response, HttpResponseRedirect
from shopify_app.models import *
import shopify,dateutil.parser

# Create your views here.
def login(request):
	if request.method == "GET":
		if not request.session.get('shop'):
			return render(request,"shopify_app/login.html")
		else:
			return HttpResponseRedirect('/home')
	else:
		shop_name = request.REQUEST.get('shop')
		return redirect_and_authenticate(shop_name)

def home(request):
	store = find_store(request)	
	if store:
			products = store.products.all()
			return render_to_response("shopify_app/home.html",{'products':products})
	else:
		return return_to_root

def search(request):
	if request.method == "GET":
		store = find_store(request)
		if store:
			products = store.products.filter(name__icontains = request.REQUEST.get('product'))
			return render_to_response("shopify_app/home.html",{'products':products})


def find_store(request):
	shop_session = request.session.get('shop')
	if shop_session:
		store = Store.objects.get(name = shop_session)
		return store
	else:
		return None

def logout(request):
	request.session.flush()
	return return_to_root(request)


def return_to_root(request):
	return HttpResponseRedirect('/')

def save_store_details(request):
	shop = request.REQUEST.get('shop')
	session = shopify.Session(shop)
	token = session.request_token(request.REQUEST)
	try:
		store = Store.objects.get(name = shop)
		store.access_token = token
		store.save()
	except Store.DoesNotExist:
		store = Store.objects.create(name = shop, access_token = token)

	#save orders,products and customers
	save_details(store)
	request.session['shop'] = shop
	return HttpResponseRedirect('/home')

def reload(request):
	shop = request.session.get('shop')
	try:
		store = Store.objects.get(name = shop)
	except Store.DoesNotExist:
		return HttpResponseRedirect('/')
	save_details(store)
	return HttpResponseRedirect('/home')

def save_details(store):
	session = shopify.Session(store.name, store.access_token)
	shopify.ShopifyResource.activate_session(session)
	save_customers(shopify.Customer.find(),store.id)
	save_products(shopify.Product.find(),store.id)
	save_orders(shopify.Order.find(),store.id)


def save_customers(customers,store_id):
	for customer in customers:
		try:
			Customer.objects.get(id = customer.id)
		except:
			Customer.objects.create(id = customer.id,name = customer.first_name, phone_number = customer.default_address.phone,store_id = store_id)

def save_products(products,store_id):
	for product in products:
		try:
			Product.objects.get(id = product.id)
		except:
			Product.objects.create(id = product.id, name = product.title, store_id = store_id)

def save_orders(orders,store_id):
	for order in orders:
		try:
			Order.objects.get(id = order.id)
		except:
			Order.objects.create(id = order.id, customer_id = order.customer.id, store_id = store_id, date = dateutil.parser.parse(order.created_at))
			for detail in order.line_items:
				Order_Product.objects.create(order_id = order.id, product_id = detail.product_id )

def redirect_and_authenticate(shop_name):
	redirect_url = build_redirect_url(shop_name)
	return HttpResponseRedirect(redirect_url)

def build_redirect_url(shop_name):
	app_credentials = App.objects.get(id = 1)
	shopify.Session.setup(api_key=app_credentials.api_key, secret=app_credentials.shared_secret)
	permission_url = shopify.Session(shop_name).create_permission_url([app_credentials.permissions])
	return permission_url + "&redirect_uri=" + app_credentials.redirect_url
