from flask import Blueprint
user_bp = Blueprint('stu', __name__)
@user_bp.route('/index')
def index():
    return 'first user_bp'