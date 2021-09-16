from django.contrib import admin
from .models import Trade

class TradeAdmin(admin.ModelAdmin):
	list_display = ('id' ,'trading_ammount' , 'profit' , 'is_published' , 'intrestrate' , 'list_date')
	list_display_links = ('id' , 'intrestrate')
	list_filter = ('trading_ammount' , 'profit' , 'intrestrate')
	list_editable = ('is_published',)
	search_fields = ('trading_ammount' , 'profit' , 'is_published' , 'intrestrate')
	list_per_page = 35


# Register your models here.
admin.site.register(Trade , TradeAdmin)
