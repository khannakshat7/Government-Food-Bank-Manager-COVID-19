from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Block(models.Model):
    blockname = models.CharField(max_length=128)

    def __str__(self):
        return self.blockname

class GramPanchayat(models.Model):
    gramname = models.CharField(max_length=128)
    blockna = models.ForeignKey(Block, on_delete=models.CASCADE,null = True)
    # members = models.ManyToManyField(Block, through='FoodBankBeneficiary')

    def __str__(self):
        return self.gramname

class FoodBankBeneficiary(models.Model):
    block = models.CharField(max_length=50)
    gram = models.CharField(max_length=50)

    date_added = models.DateField(auto_now=True)
    head_of_family = models.CharField(max_length=50)
    total_members_in_family = models.PositiveIntegerField()
    mobile = models.CharField(max_length=50)
    NFSA = models.BooleanField()
    food_packet_Count = models.PositiveIntegerField()
    wheat_kg = models.PositiveIntegerField()
    rice_kg = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date_added)

    
class FoodBankInventryDry(models.Model):
    block = models.CharField(max_length=50)
    gram = models.CharField(max_length=50)

    date_added = models.DateField(auto_now=True)
    Available = models.PositiveIntegerField()
    Recieved_Bhamashah = models.PositiveIntegerField()
    Recieved_Government = models.PositiveIntegerField()
    Recieved_NGO = models.PositiveIntegerField()
    Distributed = models.PositiveIntegerField()
    Required = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date_added)

class FoodBankInventrymid(models.Model):
    block = models.CharField(max_length=50)
    gram = models.CharField(max_length=50)

    date_added = models.DateField(auto_now=True)
    Available_Wheat_Kgs = models.PositiveIntegerField()
    Recieved_Wheat_Kgs = models.PositiveIntegerField()
    Distributed_Wheat_Kgs = models.PositiveIntegerField()
    Required_Wheat_Kgs = models.PositiveIntegerField()
    Available_Rice_Kgs = models.PositiveIntegerField()
    Recieved_Rice_Kgs = models.PositiveIntegerField()
    Distributed_Rice_Kgs = models.PositiveIntegerField()
    Required_Rice_Kgs = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date_added)

class FoodBankInventrycook(models.Model):
    block = models.CharField(max_length=50)
    gram = models.CharField(max_length=50)

    date_added = models.DateField(auto_now=True)
    Received_Cooked_Meal_Government = models.PositiveIntegerField()
    Received_Cooked_Meal_Bhamashah = models.PositiveIntegerField()
    Recieved_Cooked_Meal_NGO = models.PositiveIntegerField()
    Distributed_Overall_Cooked_Meal = models.PositiveIntegerField()

    def __str__(self):
        return str(self.date_added)