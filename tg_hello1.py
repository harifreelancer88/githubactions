import requests

def send_to_telegram(message):
    telegram_api_token = '5602544099:AAF510C1bsLqhNq0_ZCkA-iqS_Ggr5lgaCI'
    telegram_chat_id = '928242547'
    apiURL = f'https://api.telegram.org/bot{telegram_api_token}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': telegram_chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

try:
    send_to_telegram(f"Hello World!!!")
except Exception as e:
    print(e)