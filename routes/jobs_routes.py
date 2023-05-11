from flask import Blueprint
from controllers.jobs_controller import index

jobs_routes = Blueprint('jobs_routes', __name__)

jobs_routes.route('')(index)