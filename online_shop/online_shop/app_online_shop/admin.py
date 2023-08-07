from django.contrib import admin
from.models import advertisements
# Register your models here.

# Создаем модель панели регестрирования 
class advertisements_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'auction','update_time']
    list_filter = ['auction', 'created_time', 'update_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('общее', {
            'fields': ('title', 'description')
        }), 

        ('Финансы', {
                'fields': ('price', 'auction'),
                'classes': (['collapse'])
            })
    )

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
# отображаем модель панели администрирования

admin.site.register(advertisements, advertisements_admin)

