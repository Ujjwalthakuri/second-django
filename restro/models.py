from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    # def __str__(self,):
    #     return self.name

class Food(models.Model):
    name = models.CharField(max_length=50)
    describe = models.TextField()
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self,):
        return self.name
    
class Table(models.Model):
    number = models.IntegerField()
    is_available = models.BooleanField(default=False)
    
class Order(models.Model):
    pending ="p"
    complete="c"
    inprocess="ip"
    status_choice={
        pending: "pending",
        complete:"complete",
        inprocess:"inprocess",
    }
    pending ="p"
    complete="c"
    payment_choice={
        pending: "pending",
        complete:"complete",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=2, choices=status_choice, default= pending ) 
    payment_status = models.CharField(max_length=2, choices=payment_choice, default=pending)
    total_price = models.FloatField()

class order_item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    

