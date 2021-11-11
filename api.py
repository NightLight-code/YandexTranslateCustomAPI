import requests
import json



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://translate.yandex.ru/?lang=en-ru&text=How%20are%20u%3F',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://translate.yandex.ru',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Cache-Control': 'max-age=0',
    'TE': 'trailers',
}



def translate(text, from_lang, to_lang):
    params = (
        ('id', 'f2e32741.618d63e2.59c9da0c.74722d74657874-0-0'),
        ('srv', 'tr-text'),
        ('lang', from_lang + '-' + to_lang),
        ('reason', 'paste'),
        ('format', 'text'),
        ('yu', '2376453801629721395'),
        ('yum', '1629721397668637732'),
    )
    data = {
      'text': text,
      'options': '4'
    }
    response = requests.post('https://translate.yandex.net/api/v1/tr.json/translate', headers=headers, params=params, data=data)

    json_responce = json.loads(response.text)
    return (json_responce)["text"][0]
