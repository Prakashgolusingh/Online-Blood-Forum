from flask import Blueprint, render_template, request, flash,redirect,url_for
from flask import session
from .non_sql_validation import *
from .sql_validation import *
from .models import *
auth = Blueprint('auth', __name__)

# all authentication route
@auth.route('/donor_signup',methods=['GET','POST'])
def donorSignup():
      if request.method == 'POST':
            email = request.form.get('email')
            name = request.form.get('name')
            age = request.form.get('age')  # Assuming age is an integer
            gender = request.form.get('gender')
            state = request.form.get('state')
            district = request.form.get('district')
            blood_group = request.form.get('blood_group')
            contact = request.form.get('contact')
            password = request.form.get('password1')
            confirmPassword = request.form.get('password2')
            # Now check form entries are valid or not
            message, check = is_valid_donor_signup(email, name, age, gender, state, district, blood_group, contact, password, confirmPassword)
            if check:
                  if is_donor_exist(email):
                        flash('Donor already exit, please login!', category='error')
                        return redirect(url_for('auth.donorLogin'))
                  else:
                        flash('Registered Successfully', 'success')
                        insert_donor(email, name, age, gender, state, district, blood_group, contact, password)
                        return redirect(url_for('auth.donorLogin'))
            else:
                  flash(message,'error')
                  return redirect(url_for('auth.donorSignup'))
      return render_template('donor_signup.html')

@auth.route('/donor_login',methods=['GET','POST'])
def donorLogin():
      if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            if is_donor_exist(email):
                  if check_donor_password(email,password):
                        donor = get_donor_by_email(email)
                        flash('Logged in successfully', category='success')
                        session['donor_email'] = email
                        return redirect(url_for('view.donorDashboard'))
                  else:
                        flash('Incorrect password, try again', category='error')
                        return redirect(url_for('donorLogin'))
            else:
                  flash('Email does not exist.', category='error')
                  return redirect(url_for('auth.donorSignup'))
      return render_template('donor_login.html')



@auth.route('/hospital_signup',methods=['GET','POST'])
def hospitalSignup():
      if request.method=='POST':
            email = request.form.get('email')
            name = request.form.get('name')
            license_no = request.form.get('licenseNo')
            district = request.form.get('district')
            state = request.form.get('state')
            contact = request.form.get('contact')
            password = request.form.get('password1')
            confirmPassword = request.form.get('password2')
            message, check = is_valid_hospital_signup(email, name, license_no, district, state, contact, password, confirmPassword)
            if check:
                  if is_hospital_exist(email):
                        flash('Hospital already exit, please login!', category='error')
                        return redirect(url_for('auth.hospitalLogin'))
                  else:
                        insert_hospital(email, name, license_no, state, district, contact, password)
                        flash('Registered Successfully', 'success')
                        return redirect(url_for('auth.hospitalLogin'))
            else:
                  flash(message,'error')
                  return redirect(url_for('auth.hospitalSignup'))
      return render_template('hospital_signup.html')

@auth.route('/hospital_login',methods=['GET','POST'])
def hospitalLogin():
      if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            if is_hospital_exist(email):
                  if check_hospital_password(email,password):
                        flash('Logged in successfully', category='success')
                        session['hospital_email']=email
                        return redirect(url_for('view.hospitalDashboard'))
                  else:
                        flash('Incorrect password, try again', category='error')
                        return redirect(url_for('auth.hospitalLogin'))
            else:
                  flash('Email does not exist.', category='error')
                  return redirect(url_for('auth.hospitalSignup'))
      return render_template('hospital_login.html')

@auth.route('/edit_hospital', methods=['GET', 'POST'])
def edit_hospital_profile():
      email = session.get('hospital_email')  # Get the email from the session
      if not email:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('auth.hospitalLogin'))
      if request.method == 'POST':
            
            # Update the hospital's profile based on the form data.
            name = request.form.get('name')
            contact = request.form.get('contact')
            password = request.form.get('password')

            # Update the hospital's profile in the database.
            update_hospital_profile(email, name, password, contact)
            flash('Your profile has been updated successfully', 'success')
            return redirect(url_for('view.hospitalDashboard'))
      hospital = get_hospital_by_email(email)
      return render_template('edit_hospital.html',hospital=hospital)

@auth.route('/available_blood', methods=['GET', 'POST'])
def availableBlood():
      email = session.get('hospital_email')  # Get the email from the session
      if not email:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('auth.hospitalLogin'))
      if request.method == 'POST':
            
            # Update the hospital's blood based on the form data.
            O_positive = request.form.get('O_positive')
            O_negative = request.form.get('O_negative')
            A_positive = request.form.get('A_positive')
            A_negative = request.form.get('A_negative')
            B_positive = request.form.get('B_positive')
            B_negative = request.form.get('B_negative')
            AB_positive = request.form.get('AB_positive')
            AB_negative = request.form.get('AB_negative')

            # Update the hospital's profile in the database.
            update_hospital_blood(email,O_positive, O_negative, A_positive, A_negative,B_positive,B_negative,AB_positive,AB_negative)
            flash('hospital blood has been updated successfully', 'success')
            return redirect(url_for('view.hospitalDashboard'))
      hospital = get_blood_by_email(email)
      print(hospital)
      return render_template('available_blood.html',hospital=hospital[0])

@auth.route('/admin_login',methods=['GET','POST'])
def adminLogin():
      if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            if is_admin_exist(email):
                  if check_admin_password(email,password):
                        session['admin_email']=email
                        flash('Logged in successfully', category='success')
                        return redirect(url_for('view.adminDashboard'))
                  else:
                        flash('Incorrect password, try again', category='error')
                        return redirect(url_for('auth.adminLogin'))
            else:
                  flash('Email does not exist.', category='error')
                  return redirect(url_for('auth.adminLogin'))
      return render_template('admin_login.html')

@auth.route('/logout')
def Logout():
      if not session:
            flash('Not Logged in', 'error')
            return redirect(url_for('view.home'))
      else:
            session.clear()
            flash('Logged out successfully', category='success')
            return render_template('home.html')