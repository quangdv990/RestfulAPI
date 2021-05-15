from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

student_infor = {
    'ID1': {'tensv': 'tensv1', 'age': 30, 'gender':'Male', 'email':'tensv1@gmail.com', 'class':'Mathematics', 'school': 'PCT'},
    'ID2': {'tensv': 'tensv2', 'age': 31, 'gender':'Male', 'email':'tensv1@gmai2.com','class':'English', 'school': 'PCT'},
    'ID3': {'tensv': 'tensv3', 'age': 35, 'gender':'Female','email':'tensv1@gmai3.com', 'class':'Music', 'school': 'PCT'}
}
parse = reqparse.RequestParser()

class StudentList (Resource):
    def get(self):
        return student_infor

    def post(self):
        parse.add_argument('tensv')
        parse.add_argument('age')
        parse.add_argument('gender')
        parse.add_argument('email')
        parse.add_argument('class')
        parse.add_argument('school')
        args = parse.parse_args()
        student_id = int(max(student_infor.keys())) + 1
        student_id = '%i' % student_id
        student_infor[student_id] = {
            'name': args['name'],
            'age': args['age'],
            'gender': args['gender'],
            'email': args['email'],
            'class': args['class'],
            'school': args['school'],
        }
        return student_infor[student_id], 201

class Sinhvien(Resource):
    def get(self, student_id):
        return student_infor[student_id]

api.add_resource(StudentList,'/student_infor')

if __name__ == '__main__':
    app.run(debug=True)
