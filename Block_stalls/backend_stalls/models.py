from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# 1️⃣ Block Model
class Block(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# 2️⃣ Stall Model
class Stall(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="stalls")
    name = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    is_open = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.block.name})"


# 3️⃣ Menu Item Model
class MenuItem(models.Model):
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE, related_name="menu_items")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_veg = models.BooleanField(default=True)
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# 4️⃣ Time Slot Model
class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_orders = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


# 5️⃣ Order Model
class Order(models.Model):
    STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Rejected", "Rejected"),
    ("Completed", "Completed"),
)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.SET_NULL, null=True)
    stall = models.ForeignKey(Stall, on_delete=models.SET_NULL, null=True)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# 6️⃣ Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"