from django.contrib import admin
from django.contrib.auth.models import User
from .models import Wallet

# Inline Wallet for User
class WalletInline(admin.StackedInline):
    model = Wallet
    can_delete = False
    verbose_name_plural = 'Wallet'
    readonly_fields = ('total_balance',)  # make total_balance read-only

# Extend User admin
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (WalletInline,)
    list_display = ('username', 'email', 'is_staff', 'is_active')

# Unregister default User and register new
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
