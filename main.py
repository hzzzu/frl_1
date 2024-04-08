import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6730354356:AAFDjPDiSwGRZ-eU8qGirwD7E5-cstby3uo'
TEXT_RESPONSE = 'Ого, ты помнишь обо мне и прислал {}!'


offset = -2
counter = 0
chat_id = None

while counter < 100:
    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            message = result['message']
            if 'text' in message:
                text = message['text']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("текст")}')
            elif 'sticker' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("стикер")}')
            elif 'photo' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("фото")}')
            elif 'voice' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("голосовое сообщение")}')
            elif 'video' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("видео")}')
            elif 'document' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("документ")}')
            elif 'video_note' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("видео сообщение")}')
            elif 'animation' in message:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_RESPONSE.format("гифку")}')

    time.sleep(1)
    counter += 1