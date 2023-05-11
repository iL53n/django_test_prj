from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Token')
    tg_chat_id = models.CharField(max_length=200, verbose_name='Chat ID')
    tg_message = models.TextField(verbose_name='Text message')

    def __str__(self):
        return self.tg_message

    class Meta:
        verbose_name = 'Telegram message'
        verbose_name_plural = 'Telegram messages'
