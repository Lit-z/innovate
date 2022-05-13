from flask import render_template, redirect, url_for, Blueprint

# creates the blueprint
my_view = Blueprint('my_view',__name__)

# setting up the url's of each page, page 5 at the bottm is used to show
# future expandability
@my_view.route('/')
def home():
    return render_template('home.html')

@my_view.route('/admin')
def admin():
    return render_template('admin.html')

@my_view.route('/page1')
def page1():
    return render_template('page1.html')

@my_view.route('/page2')
def page2():
    return render_template('page2.html')

@my_view.route('/page3')
def page3():
    return render_template('page3.html')

@my_view.route('/page4')
def page4():
    return render_template('page4.html')

# /js, etc as listed below will redirect to home.html which 
# is the same as url '/' as listed in the above route setting
@my_view.route('/js')
@my_view.route('/javascript')
@my_view.route('/home')
def js_redirect():
    return redirect(url_for('my_view.home'))

# for this, '/activities' sets the url name, only here and the navbar need to be 
# changed to affect what the user sees as links or in the address bar
# rather than needing to rename every reference to page5
@my_view.route('/activites')
def page5():
    return render_template('page5.html')

# this would be an optional extra if then wanted /page5 to also redirect to 
# the new activities page
@my_view.route('/page5')
def p5_redirect():
    return redirect(url_for('my_view.page5'))