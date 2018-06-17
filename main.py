# -*- coding: utf-8 -*-
import json
import requests

URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос

f = open(r'data.json', "wb")
ufr = requests.get("https://tickets.fifa.com/API/WCachedL1/ru/BasicCodes/GetBasicCodesAvailavilityDemmand?currencyId=USD")
f.write(ufr.content)
f.close()

with open('data.json') as data_file:
    data_item = json.loads(data_file.read())

    for i in data_item['Data']['Availability']:
        if i['a'] == 1 and i['c'] in (17, 56) and i['p'] in ('IMT20', 'IMT23', 'IMT30', 'IMT42', 'IMT50', 'IMT51', 'IMT52', 'IMT56', 'IMT57', 'IMT58', 'IMT62', 'IMT64'):

            if i['c'] == 17:
                cat = '****** CAT 4'
            elif i['c'] == 56:
                cat = '****** OV'

            if i['p'] == 'IMT20':
                match = '20.06 21:00, Kazan, Iran - Spain'
            elif i['p'] == 'IMT23':
                match = '21.06 21:00, Nizhny Novgorod, Argentina - Horvatia'
            elif i['p'] == 'IMT30':
                match = '24.06 15:00, Nizhny Novgorod, England - Panama'
            elif i['p'] == 'IMT42':
                match = '27.06 21:00, Nizhny Novgorod, Schveizaria - Kosta-Rica'
            elif i['p'] == 'IMT50':
                match = '30.06 17:00, Kazan'
            elif i['p'] == 'IMT51':
                match = '01.07 17:00, Moscow'
            elif i['p'] == 'IMT52':
                match = '01.07 21:00, Nizhny Novgorod'
            elif i['p'] == 'IMT56':
                match = '03.07 21:00, Moscow'
            elif i['p'] == 'IMT57':
                match = '06.07 17:00, Nizhny Novgorod'
            elif i['p'] == 'IMT58':
                match = '06.07 21:00, Kazan'
            elif i['p'] == 'IMT62':
                match = '11.07 21:00, Moscow'
            elif i['p'] == 'IMT64':
                match = '15.07 18:00, Moscow'

            print(match, cat)

            message_data = {  # формируем информацию для отправки сообщения
                'chat_id': 159496178,  # куда отправляем сообщение
                'text': match + cat,  # само сообщение для отправки
                'parse_mode': 'HTML'  # про форматирование текста ниже
            }

            #try:
            #    request = requests.post(URL + 'sendMessage', data = message_data)  # запрос на отправку сообщения
            #except:
            #    print('Send message error')
            #    return False

            #if not request.status_code == 200:  # проверим статус пришедшего ответа
            #    return False

