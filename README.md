# Recommendation System
This repository tried to solve recommendation problem in e-commerce. Suggesting a new product that the customer may like based on the products in the cart.

# Word embedding (About model)
Word2Vec(w2v) model chose because I can define the size of output of model with w2v model while training the model. That model uses neural network model to learn word associations from corpus of text. That model contain 2 layer neural networks. Word2vec can utilize either of two model architectures to produce a distributed representation of words. One is continuous bag-of-words (CBOW), another one is continuous skip-gram. Some articles shows that CBOW is faster but skip-gram has better effient for infrequent words.

# Usage
For use the the API, just follow the below codes
#### $ git clone https://github.com/serdarakyol/recommendation-system.git
#### $ cd recommendation-system 
#### $ virtualenv env
#### $ source env/bin/activate
#### $ pip install -r requirements.txt
#### $ uvicorn main:app --reload
Go to http://127.0.0.1:8000/docs on your local machine. Click on the similarity and write your cart products for get system can recommand you

### Request body
![Request Body](1.png)

### Response body
![Response Body](2.png)

# Pros 
1. That demo works well for text-based and small data. 
2. The model is not large. Therefore model can work efficiently
 
# Cons
1. API won't work efficiently for big data 

# If there was enough time
1. If the data could be fit to apriori algorithm, I believe that demo would work more efficiently.
2. I could research about collaborative filtering and implement that to this demo
3. Learn more about FastAPI and improve API

