import json

import aiohttp

from calculates import authKEY, message



async def list_of_arriving_buses_post():
    print('Зашел')
    url = "https://tosamara.ru/api/v2/json"

    json_data = {
        'clientId': "SmrSmartCity",
        'os': 'android',
        'authKey': authKEY,
        'message': message
    }
    print('создал переменные')
    async with aiohttp.ClientSession() as session:
        print('сессия')
        async with session.post(url, data=json_data) as response:
            print('ответ', response.status)
            text = await response.text()
            arrival = json.loads(text)
            print('json do')
            arrival = arrival['arrival']
            print('json after')
            return arrival
