import subprocess
from subprocess import check_output
from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)


# flipkart
@app.route('/flipkart', methods = ['GET'])
def flipkart():
    product_name =  request.args['q']
    open('output.jl', 'w').close()
    if product_name:
        data = []
        # flipkart
        p = subprocess.check_output(
            'scrapy runspider flipkart.py -a category="{}" -o output.jl'.format(product_name), 
            shell=True)
        with open('output.jl') as f:
            for line in f:
                data.append(json.loads(line))
        return jsonify(sorted(data, key = lambda i: i['product_price']))
    return "Querry param not passed"

# amazon
@app.route('/amazon', methods = ['GET'])
def amazon():
    product_name =  request.args['q']
    open('output.jl', 'w').close()
    if product_name:
        data = []
        p = subprocess.check_output(
            'scrapy runspider amazon.py -a category="{}" -o output.jl'.format(product_name), 
            shell=True)
        with open('output.jl') as f:
            for line in f:
                data.append(json.loads(line))
        return jsonify(sorted(data, key = lambda i: i['product_price']))

    return "Querry param not passed"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


