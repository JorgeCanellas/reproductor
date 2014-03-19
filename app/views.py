from flask import render_template
from flask.ext.login import login_required

from app import app



#--------------------------------------------------------------------------------------------------------
# INDEX: Main page of the monkey already connected
#--------------------------------------------------------------------------------------------------------

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', user=user, monkeys_list=monkeys_list)


