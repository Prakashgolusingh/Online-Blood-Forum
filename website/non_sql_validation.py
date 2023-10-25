

def is_valid_donor_signup(email, name, age, gender, state, district, blood_group, contact, password, confirmPassword):
      if(len(email)<10):
            return 'invalid email id', False
      elif(len(name)<1):
            return 'Name is too short', False
      elif(len(age)<1):
            return 'Invalid age', False
      elif(int(age)<18):
            return ' your age is less than 18' , False
      elif(int(age)>80):
            return 'Your age is greater than 80 ', False
      elif(len(gender)<1):
            return 'Choose Valid Gender', False
      elif(len(state)<1):
            return 'Choose Valid State ', False
      elif(len(district)<1):
            return 'Choose valid District ', False
      elif(len(blood_group)<1):
            return 'Choose Valid Blood Group ', False
      elif(len(contact)<10):
            return 'Enter Valid Mobile Number ', False
      elif(password != confirmPassword):
            return 'Password Is Not Matching ', False
      else:
            return 'Form is Valid', True

def is_valid_hospital_signup(email, name, license_no, state, district, contact, password, confirmPassword):
      if(len(email)<10):
            return 'invalid email id', False
      elif(len(name)<1):
            return 'Name is too short', False
      elif(len(license_no)<1):
            return 'Enter Valid License Number', False
      elif(len(state)<1):
            return 'Choose Valid State ', False
      elif(len(district)<1):
            return 'Choose valid District ', False
      elif(len(contact)<10):
            return 'Enter Valid Mobile Number ', False
      elif(password != confirmPassword):
            return 'Password Is Not Matching ', False
      else:
            return 'Form is Valid', True