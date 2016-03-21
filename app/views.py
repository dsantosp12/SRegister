from flask import (Blueprint, render_template, g, redirect,
                   url_for, request, flash)

init = Blueprint('init', __name__)


@init.route('/')
def index():
    return "<h2>Hello world!</h2>"
