from matplotlib import blocking_input
from numpy import outer
from flask import Flask,  Blueprint, render_template
from flask_login import login_required, current_user
from untitled_blog_thing.blog_app.app.models import User
from . import firestore_db, db

main = Blueprint('main', __name__)
app = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/project_list')
@login_required
def profile():
    project_list  = [doc['title'] for doc in firestore_db.collection(current_user.id).stream()]
    project_ids = [doc.id for doc in firestore_db.collection(current_user.id).stream()]
    return render_template('project_list.html', project_list_id = list(zip(project_list, project_ids)))

@main.route('/editor/<project_id>')
@login_required
def editor(project_id):
    current_user.current_project = project_id
    project = firestore_db.collection(current_user.id).document(project_id).get().to_dict()
    return render_template('editor.html', project = project)

@main.route('/add_item/<item_type>')
@login_required
def add_item(item_type):
    # gives option to add a new item to the current project
    
    pass 



@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
