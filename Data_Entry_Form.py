import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic (CAR)", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia (FYROM)", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka"]
root = tkinter.Tk()
root.title("Hotel Management")
# baground color
root.configure(bg='#00E0CF')
# logo
logo = PhotoImage(file="download.png")
root.iconphoto(False, logo)

frame = tkinter.Frame(root)
frame.pack()

#function
def enter_data():
    # frame 1
    first_name = first_name_entery.get()
    last_name = last_name_entery.get()
    titlecmbobox = title_combobox.get()
    agespin = age_spinbox.get()
    nationalitycombo = nationality_combobox.get()

    # frame 2
    numcourse = numcourses_spinbox.get()
    numsemister = numsemister_spinbox.get()
    registered_ststus = reg_status_var.get()
    terms = terms_var.get()
    print(f"The first name is {first_name}, and the last name is {last_name}.\nThe chosen title is {titlecmbobox}, and the age is {agespin}, with the nationality being {nationalitycombo}.\n The number of courses is {numcourse}, and the number of semesters is {numsemister}.\n The registered status is {registered_ststus}    ")
    print("-------------------------------------------------------------------------------")




# User info
# frame 1 - "user_info_frame"
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=10, pady=5)

# 1st name - frame 1
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

# Entry data for 1st name - frame 1
first_name_entery = Entry(user_info_frame)
first_name_entery.grid(row=1, column=0, padx=10, pady=5)

#last name - frame 1
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# Entry data for last name - frame 1
last_name_entery = Entry(user_info_frame)
last_name_entery.grid(row=1, column=1, padx=10, pady=5)

# chose mr. or mrs. we call title - frame 1
title_lable = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values= ["", "Mr.", "Mrs.", "Dr."])
title_lable.grid(row=0, column=2)
# comobobox
title_combobox.grid(row=1, column=2, padx=10, pady=5)

# age - using spin box - frame 1
age_lable = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=50)
age_lable.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0, padx=10, pady=5)

# nationality - comobobox - frame 1
nationality_lable = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=countries)
nationality_lable.grid(row=2, column=1, padx=10, pady=5)
nationality_combobox.grid(row=3, column=1, padx=10, pady=5)

# Register data
# frame 2 - "courses_frame"
courses_frame = tkinter.LabelFrame(frame, text="Fill the data")
courses_frame.grid(row=1, column=0, sticky="news", padx=10, pady=5)
# data -- in frame2 # we are unable to use .get function directly in checkbutio we need to converst take var(stringvar)
registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar()
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable= reg_status_var, onvalue="Registered",
                                       offvalue="Not registered")

registered_label.grid(row=0, column=0, padx=10, pady=5)
registered_check.grid(row=1, column=0, padx=10, pady=5)

# courses data - frame2
numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1, padx=10, pady=5)
numcourses_spinbox.grid(row=1, column=1, padx=10, pady=5)

# semister - frame2
numsemister_lable = tkinter.Label(courses_frame, text="Semester")
numsemister_spinbox = tkinter.Spinbox(courses_frame, from_= 0, to="infinity")
numsemister_lable.grid(row=0, column=2, padx=10, pady=5)
numsemister_spinbox.grid(row=1, column=2, padx=10, pady=5)

# frame - 3 accepts
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_var = tkinter.StringVar()
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=terms_var,
                                  onvalue="acception terms and conditions", offvalue="not acception terms and conditions")
terms_check.grid(row=0,column=0, padx=20, pady=20)


#button
button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)



























root.mainloop()
