import flask
from flask.ext import restful

from flaskBase import app
from flaskBase.db import db
from flaskBase.decorators import login_required

from flaskBase.models import SampleModel, serial_from

API = restful.Api(app)


class SampleRessource(restful.Resource):

    #@login_required
    def get(self):
        sm = SampleModel.query.first()
        return {'sample_model': serial_from(sm)}, 200

API.add_resource(SampleRessource, '/api/sample/')
