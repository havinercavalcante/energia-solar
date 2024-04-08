from django.contrib import admin
from .models import Consumer, DiscountRule

# Register your models here.

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'city', 'state', 'consumption', 'distributor_tax', 'discount_rule')
    search_fields = ('name', 'document')
    list_filter = ('city', 'state', 'discount_rule__consumer_type')

class DiscountRuleAdmin(admin.ModelAdmin):
    list_display = ('consumption_range', 'consumer_type', 'cover_value', 'discount_value')
    list_filter = ('consumer_type',)

admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(DiscountRule, DiscountRuleAdmin)