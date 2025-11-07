from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    btc_balance = models.DecimalField(default=0.00, max_digits=20, decimal_places=8)
    eth_balance = models.DecimalField(default=0.00, max_digits=20, decimal_places=8)
    usdt_balance = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    total_balance = models.DecimalField(default=0.00, max_digits=20, decimal_places=3)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

    def save(self, *args, **kwargs):
        # Calculate total balance before saving
        self.total_balance = self.btc_balance + self.eth_balance + self.usdt_balance
        super().save(*args, **kwargs)