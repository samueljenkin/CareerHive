from flask import Blueprint
from controllers.sessions_controller import new, create, delete

sessions_routes = Blueprint('sessions_routes', __name__)

sessions_routes.route('/new')(new)
sessions_routes.route('', methods=["POST"])(create)
sessions_routes.route('/delete', methods=["POST"])(delete)