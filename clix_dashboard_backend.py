from app import app, db
from app.models.user.schema import User
import click
#from app.scripts import dataupload

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

#@app.cli.command()
#@click.option('--schooldata', help='To load school data into SQLite/Postgreql DB, done during initial setup')
#def loaddata(schooldata):
#    print('Loading all school Data from {}'.format(schooldata))
#    return dataupload.upload_schooldata(schooldata, db = db)

@app.cli.command()
@click.option('--username', help='To create admin user for clix_dashboard_backend, done during initial setup')
def create_admin(username):
    print('Creating Admin User for CLIx_dashboard_backend\n')
    print('Enter Password for UserName: {}'.format(username))
    passwd = input()
    print('Enter emailID:')
    email = input()
    adminuser = User(username=username, password=passwd)
    #adminuser.set_password(password=passwd)
    db.session.add(adminuser)
    db.session.commit()
    print('Congratulations, you are now a admin user for CLIx Daashboard Backend!')
    return None


