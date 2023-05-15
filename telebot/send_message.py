import requests
from .models import TeleSettings


def sendTelegram(order):
    settings = TeleSettings.objects.get(pk=1)

    if settings:
        method = '/sendMessage'
        api = 'https://api.telegram.org/bot'
        url = f'{api}{settings.tg_token}{method}'

        if settings.tg_message.find('{ name }') and settings.tg_message.find('{ phone }'):
            text = settings.tg_message\
                .replace('{ name }', order.order_name)\
                .replace('{ phone }', order.order_phone)
        else:
            text = settings.tg_message

        payload = {
            'chat_id': settings.tg_chat_id,
            'text': text,
        }

        try:
            req = requests.post(url, data=payload)
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Sending error!')
            elif req.status_code == 500:
                print('Server error!')
            else:
                print('OK. The message was sent!')

    else:
        pass
