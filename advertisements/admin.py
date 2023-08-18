from django.contrib import admin
from .models import Advertisement

class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "auction", "price", "created_at", "created_day"]
    list_filter = ["auction", "created_at"]
    search_fields = ["title"]
    actions = ["mark_auction_as_true", "mark_auction_as_false"]
    fieldsets = (
        ('Общая информация' , {
            "fields":("title", "description"),
            "classes":["collapse"]
        }),
        ("Финансы", {
            "fields": ("price", "auction"),
            "classes":["collapse"]
        })
    )

    @admin.action(description="Добавить возможность")
    def mark_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description="убрать возможность")
    def mark_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Advertisement, AdvertismentAdmin)