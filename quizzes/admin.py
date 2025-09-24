from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']     # 📋 Show these columns
    search_fields = ['title', 'description']   # 🔍 Enable search
    list_filter = ['created_at']               # 🗂️ Filter sidebar