from django.db import models

class Category(models.Model):
    identifier = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)  
    api_name = models.CharField(max_length=255)  
    url = models.URLField(max_length=200)
    description = models.TextField()
    marketplace = models.CharField(max_length=255)  
    type = models.CharField(max_length=255)  

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name

class CategoryInProduct(models.Model):
    product = models.CharField(max_length=255)  
    category = models.CharField(max_length=255)  
    marketplace = models.CharField(max_length=255)  

    class Meta:
        db_table = 'CategoryInProduct'

    def __str__(self):
        return f'Product: {self.product}, Category: {self.category}'

class Marketplace(models.Model):
    name = models.CharField(max_length=255, primary_key=True)  

    class Meta:
        db_table = 'Marketplace'

    def __str__(self):
        return self.name

class Market(models.Model):
    identifier = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=255)  
    marketplace = models.CharField(max_length=255)  

    class Meta:
        db_table = 'Market'

    def __str__(self):
        return self.name

class CategoryInMarket(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    marketplace = models.CharField(max_length=255)  

    class Meta:
        db_table = 'CategoryInMarket'

    def __str__(self):
        return f'Category: {self.category.name}, Market: {self.market.name}'

class Keyword(models.Model):
    identifier = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)  
    marketplace = models.CharField(max_length=255)  

    class Meta:
        db_table = 'Keywords'

    def __str__(self):
        return self.name

class Product(models.Model):
    identifier = models.CharField(primary_key=True, max_length=150)
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=255)  
    description = models.TextField()
    type = models.CharField(max_length=255)  
    creator = models.CharField(max_length=255)  
    marketplace = models.CharField(max_length=255)  

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name

class ProductKeyword(models.Model):
    product = models.CharField(max_length=255)  
    keywords = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=255)  
    description = models.TextField()

    class Meta:
        db_table = 'ProductKeyword'

    def __str__(self):
        return f'Product: {self.product}, Keywords: {self.keywords}'

class Test(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
