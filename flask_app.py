"""
Service designed for detecting tuberculosis on medical images
"""

from flask import render_template
import connexion
from logger import log

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


@app.route('/')
@log
def home():
    """
    Responds to root URL

    :return: rendered template 'home.html', containing submission web form
    """
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5050, debug=True)
