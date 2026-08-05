import json

import aiohttp

from calculates import authKEY, message



async def list_of_arriving_buses_post():
    url = "https://tosamara.ru/api/v2/json"

    json_data = {
        'clientId': "SmrSmartCity",
        'os': 'android',
        'authKey': authKEY,
        'message': message
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=json_data) as response:
            text = await response.text()
            arrival = json.loads(text)
            arrival = arrival['arrival']
            return arrival
