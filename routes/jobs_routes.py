from flask import Blueprint
from controllers.jobs_controller import index, new, create, edit, update, delete, save

jobs_routes = Blueprint('jobs_routes', __name__)

jobs_routes.route('')(index)
jobs_routes.route('/new')(new)
jobs_routes.route('', methods=["POST"])(create)
jobs_routes.route('/<id>/edit')(edit)
jobs_routes.route('/<id>', methods=["POST"])(update)
jobs_routes.route('/<id>/delete', methods=["POST"])(delete)
jobs_routes.route('/<id>/save', methods=["POST"])(save)