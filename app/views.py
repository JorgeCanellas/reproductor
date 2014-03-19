from app import app


@app.route('/')
@app.route('/index')
def index():
    """


    :return:
    """
    return "Hello, World!"

@app.route('/importFilm')
def importFilm():

    return "Import films page here"

