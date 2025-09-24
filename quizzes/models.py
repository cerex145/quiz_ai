from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "quizzes"  # 📝 Proper plural form
        ordering = ['-created_at']       # 📅 Newest first
    
    def __str__(self):
        return self.title