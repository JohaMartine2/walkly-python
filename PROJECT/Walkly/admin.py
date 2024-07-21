from django.contrib import admin

# Register your models here.
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "profession_name")

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("plan_name", "price")

admin.site.register(Features)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Contact_Us)