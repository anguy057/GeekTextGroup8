from django.contrib import admin
from users.models import Account
from users.models import CreditCard
# Register your models here.


admin.site.register(Account)
admin.site.register(CreditCard)