# from flask import Flask

import numpy as np
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
# from model import NLPModel
import pickle

app = Flask(__name__)# Load the model
api = Api(app)


model = pickle.load(open('mod.pkl','rb'))
parser = reqparse.RequestParser()
parser.add_argument('query')

class Predict(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        exam_query=[0,  0,  0,  0,  0,  0,  1,  1,  0,  1, 28,  3,  1,  0,  1]
        
        prediction = model.predict(np.array([user_query]))
        

        # Output either 'Negative' or 'Positive' along with the score
        if int(prediction[0]) == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'
            
     

        # create JSON object
        output = {'prediction': pred_text}
        
        return output


api.add_resource(Predict, '/')


if __name__ == '__main__':
    app.run(debug = True)

