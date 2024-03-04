from flask import Flask, request, jsonify, render_template
import flask
import pandas as pd
from flask_cors import CORS  # Import the CORS module
from chatgpt import Prompt

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for all routes in the app 

@app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/processing_prompt', methods=['POST', 'GET'])
def call_api():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data['prompt']
        result = f'{prompt} is my question'
        return jsonify({'result': result})

    return render_template('index.html')

@app.route('/helloword', methods=['POST', 'GET'])
def helloword():
    data_return = {}
    if request.form.get("input"):
        input = request.form.get("input")
        template = request.form.get('selectedValue')

        # result = (input, template)
        result = Prompt(input, template)
        data_return = {
            'data_out': result #result
        }
        print('type:', type(result))
    else:
        print('Failed')

    json_output = jsonify(data_return)
    print(json_output)
    return json_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

