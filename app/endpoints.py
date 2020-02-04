import werkzeug
from flask import Flask, jsonify, abort, make_response, g, send_from_directory
from flask_restful import Api, Resource, reqparse, fields, marshal
# from flask_login import login_user, logout_user, current_user, login_required
from app import app
from app.models.school.schema import Metric1, Metric2, Metric3, Metric4, Metric5, Metric6, SchoolInfo, SchoolImage
from app.models.user.schema import User
from flask import Blueprint, request, make_response, jsonify
from app import bcrypt
from app.middleware import login_required
from sqlalchemy import desc, asc

from app import db
from datetime import datetime
from flask import url_for

api = Api(app)

upload_folder = app.config['UPLOAD_FOLDER']

'''
@app.after_request
def add_no_cache_header(response):
    response.headers["Cache-Control"] = "no-store"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Sample flask endpoints using resource module
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
'''

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
            school_user_code = User.query.filter_by(id=g.user).first().username

            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]

            school_attendance_table = Metric1.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric1.date)).distinct(Metric1.date).all()
            # Distinct by date and school_server_code as we have only one log per date per school
            school_serverup_table = Metric4.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric4.date)).first()

            school_tools_table = Metric3.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric3.date)).distinct(Metric3.date).all()

            school_modules_table = Metric2.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric2.date)).distinct(Metric2.date).all()

            school_tools_attendance = Metric5.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric5.date)).distinct(Metric5.date).all()

            school_modules_attendance = Metric6.query.filter_by(
                school_server_code=school_server_code
            ).order_by(desc(Metric6.date)).distinct(Metric6.date).all()

            def serialize_data(record):
                if record is not None:
                    record_dict = dict((col, getattr(record, col)) for col in record.__table__.columns.keys())
                    record_dict['date'] = record_dict['date'].strftime("%Y%m%d")
                    return record_dict
                else:
                    return None

            school_attendance_json = [serialize_data(each) for each in school_attendance_table]
            school_serverup_json = [serialize_data(school_serverup_table)]
            school_tools_json = [serialize_data(each) for each in school_tools_table]
            school_modules_json = [serialize_data(each) for each in school_modules_table]
            school_tools_attendance_json = [serialize_data(each) for each in school_tools_attendance]
            school_modules_attendance_json = [serialize_data(each) for each in school_modules_attendance]

            responseObject = {
                'status': 'success',
                'message': 'Successfully Fetched data Table.',
                'data_attendance': school_attendance_json,
                'data_serverup': school_serverup_json,
                # 'data_tools': school_tools_json,
                # 'data_modules': school_modules_json,
                'data_tools_attendance': school_tools_attendance_json,
                'data_modules_attendance': school_modules_attendance_json,
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


class SchoolInfoAPI(Resource):
    """
    Resource to fetch school information - description and image uploaded
    """
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(SchoolInfoAPI, self).__init__()

    def get(self):
        # parse client json data
        # args = self.reqparse.parse_args()
        # post_data = request.get_json()
        try:
            # fetch the user data
            school_user_code = User.query.filter_by(id=g.user).first().username
            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]
            school_description = SchoolInfo.query.filter_by(school_server_code=school_server_code
                                                            ).order_by(desc(SchoolInfo.dateUpdated
                                                                            )).first().schoolDescription

            if school_description:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully Fetched School Info.',
                    'schoolDescription': school_description,
                    'username': school_server_code
                }
                return make_response(jsonify(responseObject), 200)

            else:
                responseObject = {
                    'status': 'success',
                    'message': 'No entry of description for the school yet'
                }
                return make_response(jsonify(responseObject), 200)

        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)

    def post(self):
        # get the post data
        # args = self.reqparse.parse_args()
        post_data = request.get_json()

        try:
            school_user_code = User.query.filter_by(id=g.user).first().username
            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]

            schoolDescription = post_data['schoolDescription']
            dateUpdated = datetime.utcnow()
            school_record = SchoolInfo(school_server_code=school_server_code,
                                       dateUpdated=dateUpdated,
                                       schoolDescription=schoolDescription)

            db.session.add(school_record)
            db.session.commit()
            responseObject = {
                'status': 'Success',
                'message': 'School Description Updated'
            }

            return make_response(jsonify(responseObject), 200)

        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)


class SchoolImageAPI(Resource):
    """
    Resource to fetch school information - description and image uploaded
    """
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(SchoolImageAPI, self).__init__()

    def get(self):
        # parse client json data
        # args = self.reqparse.parse_args()
        # post_data = request.get_json()
        try:
            # fetch the user data
            school_user_code = User.query.filter_by(id=g.user).first().username
            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]
            school_image_name = SchoolImage.query.filter_by(school_server_code=school_server_code
                                                          ).order_by(
                desc(SchoolImage.dateUpdated)).first().schoolImageName

            mime_type = 'image/' + school_image_name.split('.')[1]

            if school_image_name is not None:
                #schoolImagePath = upload_folder + '/' + school_image_name
                #responseObject = {
                #    'status': 'Success',
                #    'message': 'Image found for the school',
                #    'username': school_server_code,
                #    'schoolImage': url_for(schoolImagePath)
                #}
                imageResponse = make_response(send_from_directory(upload_folder, school_image_name, mimetype=mime_type))
                imageResponse.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                imageResponse.headers['Pragma'] = 'no-cache'
                return imageResponse
                #return make_response(jsonify(responseObject), 200)

            else:
                responseObject = {
                    'status': 'Success',
                    'message': 'No upload of image for the school yet'
                }
                return make_response(jsonify(responseObject), 200)

        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)

    def post(self):

        # get the post data
        parser = self.reqparse
        parser.add_argument('imageFile', type=werkzeug.datastructures.FileStorage, location='files')

        # args = parser.parse_args()
        imageFile = request.files['ImageFile']
        mimetype = request.files['ImageFile'].mimetype.split('/')[1]
        mime_type = 'image/' + mimetype

        try:
            school_user_code = User.query.filter_by(id=g.user).first().username
            school_server_code = school_user_code[-7:] + '-' + school_user_code[0:-7]

            dateUpdated = datetime.utcnow()
            image_file_name = school_server_code + dateUpdated.strftime('_%Y%b%d_%Hh%Mm%Ss') + '.' + mimetype
            school_record = SchoolImage(school_server_code=school_server_code,
                                        dateUpdated=dateUpdated,
                                        schoolImageName=image_file_name)

            schoolImagePath = upload_folder + '/' + image_file_name
            imageFile.save(schoolImagePath)
            db.session.add(school_record)
            db.session.commit()

            responseObject = {
                'status': 'Success',
                'message': 'Image Uploaded',
                'lastupdatetime': dateUpdated.strftime('%Y%b%d_%Hh%Mm%Ss')
            }
            #return send_from_directory(upload_folder, image_file_name, mimetype = mime_type)
            return make_response(jsonify(responseObject), 200)
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again. Failed to upload Image'
            }
            return make_response(jsonify(responseObject), 500)


api.add_resource(SchoolImageAPI, '/schoolimage', endpoint='schoolimage')
api.add_resource(SchoolInfoAPI, '/schoolinfo', endpoint='schoolinfo')
api.add_resource(GetDataAPI, '/getschooldata', endpoint='getschooldata')
api.add_resource(AuthenticateAPI, '/authenticate', endpoint='authenticate')

# api.add_resource(TaskListAPI, '/tasks', endpoint='tasks')
# api.add_resource(SchoolAPI, '/tasks/<int:id>', endpoint='task')
