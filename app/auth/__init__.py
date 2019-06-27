'''
Add a blueprint for user authorizing
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
