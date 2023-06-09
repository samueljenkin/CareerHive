from flask import Blueprint
from controllers.jobs_controller import index, new, create, edit, update, delete, save, apply, report, file, search, view, stored, remove, advanced

jobs_routes = Blueprint('jobs_routes', __name__)

jobs_routes.route('',)(index)
jobs_routes.route('/new')(new)
jobs_routes.route('', methods=["POST"])(create)
jobs_routes.route('/<id>/edit', methods=["POST"])(edit)
jobs_routes.route('/<id>', methods=["POST"])(update)
jobs_routes.route('/<id>/delete', methods=["POST"])(delete)
jobs_routes.route('/<id>/save', methods=["POST"])(save)
jobs_routes.route('/<id>/apply', methods=["POST"])(apply)
jobs_routes.route('/<id>/report')(report)
jobs_routes.route('/<id>/file', methods=["POST"])(file)
jobs_routes.route('/search', methods=["POST"])(search)
jobs_routes.route('/<id>/view')(view)
jobs_routes.route('/stored', methods=["POST"])(stored)
jobs_routes.route('/<id>/remove', methods=["POST"])(remove)
jobs_routes.route('/advanced', methods=["POST"])(advanced)