from flask import Flask, render_template


# import the Blueprint objects
from blueprints.suppliers       import bp as suppliers_bp
from blueprints.licenses        import bp as licenses_bp
from blueprints.branches        import bp as branches_bp
from blueprints.departments     import bp as departments_bp
from blueprints.employees       import bp as employees_bp
from blueprints.transactions    import bp as transactions_bp
from blueprints.ticketing       import bp as ticketing_bp
from blueprints.offers          import bp as offers_bp
from blueprints.payments        import bp as payments_bp
from blueprints.films           import bp as films_bp
from blueprints.customers       import bp as customers_bp
from blueprints.memberships     import bp as memberships_bp
from blueprints.categories      import bp as categories_bp
from blueprints.themestores     import bp as themestores_bp
from blueprints.customer import bp as customer_bp


app = Flask(__name__)
app.secret_key = "IUFYBGUDuuigbusirihHUUIFGFbhuirdg"
# register each Blueprint
app.register_blueprint(customer_bp)
app.register_blueprint(suppliers_bp)
app.register_blueprint(licenses_bp)
app.register_blueprint(branches_bp)
app.register_blueprint(departments_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(ticketing_bp)
app.register_blueprint(offers_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(films_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(memberships_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(themestores_bp)

@app.route('/admin')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

