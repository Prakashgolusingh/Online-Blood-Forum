from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import *
view = Blueprint('view', __name__)

@view.route('/',methods=['GET','POST'])
def home():
      search_form = True
      rows = None
      type = None
      if 'blood_group' in request.args and 'state' in request.args and 'district' in request.args:
            rows = blood_search(request.args['state'], request.args['district'], request.args['blood_group'])
            search_form = False
            type = request.args['blood_group']

      return render_template('user_blood_search.html', search_form = search_form, 
                        rows = rows, type = type)

      return render_template('home.html')


# Donor routes
@view.route('/donor_dashboard')
def donorDashboard():
      return render_template('donor_dashboard.html')

@view.route('/donote_blood',methods=['GET','POST'])
def donateBlood():
      return render_template('search_camp.html')


@view.route('/search_camps', methods = ['GET'])
def search_camps():
      donor_id = None
      if 'donor_email' in session:
            donor_id = session['donor_email']
      
      search_form = True
      rows = ""
      if 'state' in request.args and 'district' in request.args:
            rows = search_camps_backend(request.args['state'], request.args['district'], donor_id)
            search_form = False

      return render_template('search_camps.html', search_form = search_form, rows = rows)


@view.route('/register_camp', methods = ['GET', 'POST'])
def register_camp():
      if request.method == 'POST':
            donor_id = session['donor_email']
            hospital_id = request.form['hospital_id']
            camp_id = request.form['camp_id']

            register_into_camp(donor_id, hospital_id, camp_id)

      return redirect(url_for('view.search_camps'))


@view.route('/donor_awaited_camps')
def donor_awaited_camps():
      if 'donor_email' not in session:
            return redirect(url_for('auth.donor_login'))

      data = view_registered_upcoming_camps(session['donor_email'])[0]
      return render_template('donor_awaited_camps.html', data = data)


@view.route('/donor_accepted_camps')
def donor_accepted_camps():
      if 'donor_email' not in session:
            return redirect(url_for('auth.donor_login'))

      data = view_registered_upcoming_camps(session['donor_email'])[1]
      return render_template('donor_accepted_camps.html', data = data)


@view.route('/donor_rejected_camps')
def donor_rejected_camps():
      if 'donor_email' not in session:
            return redirect(url_for('auth.donor_login'))

      data = view_registered_upcoming_camps(session['donor_email'])[2]
      return render_template('donor_rejected_camps.html', data = data)


@view.route('/donor_past_camps')
def donor_past_camps():
      if 'donor_email' not in session:
            return redirect(url_for('auth.donor_login'))
      
      rows = get_donor_past_camps(session['donor_email'])
      return render_template('donor_past_camps.html', rows = rows)

@view.route('/user_blood_search', methods = ['GET'])
def user_blood_search():
      search_form = True
      rows = None
      type = None
      if 'blood_group' in request.args and 'state' in request.args and 'district' in request.args:
            rows = blood_search(request.args['state'], request.args['district'], request.args['blood_group'])
            search_form = False
            type = request.args['blood_group']

      return render_template('user_blood_search.html', search_form = search_form, 
                             rows = rows, type = type)



#Hosptal routes
@view.route('/hospital_dashboard',methods=['GET','POST'])
def hospitalDashboard():
      return render_template('hospital_dashboard.html')

@view.route('/create_camp',methods=['GET','POST'])
def createCamp():
      if request.method == 'POST':
            email = session['hospital_email']
            name = request.form.get('name')
            date = request.form.get('date')
            location = request.form.get('location')
            if location is None:
                  insert_camp(email, name, 'hospital', date)
            else:
                  insert_camp(email, name,location, date)
            flash('Camp created successfully', 'success')
            return redirect(url_for('view.hospitalDashboard'))
      return render_template('create_camp.html')

from flask import render_template

from flask import render_template, request

@view.route('/upcoming_camp')
def upcomingCamp():
      email = session['hospital_email']
      upcoming_camps=get_upcoming_camps(email)
      return render_template('upcoming_camp.html', camps=upcoming_camps)

@view.route('/delete_camp/<camp_id>')
def deleteCamp(camp_id):
      if session['hospital_email']:
            delete_camp(camp_id)
            delete_registered_camp(camp_id)
            flash('Deleted Camp Successfully', 'success')
            return render_template('hospital_dashboard.html')
      return render_template('home.html')

@view.route('/registered_donor/<camp_id>')
def registeredDonor(camp_id):
      if session['hospital_email']:
            donors = get_donors_by_camp(camp_id)
            block_values = [check_status(did[0], camp_id) for did in donors]
            print(donors)
            lenh = len(donors)
            print(lenh)
            return render_template('registered_donor.html',donors=donors,camp_id= camp_id, block_values = block_values, lenh = lenh)
      return render_template('home.html')

@view.route('/accept_donor/<donor_id>/<camp_id>')
def acceptDonor(donor_id, camp_id):
      block = False
      if session['hospital_email']:
            blood_group = get_blood_group(donor_id)
            unit = get_unit_blood(session['hospital_email'], blood_group)
            change_status(donor_id,camp_id)
            
            increase_available_blood(blood_group,unit+1,session['hospital_email'])
            flash('Accepted Blood From Donor Successfully','success')
            return redirect(url_for('view.registeredDonor', camp_id=camp_id))
      return "404"

@view.route('/reject_donor/<donor_id>/<camp_id>')
def rejectDonor(donor_id, camp_id):
      update_rejected_status(donor_id, camp_id)
      flash('Donor Rejected','success')
      return redirect(url_for('view.registeredDonor', camp_id=camp_id))

@view.route('/show_past_camp')
def showPastCamp():
      camp = get_past_camp(session['hospital_email'])
      print(session['hospital_email'])
      print(camp)
      return render_template('show_past_camp.html',camps=camp)















# route of admins
@view.route('/admin_dashboard')
def adminDashboard():
      donor_count = get_donors_count()[0]
      hospital_count = get_hospitals_count()[0]
      print(type(donor_count))
      return render_template('admin_dashboard.html',donor_count=donor_count, hospital_count=hospital_count)

@view.route('/donor_list')
def donorList():
    donors = get_all_donors()
    return render_template('donor_list.html', donors=donors)

@view.route('/hospital_list')
def hospitalList():
    hospitals = get_all_hospitals()
    return render_template('hospital_list.html', hospitals=hospitals)

@view.route('/delete_donor/<email>')
def deleteDonor(email):
      if delete_donor_by_email(email):
            flash('Successfully Deleted Donor', 'success')
      else:
            flash('There is an error in deletion of donor', 'error')
      return redirect(url_for('view.donorList'))

@view.route('/delete_hospital/<email>')
def deleteHospital(email):
      if delete_hospital_by_email(email):
            flash('Successfully deleted hospital', 'success')
      else:
            flash('There is an error in deletion', 'error')
      return redirect(url_for('view.hospitalList'))


