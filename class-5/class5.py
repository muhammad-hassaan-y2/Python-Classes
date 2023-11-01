data_base : list[tuple[str, str]] = [("Sir Qasim", "123"),
                                     ("Sir Zia", "234"),
                                     ("Sir Usman", "345")
                                     ]

input_user : str = input("Enter User Name: ")
input_password : str = input("Enter Password: ")
print("Your data: " + input_user + " \t" + input_password)


for row in data_base:
                     user, password = row 
                     if input_user == user and input_password == password:
                       print(f"Valid User {user.title()}")
                       
                       break  
else:
     print("Not found || Invalid User")