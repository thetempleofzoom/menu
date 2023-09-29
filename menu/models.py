from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('soup', 'Soup'),
    ('entrees', 'Entrees'),
    ('dessert', 'Dessert'),
    ('beverages', 'Beverages')
)

STATUS = (
    (0, 'Not Avail'),
    (1, 'Available')
)

class Items(models.Model):
    dish = models.CharField(max_length=300, unique=True)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    meal_category = models.CharField(max_length=30, choices=MEAL_TYPE) #for dropdown
    # on_delete determines what happens when user is deleted. 
    # cascade = all items deleted / protect = all items remain / set_null = no author 
    chef = models.ForeignKey(User, on_delete=models.PROTECT) # User also has a database
    status = models.IntegerField(choices=STATUS, default=1)
    # auto now add created only once
    date_created = models.DateField(auto_now_add=True)
    # auto now can be created multiple times
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.meal
    