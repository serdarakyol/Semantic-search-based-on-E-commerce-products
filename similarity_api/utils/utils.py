import string
import pickle
from gensim.models import Word2Vec
from numba import jit, prange
from numpy import dot, ndarray, zeros, float64, argmax
from numpy.linalg import norm


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
    Calculate average of cart

    model: Word2Vec model
    data: cleaned cart items

    Return: Returns vector with size 300
    """
    
    cart_vectors = zeros((300,))
    c = 0
    for sent in data:
        sent = sent.split(' ')
        for word in sent:
            word_vector = model.wv.get_vector(word)
            cart_vectors += word_vector
            c += 1
    return cart_vectors / c


@jit(nopython=True, fastmath=True)
def calculate_cos_similarity(first_item:ndarray, second_item:ndarray):
    """
    Calculates cosine similarity between 2 vectors
    
    first_item: First item to calculate similarty
    second_item: Second item to calculate similarty
    
    Return: Similarity score
    """
    dt = dot(first_item, second_item)
    if abs(dt) < 1e-10:
        return 0
    else:
        return dt/norm(first_item)/norm(second_item)


@jit(nopython=True, parallel=True)
def get_scores_parallel(multiple_item:ndarray, single_item:ndarray):
    """
    Calculate similarity between 1 to many item

    multiple_item: Banch of item to calculate similarity
    single_item: Single item to calculate similarity

    Return: Similarity scores
    """
    n = multiple_item.shape[0]
    #n:int = 10235
    scores = zeros(shape=(n), dtype=float64)
    for i in prange(n):
        scores[i] = calculate_cos_similarity(first_item=single_item, second_item=multiple_item[i])

    return scores


def calculate(multiple_item:ndarray, single_item:ndarray):
    """
    Calculates cosine similarity between a item and whole dataset
    
    multiple_item: All dataset to calculate with single_item
    single_item: Single item to calculate for whole dataset
    
    Return: Similarity between single_item and multiple_item[i]
    """
    # create 10235x300 shape of array
    mult = zeros(shape=(multiple_item.shape[0], multiple_item[0].shape[0]), dtype=float64)
    for i in range(mult.shape[0]):
        mult[i] = multiple_item[i]
    
    return get_scores_parallel(multiple_item=mult, single_item=single_item)

def recommanded(products, avg_cart, cart):
    """
    Get 10 most similar products

    products: all_products
    avg_cart: average or cart vectors
    cart: current products on cart

    Return: 10 recommanded products with similarities
    """
    results = []
    recommanded = {
        "cart" : cart,
        "similar_items" : []
    }
    # calculate average cart with other products
    scores = calculate(multiple_item=products.avg.to_numpy(), single_item=avg_cart)
    
    # get top 10 similar products:
    for i in range(10):
        index = argmax(scores)
        temp = {
            "productName":products.features[index],
            "similarity": scores[index]
        }
        results.append(temp)
        scores[index] = 0

    # sort
    results = sorted(results, key=lambda x: x["similarity"], reverse=True)
    for item in results:
        if item['productName'] not in cart:
            recommanded['similar_items'].append(item)

    return recommanded
