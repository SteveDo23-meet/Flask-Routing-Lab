from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def idk():
    return render_template("home.html")

@app.route('/product')
def idok():
    return render_template("product.html")

@app.route('/dior_low')
def dior():
    return render_template("dior1.html")

@app.route('/chicago')
def chicago():
    return render_template("Trophy.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/checkout')
def pay():
    return render_template("checkout.html")





# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
