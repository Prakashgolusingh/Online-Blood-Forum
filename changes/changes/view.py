from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import *
view = Blueprint('view', __name__)

@view.route('/',methods=['GET','POST'])
def home():
      return render_template('home.html')


# Donor routes
@view.route('/donor_dashboard')
def donorDashboard():
      return render_template('donor_dashboard.html')

@view.route('/donote_blood',methods=['GET','POST'])
def donateBlood():
      return render_template('search_camp.html')


# Sankhanil

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


#Hosptal routes
@view.route('/hospital_dashboard',methods=['GET','POST'])
def hospitalDashboard():
      return render_template('hospital_dashboard.html')

@view.route('/create_camp',methods=['GET','POST'])
def createCamp():
      return render_template('create_camp.html')
'''
@app.route('/update_blood', methods=['GET', 'POST'])
def update_blood():
    form = BloodForm()

    if form.validate_on_submit():
        blood_group = form.blood_group.data
        available_units = form.available_units.data

        # Retrieve the hospital based on the user's session or however you're handling authentication
        hospital = Hospital.query.filter_by(id=session['hospital_id']).first()

        # Check if blood availability for this hospital and blood group already exists
        existing_blood = BloodAvailability.query.filter_by(hospital_id=hospital.id, blood_group=blood_group).first()

        if existing_blood:
            # Update the existing record
            existing_blood.available_units = available_units
        else:
            # Create a new record
            new_blood = BloodAvailability(hospital_id=hospital.id, blood_group=blood_group, available_units=available_units)
            db.session.add(new_blood)

        db.session.commit()
        return redirect(url_for('hospital_dashboard'))

    return render_template('available_blood.html', form=form)

'''













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
