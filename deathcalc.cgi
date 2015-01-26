from wsgiref.handlers import CGIHandler
from deathcalc import app.py
CGIHandler().run(app)