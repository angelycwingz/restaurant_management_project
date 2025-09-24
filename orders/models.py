from django.db import models

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Order Statuses"

    def __str__(self):
        self.name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Link to OrderStatus
    status = models.ForiegnKey(
        OrderStatus, 
        on_delete=models.SET_NULL, # set to Null if order status is deleted
        null=True,
        related_name="orders" # for reverse lookup
    )

    def __str__(self):
        return f"Order #{self.id} - {self.product_name} ({self.status})"