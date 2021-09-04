# library imports
from flask_restplus import Resource, fields

# module imports
from app import api, transport_agent


transport_agent = api.model("transport_agent", {
    "first_name" : fields.String(required=True, description="first_name"),
    "last_name" : fields.String(required=True, description="last_name"),
    "id_number" : fields.String(required=True, description="id_number"),
    "email" : fields.String(required=False, description="email"),
    "role" : fields.String(required=False, description="role"),
    'feeding_amount': fields.List(fields.Raw(), description="feeding_amount")
    })


profile = api.model("profile", {
    "id_number" : fields.String(required=True, description="id_number")
    })

