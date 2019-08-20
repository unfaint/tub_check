"""
Simple performance logging module.
To use it, import and @log decorator
just before a function needed to watch.

Example (FLASK application):
    @app.route('/')
    @log
    def home():
        return render_template('home.html')
"""

import logging
from time import time

logger = logging.getLogger('performance')
logger.setLevel(logging.DEBUG)

ch = logging.FileHandler('./logs/performance.log')
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)


def log(fn):
    def fn_log(*args, **kwargs):
        time1 = time()
        name = fn.__name__
        result = fn(*args, **kwargs)
        logger.debug('{} - {} ms'.format(name, time() - time1))
        return result

    return fn_log
