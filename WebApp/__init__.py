from flask import Flask
app = Flask(__name__)
from WebApp.modules.home.home import index
from WebApp.modules.products.products import products
app.register_blueprint(index)
app.register_blueprint(products)