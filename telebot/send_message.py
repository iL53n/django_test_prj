import requests
from .models import TeleSettings


def sendTelegram(order):
    settings = TeleSettings.objects.get(pk=1)

    method = '/sendMessage'
    api = 'https://api.telegram.org/bot'
    url = f'{api}{settings.tg_token}{method}'
    text = settings.tg_message\
        .replace('{ name }', order.order_name)\
        .replace('{ phone }', order.order_phone)

    payload = {
        'chat_id': settings.tg_chat_id,
        'text': text,
    }

    requests.post(url, data=payload)
