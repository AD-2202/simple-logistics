from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shipments = []

@app.route('/')
def index():
    return render_template('index.html', shipments=shipments)

@app.route('/add', methods=['POST'])
def add():
    shipment = {
        'id': len(shipments) + 1,
        'description': request.form['description'],
        'method': request.form['method'],
        'status': request.form['status'],
        'cost': request.form['cost']
    }
    shipments.append(shipment)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
