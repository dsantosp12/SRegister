from flask import Blueprint
from .building import BuildingController

buildings = Blueprint('buildings', __name__)