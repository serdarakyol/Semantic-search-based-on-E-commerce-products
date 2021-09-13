from recommendation_api import utils
from fastapi import FastAPI

model = utils.load_model(
    'recommendation_api/models/w2v.model')

products = utils.load_data('recommendation_api/data/prod.pkl')


app = FastAPI()
"""a = ["Bakliyat, Pirinç, Makarna, Türkiye Tarım Kredi Koop.Yeşil Mercimek 1 kg",
     "Bakliyat, Pirinç, Makarna, Reis Gönen Baldo Pirinç 1 kg"]
print(utils.clean_text(a))"""


def recommand(cart: list):
    clean_cart = utils.clean_text(cart)
    avg_cart = utils.get_cart_avg(model, clean_cart)
    recom = utils.recommanded(products, avg_cart, cart)
    print(recom)
    return recom


@ app.post('/similarity')
def similarity(cart: list):
    return recommand(cart)


@ app.post('/cleancontent')
def clean_text(text: list):
    return utils.clean_text(text)
