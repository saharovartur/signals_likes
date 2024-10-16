from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from images.models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def user_like_changed(sender, instance, **kwargs):
    """Обрабатывает изменения в отношении "users_like" для изображения,
    обновляя счетчик лайков"""
    instance.total_likes = instance.users_like.count()
    instance.save()
