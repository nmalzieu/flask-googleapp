#!/usr/bin/env python
import sys

sys.path.append('/usr/local/google_appengine/')

from flaskBase import db
db = db.db
from flaskBase.models import *

db.create_all()
