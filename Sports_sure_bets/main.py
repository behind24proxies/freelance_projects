import requests
import time
import json
import datetime

now = datetime.datetime.now()


def get_sure(code):
    list_pay = []

    url = f'https://oddspedia.com/api/v1/getSurebets?markets=&profitPercentage=1.00%2C1000.00&geoCode={code}&geoState=&sports=&bookmakers=&wettsteuer=0&sort=profit&language=en'
    jned = requests.get(url).json()
    for count, x in enumerate(jned['data']):
        temp_date = str(x['md'])[0:-6]
        print(temp_date)
        try:

            date = datetime.datetime.strptime(temp_date, '%Y-%m-%d %H:%M')
            diff = now-date
            print(count)
            element = {
                'pay': x['payout'],
                'day': diff.days,
                'type': x['ot_name'],
                'odds': x['odds']
            }
            list_pay.append(element)
            print(element)
        except Exception as e:
            print(e)
            try:
                element = {
                    'pay': x['payout'],
                    'day': diff.days
                }
                list_pay.append(element)
            except:
                print('error')
    list_pay.sort(key=lambda x: x['day'])
    print(list_pay)
    with open('sure.json', 'w') as f:
        f.write(json.dumps(list_pay))


# well, the oddspedia api works with lots of geo codes, UK is one of them
get_sure('UK')

print('done')
