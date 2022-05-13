from flask import Flask, render_template
from views import my_view

# initialises flask and the blueprint (template) to be used from views.py
app = Flask(__name__)
app.register_blueprint(my_view)

# how the website will handle 404 page cannot be found errors
# it does this by loading the 404.html designed error page instead of the 
# browser standard which will keep the users on the website with the navbar
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',e=e)

# to run the site with different settings than the default via running app.py
# compared to the usual flask run settings of debug=False and port=5000
if __name__ == '__main__':
    app.run(debug=True,port=8000)