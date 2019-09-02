from flask import Flask, jsonify, abort, make_response, g
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from app.models.school.schema import Metric1, Metric2
from app.models.user.schema import User
from flask import Blueprint, request, make_response, jsonify
from app import bcrypt
from app.middleware import login_required


api = Api(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TaskListAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': [marshal(task, task_fields) for task in tasks]}

    def post(self):
        args = self.reqparse.parse_args()
        task = {
            'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201


class SchoolAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('school_server_code', type=str, location='json')
        self.reqparse.add_argument('state', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(SchoolAPI, self).__init__()

    def get(self, school_server_code):
        school_m1 = Metric1
        school_data = []
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        return {'task': marshal(task[0], task_fields)}

    def put(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}

class AuthenticateAPI(Resource):
    """
    User Login Resource
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(AuthenticateAPI, self).__init__()

    def post(self):
        # get the post data
        # args = self.reqparse.parse_args()
        post_data = request.get_json()

        try:
            # fetch the user data
            user = User.query.filter_by(
                username=post_data['username']
            ).first()

            if user and bcrypt.check_password_hash(
                user.password_hash, post_data['password']
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully Authenticated.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject), 200)
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject), 404)
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)

class GetDataAPI(Resource):
    """
    Resource to fetch school level data table (of all the metrics) from clix_dashboard_postgres db
    """
    decorators = [login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(GetDataAPI, self).__init__()

    def get(self):
        # parse client json data
        # args = self.reqparse.parse_args()
        # post_data = request.get_json()
        try:
            # fetch the user data
            school_user_code = User.query.filter_by(id = g.user).first().username
            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]
            school_table = Metric1.query.filter_by(
                school_server_code=school_server_code
            ).all()

            def serialize_data(record):
                return {
                    "id": record.id,
                    "school_server_code": record.school_server_code,
                    "date": record.date.strftime("%Y%m%d"),
                    "attendance_tools": record.attendance_tools,
                    "attendance_modules": record.attendance_modules,
                    "state": record.state,
                    "district": record.district
                }

            school_table_json = [serialize_data(each) for each in school_table]

            responseObject = {
                'status': 'success',
                'message': 'Successfully Fetched data Table.',
                'data': school_table_json,
                'username': school_server_code
                }
            return make_response(jsonify(responseObject), 200)
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)

api.add_resource(GetDataAPI, '/school', endpoint='school')
api.add_resource(AuthenticateAPI, '/authenticate', endpoint='authenticate')

#api.add_resource(TaskListAPI, '/tasks', endpoint='tasks')
#api.add_resource(SchoolAPI, '/tasks/<int:id>', endpoint='task')
