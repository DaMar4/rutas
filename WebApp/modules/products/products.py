from flask import Blueprint,render_template
products = Blueprint("products",__name__)
@products.route("/productos",methods=["GET","POST"])
def devices():
    return render_template("productos.html")