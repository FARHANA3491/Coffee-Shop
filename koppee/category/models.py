from django.db import models

# Create your models here. #farhana 111 ifarhana3491@gmail.com
coffee_types = (
    ('hot','HOT'),
    ('cold','COLD'),
)

class category(models.Model):
    categ_name =  models.CharField(max_length=255)
    categ_type =  models.CharField(max_length=10, choices= coffee_types, default = 'hot')
    def __str__(self):
        return self.categ_name
     