import pandas
import sys
import os
from datetime import datetime
from app.models import SyncStatus

def upload_schooldata(school_data_path, db):
    db_conn = db.engine
    data = pandas.read_csv(os.path.abspath(school_data_path))
    table_name = 'syncstatus'

    data['lastupdated'] = datetime.utcnow()
    data['previous_update_date'] = datetime.utcnow() - datetime.timedelta(1)
    data['currentfilesize'] = '4321KB'
    data['previousfilesize'] = '2321KB'

    cols = ['schoolname', 'schoolcode', 'state', 'lastupdated', 'district', 'previous_update_date', 'currentfilesize', 'previousfilesize']
    data = data[cols]

    ## TODO: Need to map district code to district names
    district_code_map = {}

    column_type_dict = {
    'state': 'object',
    'schoolcode': 'object',
    'lastupdated': 'datetime64',
    'schoolname': 'object',
     'district': 'object',
     'previous_update_date': 'datetime64',
     'currentfilesize': 'object',
     'previousfilesize': 'object'
     }
    data = data.astype(column_type_dict)
    for school in data.iterrows():
        school_record = school[1]
        record = SyncStatus(state=school_record['state'],
        schoolcode = school_record['schoolcode'],
        lastupdated = school_record['lastupdated'],
        schoolname = school_record['schoolname'],
        district = school_record['district'])
        db.session.add(record)
        db.session.commit()

    print('Done uploading school data into SQLite db')
    return None
