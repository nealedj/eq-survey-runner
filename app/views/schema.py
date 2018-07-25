from flask import Blueprint, jsonify
from app.utilities.schema import load_schema_from_params

schema_blueprint = Blueprint('schema', __name__)


@schema_blueprint.route('/schema/<eq_id>/<form_type>', methods=['GET'])
def get_schema_json(eq_id, form_type):
    schema = load_schema_from_params(eq_id, form_type)

    return jsonify(schema.json)
