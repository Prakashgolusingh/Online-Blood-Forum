# Flask is class of creating application
from flask import Flask
from .models import *
from .sql_validation import *
from .non_sql_validation import *
def create_app():
      app = Flask(__name__)  #creating object of our application, Flask is application class
      # app is object.
      app.config['SECRET_KEY'] = 'weiohreihgsdkfnsxklfjweroifdjneiothr3ilf'
      init_db()
      from .view import view # importing blueprint variable from view.py file
      from .auth import auth
      # we use blueprint to define route of similar type in one module.
      app.register_blueprint(view, url_prifix='/') #registering blueprint with app.
      # url_prifix is use to add prefix in address of the endpoint of all route in that file.
      app.register_blueprint(auth)
      # we don't need to use '/' cause it is default value, so we can remove url_prefix.
      return app  