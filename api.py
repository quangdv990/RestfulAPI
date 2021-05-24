from typing import get_args
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import json


app = Flask(__name__)
api = Api(app)

student_infor = {
    '1': {'tensv': 'tensv1', 'age': 30, 'gender':'Male', 'email':'tensv1@gmail.com', 'class':'Mathematics', 'school': 'PCT'},
    '2': {'tensv': 'tensv1', 'age': 31, 'gender':'Male', 'email':'tensv2@gmail.com','class':'English', 'school': 'PCT'},
    '3': {'tensv': 'tensv3', 'age': 35, 'gender':'Female','email':'tensv3@gmail.com', 'class':'Music', 'school': 'PCT'}
}
parse = reqparse.RequestParser()


#class StudentList (Resource):
@app.route('/')
def get():
    return student_infor
@app.route('/', methods=["POST"])
def post():
        parse.add_argument('tensv')
        parse.add_argument('age')
        parse.add_argument('gender')
        parse.add_argument('email')
        parse.add_argument('class')
        parse.add_argument('school')
        args = parse.parse_args()
        student_id = int(max(student_infor.keys())) + 1
       
        student_infor[student_id] = {
            'tensv': args['tensv'],
            'age': args['age'],
            'gender': args['gender'],
            'email': args['email'],
            'class': args['class'],
            'school': args['school'],
        }
        
        with open('sv.json','w') as f:
            json.dump(student_infor, f)

        return student_infor[student_id], 201


@app.route('/data', methods=['GET'])
def get_query_string():
    r = {}
    email = request.args.get("email")
    for i in student_infor: # 1, 2, 3
        # student_infor[i] = {'tensv': 'tensv1', 'age': 30, 'gender':'Male', 'email':'tensv1@gmail.com', 'class':'Mathematics', 'school': 'PCT'}
        for j in student_infor[i]:
            v = student_infor[i][j]
            if j == "email" and v == email:
                return student_infor[i], 200

@app.route('/datatensv', methods=['GET'])
def get_query_string():
    r = {}
    tensv = request.args.get("tensv")
    for i in student_infor: # 1, 2, 3
        # student_infor[i] = {'tensv': 'tensv1', 'age': 30, 'gender':'Male', 'email':'tensv1@gmail.com', 'class':'Mathematics', 'school': 'PCT'}
        for j in student_infor[i]:
            v = student_infor[i][j]
            if j == "tensv" and v == tensv:
                return student_infor[i], 200  
class Sinhvien(Resource):
    def get(self, student_id):
        return student_infor[student_id]

api.add_resource(Sinhvien,'/student_infor')

if __name__ == '__main__':
    app.run(debug=True)
