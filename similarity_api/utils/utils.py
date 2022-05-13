import numpy as np
import string
import pickle
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text):
    """
    Got string object for clean

    Input: str
    Output: str
    """
    black_list = ['ml', 'gr', 'lt', 'kg']
    delete_dict = {
        sp_character: ' ' for sp_character in string.punctuation}
    delete_dict[' '] = ' '
    table = str.maketrans(delete_dict)
    text1 = text.translate(table)
    textArr = text1.split()
    text2 = ' '.join([w for w in textArr if (
        not w.isdigit() and (not w.isdigit() and len(w) > 1))])
    text2 = text2.split(' ')
    text2 = ' '.join([word for word in text2 if (word not in black_list)])
    
    return text2.lower()


def load_data(path):
    """
    load products
    """
    try:
        with open(path, 'rb') as handle:
            data = pickle.load(handle)
        print('Data Loaded...')
    except IOError as exc:
        print(str(exc))
    return data


def load_model(path):
    """
    Load word2vec model
    """
    try:
        model = Word2Vec.load(path)
        print("Model Loaded...")
    except IOError as exc:
        print(str(exc))
    return model


def get_cart_avg(model, data):
    """
    model: Word2Vec model
    data: cleaned cart items
    """
    
    cart_vectors = np.zeros((300,))
    c = 0
    for sent in data:
        sent = sent.split(' ')
        for word in sent:
            word_vector = model.wv.get_vector(word)
            cart_vectors += word_vector
            c += 1
    return cart_vectors / c


def recommanded(products, avg_cart, cart):
    """
    Get 10 most similar products

    products: all_products
    avg_cart: average or cart vectors
    cart: current products on cart
    """
    similar = []
    recommanded = {
        "cart" : cart,
        "similar_items" : []
    }

    # calculate cart average with all products
    for i in range(len(products)):
        similarity = cosine_similarity(avg_cart.reshape(
            1, -1), products.avg[i].reshape(1, -1))
        if similarity > 0.8:
            item = {
                'productName': products.features[i],
                'similarity': similarity[0][0]
            }
            similar.append(item)

        if len(similar) == 10:
            break

    sorted_data = sorted(similar, key=lambda i: i['similarity'], reverse=True)
    
    # dont recommend if similar item same on the cart
    for item in sorted_data:
        if item['productName'] not in cart:
            recommanded['similar_items'].append(item)
    
    return recommanded
