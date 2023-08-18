from django.db import models
from django.contrib import admin


class Advertisement(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @admin.display
    def created_day(self):
        from django.utils import timezone    
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return f"Сегодня в {created_time}"
        return self.created_at

class Meta:
    db_table = "advertisements"
    verbose_name = "объявление"
    verbose_name_plural = "объявления"