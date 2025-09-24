from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    """🔄 Converts Quiz model to/from JSON"""
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # 🔒 Auto-generated fields