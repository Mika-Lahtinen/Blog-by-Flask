from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404_Page_not_Found.html'), 404


@main.app_errorhandler(500)
def internal_server_error(error):
    return render_template('500_Internal_Server_Error.html'), 500
