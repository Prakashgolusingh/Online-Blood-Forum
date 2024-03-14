# Online-Blood-Forum
This project is a part of Semester-5 DBMS lab.

The Online Blood Forum Project is a pioneering initiative driven by the vision to bridge 
the gap between blood donors and those in need of it by connecting them to the hospitals in their area.

About the project  - We have Four type of user for this application

## Normal User-
1. who are looking for blood in thier district, they don't need to sign up or sign in they can directly search for hospital
2. Based on state, district and blood group all registered hospital in that district get listed on screen,
3.  with number unit of blood available for searched blood group, name, address and contact number, etc about the all the hospitals in that district.
   
## ● Hospitals - 
1. Hospitals need to register first based on name(include their address in name), state, district, contact number, license number, etc.
2. They can update their profile through hospital dashboard
3. They can update manually number of unit blood available for each type of blood group any time,
4. there is a another way also to update no. of units automatically through blood camps.
5. hospitals can organize camps (one hospital can create multiple camps)
by filling a form with some information about camp like date, place, etc.

6. Hospital can view the list of registered donors in camp with donors details.
7. Hospitals have choise to accept/reject registered donors
8. if reject donors deleted from list and can't register again in that camp.
9. If accepted, 1 unit of blood will increase in that hospital available blood bank of same blood group that of donor.
10. They can view history of organized blood camp with their registered donors.

## ● Donors - 
1. Donors can create their account base name, state, district, contact number, etc.
2. They can also search for blood in nearby hospitals.
3. They can register in blood donation camp if they are eligible(like they have not registered in any camp in last 4 months).
4. They can update their profile's basic information.
5. They can check if donor already applied for any camp and it's not accepted/reject till now.
6. They can see all past camps in which donor participated with status of accepted or rejected in that camp.

## ● Admin– 
1. Admin can't register by itself, but only by developers.
2. Admin can view donors and hospitals. 
3. Admin can delete account of any donor or hospital.
4. Admin manage user/donors as well as hospitals based on license 
number. Admin can delete account of any donors or hospitals if it finds any thing suspicious.

## About techology and application
1. created using flask and sqlite (sqlite is provided by flask itself) so no need to add any other database until you don't want to use sqlite.
2. Total 6 table are their in this application.
3. GUI are not much fancy, it is simple and mostly bootstrap are used, since the main aim to work on backend.

## Note-
1. This is my 3rd project in flask and the best one till date. But i personlly love this project cause i learned alot while working on it.
2.  learning new technology or working on product which can be used by people gives us different felling.
3.  Not copied from somewhere.

# Search Blood
![Screenshot 2024-03-14 201208](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/c0d511d8-107c-4573-a8df-65143c30adc9)

# Hospital Login
![Screenshot 2024-03-14 193016](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/d0a9ea9a-7f7a-4d34-a2ff-2471f67c0e52)
# Hospital SignUp
![Screenshot 2024-03-14 193046](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/5e518309-10b7-439f-8a03-cab25e586b97)
# Hospital Landing Page
![Screenshot 2024-03-14 193224](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/0e32ec09-0368-45b7-83c3-d949c56627e4)
# Check and update Available Blood
![Screenshot 2024-03-14 193329](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/4b796813-138e-49a6-aac1-8473f6fba966)
# Create New Camp
![Screenshot 2024-03-14 200839](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/1617e24e-2290-4e69-a85e-175af0f9830c)

# Donor Login
![Screenshot 2024-03-14 192842](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/206d2e58-d4db-4fef-80a4-ddcf575ecede)
# Donor SignUp
![Screenshot 2024-03-14 192948](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/7f009a19-d8cb-4a42-97af-b4c08848d047)
# Search Camp
![Screenshot 2024-03-14 193506](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/f067af9a-2d18-4b75-a85b-140bb50ddfc9)
# Past Applied Camps
![Screenshot 2024-03-14 193552](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/f1d5e938-53d7-4593-9b0d-4107cbabb2e0)
# Awaited Camp Registration
![Screenshot 2024-03-14 193619](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/bf098b92-9493-4b34-b645-b82ca28762a9)
# Admin Login 
![Screenshot 2024-03-14 192813](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/62c15b43-3793-434c-9063-d4d4a332dcdc)
# Admin Dashboard
![Screenshot 2024-03-14 193706](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/48445942-1554-49bb-a524-dd3dc8e7b721)
# List Of Hospitals
![Screenshot 2024-03-14 193724](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/dc9ca73a-d4f6-4c0c-b757-59e718c2c82c)
# List Of Donors
![Screenshot 2024-03-14 193739](https://github.com/Prakashgolusingh/Online-Blood-Forum/assets/95623466/f76dffe3-0cc0-440d-9e19-a20fc8e474e5)



