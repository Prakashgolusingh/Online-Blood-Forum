# Online-Blood-Forum
The Online Blood Forum Project is a pioneering initiative driven by the vision to bridge 
the gap between blood donors and those in need within our community.

About the project  - We have Four type of user for this application

## Normal User-
1. who are looking for blood in there district, they don't need to sign up or sign in they can directly search for hospital
2. Based on state, district and blood group all registered hospital in that district get listed on screen,
3.  with number unit of blood available for searched group, name, address and contact number.
   
## ● Hospitals - 
1. Hospitals need to register first based on name(include their address with name), state, district, contact number, license number, etc.
2. They can update their profile through hospital dashboard
3. They can update manually number of unit blood available for each type of blood group.
4. They can organize camps (one hospital can create multiple camps)
by filling a form with some information about camp like date, place, etc.

5. Hospital can view the list of registered donors in camp with donors details.
6. Hospitals have choise to accept/reject registered donors
7. if reject donors delted from list and can't register again in that camp.
8. If accepted, 1 unit of blood will increase in that hospital available blood bank of same blood group that of donor.
9. They can view history of organized blood camp with their registered donors.

## ● Donors - 
1. Donors can create their account base name, state, district, contact number, etc.
2. They can also search for blood in nearby hospitals.
3. They can register in blood donation camp if they are eligible(like they have not registered in any camp in last 4 months).
4. They can update their profile's basic information.  

## ● Admin– 
1. Admin can't register by itself, but only by developers.
2. Admin can view donors and hospitals. 
3. Admin can delete account of any donor or hospital.
4. Admin manage user/donors as well as hospitals based on license 
number. Admin can delete account of any donors or hospitals if it finds any thing suspicious.

## About techology and application
1. create using flask and sqlite (sqlite is provided by flask itself).
2. Total 6 table are their in this application.
3. GUI are not much fancy, it is simple and mostly bootstrap are used.
