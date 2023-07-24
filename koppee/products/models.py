from django.db import models
from category.models import category

# Create your models here.
class products(models.Model):
    prod_name = models.CharField( max_length=50)
    prod_descr = models.TextField()
    prod_categ = models.ForeignKey(category, on_delete=models.CASCADE)
    prod_price = models.IntegerField()
    prod_img = models.ImageField(upload_to='pic')
    def __str__(self):
        return self.prod_name
    
class booking(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_mail = models.CharField(max_length=50)
    cust_date = models.DateField()
    cust_time = models.TimeField(auto_now=False)
    cust_pers = models.IntegerField()
    def __str__(self):
        return self.cust_name


    