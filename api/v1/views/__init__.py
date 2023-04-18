from flask import Blueprint
import api.v1
from api.v1.views.index import *

app_views = Blueprint("/api/v1")
