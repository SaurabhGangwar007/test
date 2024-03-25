from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('carSales.html')

@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    # Get form data
    year = request.form['year']
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    condition = request.form['condition']
    fuel = request.form['fuel']
    odometer = request.form['odometer']

    # Perform price calculation (replace with actual logic)
    # For demonstration purposes, returning a static price
    price = 20000

    # Render car_sales2.html with the processed data
    return render_template('carSales2.html', year=year, manufacturer=manufacturer, model=model, condition=condition, fuel=fuel, odometer=odometer, price=price)

if __name__ == '__main__':
    app.run(debug=True)