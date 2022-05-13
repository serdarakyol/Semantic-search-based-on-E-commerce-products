#from os.path import dirname, abspath

from similarity_api.models.model_recommend import SimilarityRequest, SimilarityResponse
from similarity_api.utils.utils import clean_text, load_data, load_model, get_cart_avg, recommanded

#ROOT_DIR = dirname(dirname(abspath(__file__)))
#MODEL = load_model(ROOT_DIR + "/models/den_hepsi_burada_word2vec.model")
#PRODUCTS = load_data(ROOT_DIR + "/data/final_products.pkl")


class Recommend:
    def __init__(self, model, product) -> None:
        self.model = model
        self.product = product

    def recommend(self, item_name: SimilarityRequest) -> SimilarityResponse:
        cart_products = item_name.product_names
        
        clean_products = []
        for product in cart_products:
            clean_products.append(clean_text(product))

        # get cart of average
        avg_cart = get_cart_avg(self.model, clean_products)
        
        # find similar items
        results = recommanded(self.product, avg_cart, cart_products)

        return results
