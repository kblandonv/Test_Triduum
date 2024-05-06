from django.db import models
from django.db import connection

# Create your models here.

class Product(models.Model):
    """
    Represents a product in the e-commerce system.

    Attributes:
        id (int): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        stock (int): The available stock quantity of the product.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order in the e-commerce system.

    Attributes:
        id (AutoField): The primary key for the order.
        date (DateField): The date when the order was placed.
        client (CharField): The name of the client who placed the order.
    """

    id = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model):
    """
    Represents the details of an order.

    Attributes:
        id (AutoField): The primary key for the order detail.
        order_id (ForeignKey): The foreign key to the Order model, representing the order to which this detail belongs.
        quantity (IntegerField): The quantity of the product in the order.
        product_id (ForeignKey): The foreign key to the Product model, representing the product in the order.

    Meta:
        unique_together (tuple): Specifies that the combination of order_id and product_id should be unique.
        ordering (list): Specifies the default ordering of OrderDetail instances based on their id.

    Methods:
        __str__(): Returns a string representation of the OrderDetail instance.

    """

    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order_id', 'product_id')
        ordering = ['id']

    def __str__(self):
        return str(self.order_id, self.product_id)
    
