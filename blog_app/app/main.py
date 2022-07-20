from matplotlib import blocking_input
from flask import Flask,  Blueprint, render_template
from flask_login import login_required, current_user
from . import firestore_db, db

main = Blueprint('main', __name__)
app = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/editor')
@login_required
def editor():
    return render_template('editor.html')


@main.route('/editor/add_item/<item_type>/<item_content>', methods=['POST'])
@login_required
def add_item(item_type):
    user_id = current_user.id
    current_users_all_blogs = [doc.id for doc in firestore_db.collection(u'user_id').stream()]

    if item_type == 'heading':
        pass
    if item_type == 'paragraph':
        pass
    if item_type == 'image':
        pass
    if item_type == 'poll':
        pass
    if item_type == 'question':
        pass

@main.route('/editor/remove_item/<item_id>')
@login_required
def remove_item(item_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
