import requests
import bs4
from lexicon import lexicon_ru
from lexicon.lexicon_en import cars_dict


"""This parser gets information about average price of a few famous car models in Bishkek.
This data may be interesting for car sellers"""


def get_model_price(model):
    result = []
    amount_of_cars = 0
    for i in range(1, 10):
        site = requests.get(cars_dict[model].format(i))
        pars = bs4.BeautifulSoup(site.text, 'lxml')
        elems = pars.select('div > p > span')
        for j in elems:
            if str(j).endswith('KGS</span>'):
                result.append(int(str(j)[6:-10].replace(" ", "")))
                amount_of_cars += 1
            elif str(j).endswith('USD</span>'):
                konvertaciya = int(int(str(j)[6:-10].replace(" ", "")) * 84.45)
                result.append(konvertaciya)
                amount_of_cars += 1
    average_lalafo_price = int(sum(result) / len(result))
    data = f'Средняя цена авто {lexicon_ru.cars_ru[model]}\n{average_lalafo_price} KGS'
    return data
