from flask import render_template
from flask.ext.login import login_required

from app import app


#--------------------------------------------------------------------------------------------------------
# INDEX: Main page of the monkey already connected
#--------------------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/index')
@app.route('/importfilm')
#@login_required
def index():
    return "Mundooo bonitoooo"  # , user=user, monkeys_list=monkeys_list)

