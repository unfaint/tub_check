"""
Controller module for API
"""
from flask import make_response, abort
from .logger import log


@log
def check(**kwargs):
    if kwargs.get('image', False):
        print('Yes!')
        return make_response("Success!", 201)
    else:
        print('No!', kwargs)
        abort(406, 'I can\'t! Sorry!')
