from flask import Flask,  Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)
app = Flask(__name__)
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    
if __name__ == '__main__':
    app.run(debug=True)