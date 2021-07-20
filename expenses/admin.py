from django.contrib import admin
from .models import Expense

admin.site.register(Expense)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

# Register your models here.
