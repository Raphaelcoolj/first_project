from django.contrib import admin
from django.contrib.auth.models import User
from .models import Wallet

# Optional: extend User admin to show related wallet
class WalletInline(admin.StackedInline):
    model = Wallet
    can_delete = False
    verbose_name_plural = 'Wallet'

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (WalletInline,)
    list_display = ('username', 'email', 'is_staff', 'is_active')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Wallet)
