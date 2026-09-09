from django.contrib import admin
from .models import TelegramUser, LearningCategory, LearningMaterial

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'first_name', 'username', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('telegram_id', 'username', 'first_name')

@admin.register(LearningCategory)
class LearningCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)

@admin.register(LearningMaterial)
class LearningMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
