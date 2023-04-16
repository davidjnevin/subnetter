import ipaddress

from flask import Flask, jsonify, redirect, render_template, request, url_for

from subnetter.subnet_calculator import calculate_subnet

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    ip_address = request.form['ip_address']
    subnet_mask = request.form['subnet_mask']
    result = calculate_subnet(ip_address, subnet_mask)

    if result.get('error'):
        # Handle error
        return render_template('index.html', error=result['error'])

    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
