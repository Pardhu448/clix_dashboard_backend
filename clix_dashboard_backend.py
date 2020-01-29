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
@click.option('--username', help='Username to create admin user for clix_dashboard_backend (mostly used during initial setup) {Mandatory}')
@click.option('--password', help='Password to create admin user for clix_dashboard_backend (mostly used during initial setup)')
@click.option('--email', help='Email to create admin user for clix_dashboard_backend (mostly used during initial setup)')
def create_admin(username, password = "", email = ""):
    print('Creating Admin User(', username, ') for CLIx_dashboard_backend\n')

    if not password:
        print('Enter Password for UserName( {}'.format(username), "):")
        password = input()

    if not email:
        print('Enter emailID:')
        email = input()

    adminuser = User(username=username, password=password)
    #adminuser.set_password(password=password)
    db.session.add(adminuser)
    db.session.commit()
    print('Congratulations, you are now a admin user for CLIx Daashboard Backend!')
    return None