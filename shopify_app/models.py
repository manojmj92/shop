from django.db import models
from datetime import datetime
import dateutil.relativedelta

# Create your models here.
class App(models.Model):
	id = models.AutoField(primary_key=True)
	api_key = models.CharField(max_length = 50)
	shared_secret = models.CharField(max_length = 50)
	permissions = models.CharField(max_length=100)
	redirect_url = models.CharField(max_length=50)

class Store(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	access_token = models.CharField(max_length=50)


class OrderManager(models.Manager):
	def in_last_12_months(self):
		one_year_ago = datetime.now() - dateutil.relativedelta.relativedelta(months=12)
		return self.filter(date__gte = one_year_ago)

class Order(models.Model):
	id = models.IntegerField(primary_key=True)
	store = models.ForeignKey('Store', related_name='order')
	customer = models.ForeignKey('Customer', related_name='order')
	date = models.DateTimeField(default=datetime.now, blank=True)
	products = models.ManyToManyField('Product', through='Order_Product')
	objects = OrderManager()
	

class Product(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	store = models.ForeignKey('Store', related_name='products')
	orders = models.ManyToManyField('Order', through='Order_Product')

class Customer(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	phone_number = models.CharField(null = True,max_length=30)
	store = models.ForeignKey('Store', related_name='customer')

class Order_Product(models.Model):
	id = models.AutoField(primary_key=True)
	order = models.ForeignKey('Order',related_name ="orders")
	product = models.ForeignKey('Product',related_name="products")