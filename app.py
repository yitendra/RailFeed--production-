from flask import Flask, render_template, request, jsonify
import classifier as clf
from util import CUR_DIR
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
#     return "hello world!"
      return render_template('index.html')  


""" 
        @method POST /review
        @access Public
        Test single input via the application 
"""
@app.route('/review', methods=['POST'])
def review():
        text = request.get_json()
        Y = clf.classify(text['review'])
        # print(Y)
        return jsonify({'message': text['review']})


""" 
        @method POST /upload
        @access Public
        File Upload 
"""
@app.route('/upload', methods=['POST'])
def csvFile():
        csv = request.files['file']
        filename = csv.filename
        csv.save(os.path.join(CUR_DIR,'media',filename))
        return "file Upload successful"


""" 
        @method POST /review/{text}
        @access Public
        Test single input via only the api endpoint
"""
@app.route('/review/<string:name>')
def getReview(name):
        Y = clf.classify(name)
        return jsonify({"msg": Y})





if __name__ == '__main__':
    app.run(debug=True)