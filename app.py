from flask import Flask, render_template, request, jsonify
import classifier as clf
from classifier import CUR_DIR
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
#     return "hello world!"
      return render_template('index.html')  

# @app.route('/success',methods=['POST'])
# def success():
#     if request.method == 'POST':
        
#         review = request.form['user_review']
#         Y = clf.classify(review)
#         return render_template('success.html',val=Y)

@app.route('/review', methods=['POST'])
def review():
        text = request.get_json()
        Y = clf.classify(text['review'])
        print(Y)
        return jsonify({'message': Y})

@app.route('/upload', methods=['POST'])
def csvFile():
        csv = request.files['file']
        filename = csv.filename
        csv.save(os.path.join(CUR_DIR,'media',filename))
        return "file Upload successful"


if __name__ == '__main__':
    app.run(debug=True)