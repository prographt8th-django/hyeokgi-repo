from django.db import models

from user.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Diary(BaseModel):
    # (db 저장 값, 표시 값(admin, form))
    # diary.emotion = [0], diary.get_emotion_display = [1]
    EMOTION_CHOICES = (
        ('HP', 'Happy'),
        ('SD', 'Sad'),
        ('AG', 'Angry'),
        ('SS', 'SoSo')
    )

    emotion = models.CharField(max_length=2, choices=EMOTION_CHOICES)
    context = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']