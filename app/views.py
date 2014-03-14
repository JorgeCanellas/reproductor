from flask import render_template, flash, redirect, request, jsonify
from sqlalchemy import exc
from app import app, db
from forms import *
from models import Films



#--------------------------------------------------------------------------------------------------------
# INDEX: Main page of the monkey already connected
#--------------------------------------------------------------------------------------------------------

@app.route ('/')
@app.route ('/index')
@login_required
def index ():
	


	return render_template ('index.html', user=user, monkeys_list=monkeys_list)


"""

#--------------------------------------------------------------------------------------------------------
# LOAD_USER: This callback is used to reload the user object from the user ID stored in the session
#--------------------------------------------------------------------------------------------------------

@login_manager.user_loader
def load_user(id):
	return Monkey.query.get(int(id))



#--------------------------------------------------------------------------------------------------------
# NEW_USER: Add a new user through the form SignUp. Just available in the login.html template
#--------------------------------------------------------------------------------------------------------

@app.route ('/new_user', methods = ['GET','POST'])
def new_user():

	sigInForm = SigninForm()
	logInForm = LoginForm()

	if sigInForm.validate_on_submit():

		newMonkey = Monkey( username = sigInForm.usernameSigin.data, email = sigInForm.emailSigin.data, password = sigInForm.passwordSigin.data)

		if newMonkey is not None :
			db.session.add(newMonkey)
			
			try:
				db.session.commit()
				login_user(newMonkey)
				return redirect ('/index')

			except exc.SQLAlchemyError:
				return redirect ('/login')

	return render_template ('login.html', logInForm = logInForm, sigInForm = sigInForm)
	

#--------------------------------------------------------------------------------------------------------
# LOGIN: Login with the login form once the user is already registered in the service
#--------------------------------------------------------------------------------------------------------

@app.route ('/login', methods = ['GET','POST'])
def login ():

	sigInForm = SigninForm()
	logInForm = LoginForm()

	if logInForm.validate_on_submit():

		try:
			monkey = db.session.query(Monkey).filter_by(email=logInForm.emailLogin.data).first()
			if monkey.password == logInForm.passwordLogin.data :
				login_user(monkey)
				return redirect ('/index')
		except:
			return redirect ('/login')

	return render_template ('login.html', logInForm = logInForm, sigInForm = sigInForm)


#--------------------------------------------------------------------------------------------------------
# LOGOUT: Logout from the service
#--------------------------------------------------------------------------------------------------------

@app.route ('/logout')
@login_required
def logout ():
	logout_user()
	return redirect('/login')


#--------------------------------------------------------------------------------------------------------
# ADD_FRIEND: Add monkey as a friend
#--------------------------------------------------------------------------------------------------------

@app.route ('/add_friend')
def add_friend():
	idMonkey = request.args.get('idMonkey', 'fail')
	new_friend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.new_friend(new_friend):
		db.session.commit()
		return jsonify(username = new_friend.username, res = 'True' )
	else:
		return jsonify(username = new_friend.username, res = 'False' )


#--------------------------------------------------------------------------------------------------------
# ADD_UNFRIEND: Add monkey as a unfriend 
#--------------------------------------------------------------------------------------------------------

@app.route ('/add_unfriend')
def add_unfriend():
	idMonkey = request.args.get('idMonkey', 'fail')
	new_unfriend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.new_unfriend(new_unfriend):
		db.session.commit()
		return jsonify(username = new_unfriend.username, res = 'True' )
	else:
		return jsonify(username = new_unfriend.username, res = 'False' )


#--------------------------------------------------------------------------------------------------------
# ADD_BESTFRIEND: Add monkey as a bestfriend. Check if you have already one bestfriend
#--------------------------------------------------------------------------------------------------------

@app.route ('/add_bestfriend')
def add_bestfriend():
	idMonkey = request.args.get('idMonkey', 'fail')
	new_bestfriend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.new_bestfriend(new_bestfriend):
		db.session.commit()
		return jsonify(username = new_bestfriend.username, res = 'True' )
	else:
		return jsonify(username = new_bestfriend.username, res = 'False' )


#--------------------------------------------------------------------------------------------------------
# DEL_FRIEND: Delete monkey as a friend 
#--------------------------------------------------------------------------------------------------------

@app.route ('/del_friend')
def del_friend():
	idMonkey = request.args.get('idMonkey', 'fail')
	del_friend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.rem_friend(del_friend):
		db.session.commit()
		return jsonify(username = del_friend.username, res = 'True' )
	else:
		return jsonify(username = del_friend.username, res = 'False' )


#--------------------------------------------------------------------------------------------------------
# DEL_UNFRIEND: Delete monkey as a unfriend 
#--------------------------------------------------------------------------------------------------------

@app.route ('/del_unfriend')
def del_unfriend():
	idMonkey = request.args.get('idMonkey', 'fail')
	del_unfriend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.rem_unfriend(del_unfriend):
		db.session.commit()
		return jsonify(username = del_unfriend.username, res = 'True' )
	else:
		return jsonify(username = del_unfriend.username, res = 'False' )


#--------------------------------------------------------------------------------------------------------
# DEL_BESTFRIEND: Delete monkey as a bestfriend 
#--------------------------------------------------------------------------------------------------------

@app.route ('/del_bestfriend')
def del_bestfriend():
	idMonkey = request.args.get('idMonkey', 'fail')
	del_bestfriend = db.session.query(Monkey).filter_by(id=idMonkey).first()
	if current_user.rem_bestfriend(del_bestfriend):
		db.session.commit()
		return jsonify(username = del_bestfriend.username, res = 'True' )
	else:
		return jsonify(username = del_friend.username, res = 'False' )




##############################################################################################################
##############################################################################################################
##############################################################################################################
#    TEST
##############################################################################################################
##############################################################################################################
##############################################################################################################


@app.route ('/test_users')
def test_users():
	
	newMonkey1 = Monkey( username = "alvaro1990", email = "alvaro@gmail.com", password = "alvaro")
	newMonkey2 = Monkey( username = "bruno1989", email = "bruno@gmail.com", password = "bruno")
	newMonkey3 = Monkey( username = "andrea1989", email = "andrea@gmail.com", password = "andrea")
	newMonkey4 = Monkey( username = "sergio1989", email = "sergio@gmail.com", password = "sergio")
	newMonkey5 = Monkey( username = "alberto1990", email = "alberto@gmail.com", password = "alberto")
	newMonkey6 = Monkey( username = "marta1978", email = "marta@gmail.com", password = "marta")
	newMonkey7 = Monkey( username = "ana1990", email = "ana@gmail.com", password = "ana")
	newMonkey8 = Monkey( username = "paco1988", email = "paco@gmail.com", password = "paco")
	newMonkey9 = Monkey( username = "luis1990", email = "luis@gmail.com", password = "luis")

	db.session.add(newMonkey1)
	db.session.add(newMonkey2)
	db.session.add(newMonkey3)
	db.session.add(newMonkey4)
	db.session.add(newMonkey5)
	db.session.add(newMonkey6)
	db.session.add(newMonkey7)
	db.session.add(newMonkey8)
	db.session.add(newMonkey9)

	db.session.commit()

	return redirect('/login')



"""