#NG LUM THYN
#TP061914

import random #imports random into code (used at line 248)

#Main Menu and Login Interfaces
#Main Menu
def mainmenu():
    flag = 0
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        print("\nWelcome to REAL CHAMPIONS SPORT ACADEMY SYSTEM (RCSAS)!")
        ask = int(input("Choose to login as Admin(0), Student(1) or terminate session(2): "))    
        if ask == 0:
            adminlogin()#to admin login interface (username: admin; password: admin)
        elif ask == 1:
            while True:#initialise loop structure to repeat if inputs are incorrect
                ask1 = int(input("Are you a Registered Student (0 for yes, 1 for no)? "))
                if ask1 == 0:
                    rstudentlogin()#to registered student login interface (username: student; password: student)
                    break
                if ask1 == 1:
                    studentmenu()#to student menu interface
                    break
                else:
                    print("Invalid input. Please try again.")
        elif ask == 2:
            flag = 1 #returns flag value as 1, terminates the session
            break#breaks out of the final loop
        else:
            print("Invalid input. Please try again")

#Admin Login
def adminlogin(): #(username: admin; password: admin)
    print("\nPlease login to access system.")
    while True: #initialise loop structure to repeat if inputs are incorrect
        name = str(input("Username: "))
        pswd = str(input("Password: "))
        if name == "admin" and pswd == "admin": #only continue if both name and pswd are correct
            print("Login Successful!")
            adminmenu()#to the admin menu interface
            break
        else: 
            print("Username or password incorrect, please try again.")

#Registered Student Login
def rstudentlogin(): #(username: StudentName; password: StudentID)
    print("\nPlease login to access system.")

    studname = [] #create list for storing student name
    studid = [] #create list for storing student ID

    f = open("Registered_Students_Records.txt", "r") #open text file containing registered student records, mode read
    for line in f: #iterate through the lines
        studid.append(line.split(",")[0]) #add first column to list
        studname.append(line.split(",")[1]) #add second column to list
    f.close()

    trylogin = True #used for validation below
    flag = 0 
    while flag == 0:
        name = str(input("Username: "))
        pswd = str(input("Your Student ID: "))

        #checking for matching data in studname
        for i in studname:
            if name == i:
                index1 = studname.index(i) #retrieve index of matching data in list
                trylogin = True 
                break
            else:
                trylogin = False
                continue #continue iterating through loop

        #checking for matching data in studid
        for j in studid:
            if pswd == j:
                index2 = studid.index(j) #retrieve index of matching data in list
                trylogin = True
                break
            else:
                trylogin = False
                continue #continue iterating through loop

        #login validation
        while trylogin == True: 
            if name == studname[index1] and pswd == studid[index2]: #compares input to data in lists
                print("Login Successful!")
                flag = 1
                rstudentmenu() #to registered student menu interface
                break

        while trylogin == False:
            print("Username or StudentID incorrect. Please try again.")
            break

#Student Menu
def studentmenu():
    flag = 0
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        print("\nWELCOME, STUDENT.")
        print("1. View details of Sport\n2. View details of Sport Schedule\n3. Register to Access Other Details\n4. Exit")
        action = int(input("Please choose an action (Enter numbers 1-4):"))
        if action == 1:
            showsportrec()#to sport records 
        elif action == 2:
            showschedulerec()#to sport schedule records 
        elif action == 3:
            addregstudrec()#to registered student records
        elif action == 4:
            flag = 1 #returns flag value as 1, breaks the loop
        else:
            print("Invalid input. Please enter numbers 1-4 only.")

#Registered Student Menu 
def rstudentmenu():
    flag = 0
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        print("\nWELCOME, REGISTERED STUDENT!")
        print("1. View Coach Record\n2. View Self Record\n3. View Registered Sports Schedule\n4. Modify Self Record\n5. Provide Feedback and Rating to Coach\n6. Exit")
        action = int(input("Please choose an action (Enter numbers 1-6):"))
        if action == 1:
            showcoachrec()#to coach records
        elif action == 2:
            showselfrec()#to self record interface
        elif action == 3:
            showregschedulerec()#to registed schedule records
        elif action == 4:
            modselfrec()#to self record modification interface
        elif action == 5:
            feedback()#to feedback interface
        elif action == 6:
            flag = 1 #returns flag value as 1, breaks the loop
            break #breaks out of the final loop
        else:
            print("Invalid input. Please enter numbers 1-6 only.")

#Admin Menu    
def adminmenu():
    flag = 0
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        print("\nWELCOME, ADMIN!")
        print("1. Add Records\n2. Display Records\n3. Search Specific Records\n4. Sort and Display Records\n5. Modify Records\n6. Exit")
        action = int(input("Please choose an action (Enter numbers 1-6):"))
        if action == 1:
            addrec() #to the add records main menu interface
        elif action == 2:
            disrec() #to the display records main menu interface
        elif action == 3:
            searchrec() #to the search records main menu interface
        elif action == 4:
            sortdisrec() #to the sort then display records main menu interface
        elif action == 5:
            modrec() #to the modify records main menu interface
        elif action == 6:
            flag = 1 #returns flag value as 1, breaks the loop
        else:
            print("Invalid input. Please enter numbers 1-6 only.")

#Add Records Directories
#Add Coach Record
def addcoachrec():
    flag = 0
    f = open("Coach_Records.txt", "a") #opens a file containing coach records, mode append; if no such file new file will be created
    while flag == 0: #initialise loop structure to repeat for another entry
        print("\nEnter coach details:")
        #sets values to variables using inputs
        coach_ID = input("Enter ID: ") 
        name = input("Enter name: ")
        date_join = input("Enter date joined (dd/mm/yyyy): ")
        date_term = input("Enter date terminated (dd/mm/yyyy): ")
        hrly_rate = input("Enter hourly rate: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        SC_code = input("Enter Sport Centre code: ")
        SC_name = input("Enter Sport Centre name: ")
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        rating = input("Rating (1-5): ")
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask ==1:
                flag = 1 #returns flag value as 1, breaks out of main loop
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")
        # Writes inputs into text file
        f.write(coach_ID +","+ name +","+ date_join +","+ date_term +","+ hrly_rate +","+ phone +","+ address +","+ SC_code +","+ SC_name +","+ sport_code +","+ sport_name +","+ rating +"\n")
    f.close() #Closes file

#Add Sport Record
def addsportrec():
    flag = 0
    f = open("Sport_Records.txt", "a") #opens a file containing sport records, mode append; if no such file new file will be created
    while flag == 0: #initialise loop structure to repeat for another entry
        print("\nEnter Sport details:")
        #sets values to variables using inputs
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask ==1:
                flag = 1#returns flag value as 1, breaks out of main loop
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")
        f.write(sport_code +","+ sport_name + "\n") #Write inputs to text file
    f.close() #Closes file

#Add Sport Schedule Record
def addsportschedulerec():
    flag = 0
    f = open("Sport_Schedule_Records.txt", "a")#opens a file containing sport schedule records, mode append; if no such file new file will be created
    while flag == 0: #initialise loop structure to repeat for another entry
        print("\nEnter Sport Schedule details:")
        #sets values to variables using inputs
        SC_code = input("Enter Sport Centre code: ")
        SC_name = input("Enter Sport Centre name: ")
        sport_code = input("Enter sport code: ")
        sport_name = input("Enter sport name: ")
        coach_ID = input("Enter coach ID: ")
        name = input("Enter coach name: ")
        day = input("Enter day (e.g. Thursday): ")
        date = input("Enter date (dd//mm/yyyy): ")
        time_start = input("Enter start time (e.g. 12:00PM): ")
        time_end = input("Enter end time (e.g. 12:00PM): ")
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask ==1:
                flag = 1 #returns flag value as 1, breaks out of main loop
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")
        f.write(SC_code +","+ SC_name +","+ sport_code +","+ sport_name +","+ coach_ID +","+ name +","+ day +","+ date +","+ time_start +","+ time_end + "\n") #Write inputs to text file
    f.close() #Closes file

#Add Registered Student Record
def addregstudrec():
    flag = 0
    f = open("Registered_Students_Records.txt", "a")#opens a file containing registed student records, mode append; if no such file new file will be created
    while flag == 0: #initialise loop structure to repeat for another entry
        print("\nEnter student details:")
        stud_ID = random.randrange(100,10**3) #using random to generate 3 digit student ID, store in variable stud_ID
        #sets values to variables using inputs
        name = input("Enter student name: ")
        age = input("Enter age: ")
        sex = input("Enter gender (Male/Female): ")
        date_join = input("Enter date joined (dd/mm/yyyy): ")
        date_term = input("Enter date terminated (dd/mm/yyyy): ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to continue (0 for yes, 1 for no)? "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask ==1:
                flag = 1 #returns flag value as 1, breaks out of main loop
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input. Please try again.")
        f.write(str(stud_ID) +","+ name +","+ age +","+ sex +","+ date_join +","+ date_term +","+ phone +","+ address +"\n") #Write inputs to text file
    f.close() #Closes file
    print("\nWelcome, registered student! You can now login as Registered Student at main menu (username: " + name + "; password: " + str(stud_ID)+")")    

#Display Records Directories
#Show Coach Record
def showcoachrec():
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))#prints title with formatted spacing
    with open("Coach_Records.txt", "r") as f: #opens a file containing coach records, mode read
        for line in f: #iterate through all lines in text file
            Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))
    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop, returns to the display records main menu interface
        else:
            print("Invalid input, please try again.")

#Show Sport Record
def showsportrec():
    print("{0:<20}{1:<20}".format("Sports_Code","Sports_Name")) #prints title with formatted spacing
    with open("Sport_Records.txt", "r") as f: #opens a file containing coach records, mode read 
        for line in f: #iterate through all lines in text file
            Sports_Code, Sports_Name = line.split(",") #split the line using comma
            print("{0:<20}{1:<20}".format(Sports_Code, Sports_Name))#print line with formatted spacing
    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop, returns to the display records main menu interface
        else:
            print("Invalid input, please try again.")

#Show Registered Student Record
def showregstudrec():
    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format("Student_ID","Student_Name","Age_When_Joined","Gender","Date_Joined","Date_Terminated","Phone_Number","Address"))#prints title with formatted spacing
    with open("Registered_Students_Records.txt", "r") as f: #opens a file containing registered student records, mode read 
        for line in f: #iterate through all lines in text file
            Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address = line.split(",") #split the line using comma
            print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format(Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address)) #print line with formatted spacing
    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop, returns to the display records main menu interface
        else:
            print("Invalid input, please try again.")

#Show Sport Schedule   
def showschedulerec():
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Day","Date","Start_Time", "End_Time"))#prints title with formatted spacing
    with open("Sport_Schedule_Records.txt", "r") as f: #opens a file containing sports schedule records, mode read 
         for line in f: #iterate through all lines in text file
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time = line.split(",") #split the line using comma
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time)) #print line with formatted spacing
    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop, returns to the display records main menu interface
        else:
            print("Invalid input, please try again.")

#Show Registered Sport Schedule
def showregschedulerec():
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Day","Date","Start_Time", "End_Time"))
    with open("Registered_Sport_Schedule_Records.txt", "r") as f: #opens a file containing registered sports schedule records, mode read 
        for line in f: #iterate through all lines in text file
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time = line.split(",") #split the line using comma
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time)) #print line with formatted spacing
    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop, returns to the display records main menu interface
        else:
            print("Invalid input, please try again.")

#Show Self Record
def showselfrec():
    flag = 0
    while flag == 0: #initialise loop structure for searching again if data given not found in line
        data = input("\nEnter your name (Search is case-sensitive): ") #set value to variable using inputs
        with open("Registered_Students_Records.txt", "r") as f: #opens a file containing registered student records, mode read 
            for line in f: #iterate through all lines in text file
                Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address = line.split(",") #split the line using comma
                if line.startswith(data,4): #checks if given data has matching elements in line, starting from the 4th element
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format("Student_ID","Student_Name","Age_When_Joined","Gender","Date_Joined","Date_Terminated","Phone_Number","Address")) #prints title with formatted spacing
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format(Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address)) #print line with formatted spacing            
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to search again (0 for yes, 1 for no)? "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask == 1: 
                flag = 1 #returns flag value as 1, break out of nested loop, returns to the registered student main menu interface
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")

#Search Records Directories
#Search Coach ID
def searchcoachid():
    flag = 0
    while flag == 0: #initialise loop structure for searching again if data given not found in line
        data = input("\nEnter Coach ID to search (3 digit inputs only, e.g. 001): ") #set value to variable using inputs
        with open("Coach_Records.txt", "r") as f: #opens a file containing coach records, mode read 
            for line in f: #iterate through all lines in text file
                Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
                if (line.startswith(data)): #checks if given data has matching elements in starting of line
                    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<10}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))#prints title with formatted spacing
                    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<10}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating)) #print line with formatted spacing                             
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to search again?(0 for yes, 1 for no) "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask == 1: 
                flag = 1 #returns flag value as 1, break out of nested loop, returns to the search records main menu interface
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")

#Search Coach Rating
def searchcoachrating():
    flag = 0
    while flag == 0: #initialise loop structure for searching again if data given not found in line
        data = input("\nEnter Rating (1-5) to search for coaches: ") #set value to variable using inputs
        with open("Coach_Records.txt", "r") as f: #opens a file containing coach records, mode read 
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:<15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating")) #prints title with formatted spacing   
            for line in f: #iterate through all lines in text file
                Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
                if line.startswith(data,-2): #checks if given data has matching elements in line, starting with the second last element
                    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:<15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating)) #print line with formatted spacing                                              
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to search again?(0 for yes, 1 for no) "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask == 1:
                flag = 1 #returns flag value as 1, break out of nested loop, returns to the search records main menu interface
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")

#Search Sport ID
def searchsportid():
    flag = 0
    while flag == 0: #initialise loop structure for searching again if data given not found in line
        data = input("\nEnter Sport ID to search (2 digit inputs only, e.g. 01): ") #set value to variable using inputs
        with open("Sport_Records.txt", "r") as f: #opens a texr file containing sport records, mode read 
            for line in f: #iterate through all lines in text file
                Sports_Code, Sports_Name = line.split(",") #split the line using comma
                if line.startswith(data): #checks if given data has matching elements in starting of line
                    print("{0:<20}{1:<20}".format("Sports_Code","Sports_Name")) #prints title with formatted spacing 
                    print("{0:<20}{1:<20}".format(Sports_Code, Sports_Name))#prints line with formatted spacing 
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to search again?(0 for yes, 1 for no) "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask == 1:
                flag = 1 #returns flag value as 1, break out of main loop, returns to the search records main menu interface
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.")

#Search Student ID
def searchstudid():
    flag = 0
    while flag == 0: #initialise loop structure for searching again if data given not found in line
        data = input("\nEnter Student ID to search (3 digit inputs only, e.g. 001): ") #set value to variable using inputs
        with open("Registered_Students_Records.txt", "r") as f: #opens a text file containing registered student records, mode read 
            for line in f: #iterate through all lines in text file
                Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address = line.split(",") #split the line using comma
                if line.startswith(data): #checks if given data has matching elements in starting of line
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format("Student_ID","Student_Name","Age_When_Joined","Gender","Date_Joined","Date_Terminated","Phone_Number","Address")) #prints title with formatted spacing 
                    print("{0:<15}{1:<15}{2:<20}{3:<10}{4:<15}{5:<17}{6:<15}{7:<15}".format(Student_ID,Student_Name,Age_When_Joined,Gender,Date_Joined,Date_Terminated,Phone_Number,Address)) #prints line with formatted spacing 
        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to search again?(0 for yes, 1 for no) "))
            if ask == 0:
                break #break out of nested loop, returns to main loop
            elif ask == 1:
                flag = 1 #returns flag value as 1, break out of nested loop, returns to the search records main menu interface
                break #break out of nested loop, returns to main loop
            else:
                print("Invalid input, please try again.") 

#Sorting Function
def sorter(list): #parameter "list" is passed through function
    for i in range(len(list)): #iterate through a range of numbers (number retrieved from getting length of parameter "list")                                 
        for j in range(len(list) - 1 ): #iterate through a range of numbers (number retrieved from getting length of parameter "list" then subtracting 1)                          
            if list[j] > list[j + 1]: #checks if value of element is larger than the adjacent element in parameter "list"
               list[j], list[j + 1] = list[j + 1], list[j] #swaps positions of the two elements
    return list 

#Swapping Function
def swap(list, pos1, pos2): #parameters "list", "pos1" and "pos2" are passed through function
    list[pos1], list[pos2] = list[pos2], list[pos1] #swaps positions of elements
    return list

#Sort and Display Records Directories
#Sort and Display Coach Name
def sortcoachname():
    f = open("Coach_Records.txt", "r") #opens a text file containing coach records, mode read 

    list1 = [] #empty list 
    for line in f: #iterate through lines in text file
        line = line.strip() #remove leading and trailing whitespaces
        line_list = line.split(",") #split the line using comma
        list1.append(line_list) #append lists to empty list of lists
    
    list2 = [] #empty list
    for i in list1: #iterate through elements in list of lists
        for j in i: #iterate through elements in list
            list2.append(swap( i, 0, 1)) #append to list2 after swapping positions of first two elements in each list from list1
            break #break out of loop

    sorter(list2) #sort values of list2 using sorter(list)
    
    list3 = [] #empty list
    for i in list2: #iterate through elements in list of lists
        for j in i: #iterate through elements in list
            list3.append(swap(i, 0, 1)) #append to list3 after returning elements to original positions from list2
            break #break out of loop

    with open("Coach_Records_Sorted_Names.txt", "w") as f: #opens a file containing coach records sorted by names, mode write; if no such file new file will be created 
        for i in list3: #iterate through elements in list of lists
            f.write(",".join(str(j) for j in i)) #writes inputs into text file, separated with ","
            f.write("\n") #writes in a new line in text file
    
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating")) #prints title with formatted spacing
    with open("Coach_Records_Sorted_Names.txt", "r") as f: #opens a text file containing coach records sorted by names, mode read
        for line in f: #iterate through all lines in text file
            Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))#prints lines with formatted spacing

    f.close() #closes file    

    while True: #initialise loop structure to repeat if inputs are incorrect
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            break #break out of loop
        else:
            print("Invalid input, please try again.")

#Sort and Display Coach Hourly Pay Rate
def sortcoachpay():
    #comments similar to sortcoachname function, only differences will be commented
    f = open("Coach_Records.txt", "r") 

    list1 = []
    for line in f:
        line = line.strip()
        line_list = line.split(",")
        list1.append(line_list)

    list2 = []
    for i in list1:
        for j in i:
            list2.append(swap( i, 0, 4)) #append to list2 after swapping positions of first and fifth elements in each list from list1
            break

    sorter(list2)

    list3 = []
    for i in list2:
        for j in i:
            list3.append(swap(i, 0, 4)) #append to list3 after returning elements to original positions from list2
            break

    with open("Coach_Records_Sorted_Payrate.txt", "w") as f: #opens a text file containing coach records sorted by hourly rate, mode write; if no such file new file will be created 
        for i in list3:
            f.write(",".join(str(j) for j in i))
            f.write("\n")
    
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))
    with open("Coach_Records_Sorted_Payrate.txt", "r") as f: #opens a text file containing coach records sorted by hourly rate, mode read
        for line in f:
            Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",")
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))

    f.close()     

    while True:
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            toggle = 1
            break
        else:
            print("Invalid input, please try again.")                

#Sort and Display Coach Rating
def sortcoachrating():
    #comments similar to sortcoachname function, only differences will be commented
    f = open("Coach_Records.txt", "r")

    list1 = []
    for line in f:
        line = line.strip()
        line_list = line.split(",")
        list1.append(line_list)

    list2 = []
    for i in list1:
        for j in i:
            list2.append(swap( i, 0, 11) )#append to list2 after swapping positions of first and last elements in each list from list1
            break

    sorter(list2)

    list3 = []
    for i in list2:
        for j in i:
            list3.append(swap(i, 0, 11)) #append to list3 after returning elements to original positions from list2
            break

    with open("Coach_Records_Sorted_Rating.txt", "w") as f: #opens a text file containing coach records sorted by rating, mode write; if no such file new file will be created 
        for i in list3:
            f.write(",".join(str(j) for j in i))
            f.write("\n")
    
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))
    with open("Coach_Records_Sorted_Rating.txt", "r") as f: #opens a text file containing coach records sorted by rating, mode read
        for line in f: 
            Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",")
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))

    f.close()     

    while True:
        ask = int(input("\nEnter 0 to exit: "))
        if ask == 0:
            toggle = 1
            break
        else:
            print("Invalid input, please try again.")

#Modify Records Directories
#Modify Coach Record
def modcoachrec():
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))#prints title with formatted spacing
    with open("Coach_Records.txt", "r") as f: #opens a text file containing coach records, mode read
        for line in f: #iterate through all lines in text file
            Coach_ID,Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number,Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",") #split the line using comma
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))#prints lines with formatted spacing
	
    with open("Coach_Records.txt", "r") as f: #opens a text file containing coach records, mode read
        ltr = int(input("Choose a line to modify (1st line under the titles is 1, and so on.): "))
        lines = f.readlines()[ltr-1] #assigns variable with line read at specific index in text file
    print("\nThe line to modify is line "+ str(ltr) +": " + lines)

    flag = 0
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        f = open("Coach_Records.txt", "r") #opens a text file containing coach records, mode read

        #code block for writing each element in text file into list of lists, see comments in sortcoachname for detail.
        list1 = [] 
        for line in f:
            line = line.strip()
            line_list = line.split(",")
            list1.append(line_list)

        f.close() #closes text file
        
        tts = str(input("Choose text to replace in line (Search is case-senstitive): "))
        a = list1[ltr-1] #list created from index of specific list from list of lists

        for i in a: #iterate through all elements in a
            if i == tts: #check for matching elements
                index1 = a.index(i) #returns index of matching elements in a
                flag = 1 #returns flag value 1, break out of main loop
            if tts not in a: #check for non-matching elements
                print("Word not found. Please try again.")
                break #breaks out of nested loop, return to main loop              

    ttr = str(input("Replacement text: "))
    a[index1] = ttr #replaces element of a at index1 with ttr 
    
    f = open("Coach_Records.txt", "w") #opens a text file containing coach records , mode write; if no such file new file will be created; if exists overwrites its contents

    #code block for writing lists into text file as strings, see comments in sortcoachname for detail.
    for i in list1: 
        f.write(",".join(str(j) for j in i))
        f.write("\n")
    f.close()

    print("\nUpdates have been saved. \n\nUpdated record:")
    print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format("Coach_ID","Coach_Name","Date_Joined","Date_Terminated","Hourly_Rate","Phone_Number","Address","SC_Code","SC_Name","Sports_Code","Sports_Name","Rating"))
    with open("Coach_Records.txt", "r") as f: #opens a text file containing coach records , mode read
        for line in f: 
            Coach_ID,Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number,Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating = line.split(",")
            print("{0:<10}{1:<13}{2:<15}{3:<17}{4:<15}{5:<15}{6:<15}{7:<10}{8:<30}{9:<15}{10:<15}{11:>15}".format(Coach_ID, Coach_Name, Date_Joined, Date_Terminated, Hourly_Rate, Phone_Number, Address, SC_Code, SC_Name, Sports_Code, Sports_Name, Rating))

#Modify Sport Record    
def modsportrec():
    #comments similar to modcoachrec function, only differences will be commented
    print("{0:<20}{1:<20}".format("Sports_Code","Sports_Name"))
    with open("Sport_Records.txt", "r") as f: #opens a text file containing sport records, mode read
        for line in f: 
            Sports_Code, Sports_Name = line.split(",")
            print("{0:<20}{1:<20}".format(Sports_Code, Sports_Name))
    
    with open("Sport_Records.txt", "r") as f: #opens a text file containing sport records, mode read
        ltr = int(input("\nChoose a line to modify (1st line under the titles is 1, and so on.): "))
        lines = f.readlines()[ltr-1]

    print("\nThe line to modify is line "+ str(ltr) +": " + lines)

    flag = 0
    while flag == 0:
        f = open("Sport_Records.txt", "r") #opens a text file containing sport records, mode read

        list1 = []
        for line in f:
            line = line.strip()
            line_list = line.split(",")
            list1.append(line_list)

        f.close() #closes text file
        
        tts = str(input("Choose text to replace in line (Search is case-senstitive): "))
        a = list1[ltr-1]
        for i in a:
            if i == tts:
                index1 = a.index(i)
                flag = 1
                break
            if tts not in a:
                print("Word not found. Please try again.")
                break                
        break
    ttr = str(input("Replacement text: "))
    a[index1] = ttr
    
    f = open("Sport_Records.txt", "w") #opens a text file containing sport records , mode write; if no such file new file will be created; if exists overwrites its contents
    for i in list1:
        f.write(",".join(str(j) for j in i))
        f.write("\n")
    f.close()

    print("\nUpdates have been saved. \n\nUpdated record:")
    print("{0:<20}{1:<20}".format("Sports_Code","Sports_Name"))
    with open("Sport_Records.txt", "r") as f: #opens a text file containing sport records, mode read
        for line in f: 
            Sports_Code, Sports_Name = line.split(",")
            print("{0:<20}{1:<20}".format(Sports_Code, Sports_Name))
   
#Modify Sport Schedule Record
def modsportschedulerec():
    #comments similar to modcoachrec function, only differences will be commented
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Day","Date","Start_Time", "End_Time"))
    with open("Sport_Schedule_Records.txt", "r") as f: #opens a text file containing sport schedule records, mode read
        for line in f: 
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time = line.split(",")
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time))
    
    with open("Sport_Schedule_Records.txt", "r") as f: #opens a text file containing sport schedule records, mode read
        ltr = int(input("\nChoose a line to modify (1st line under the titles is 1, and so on.): "))
        lines = f.readlines()[ltr-1]

    print("\nThe line to modify is line "+ str(ltr) +": " + lines)

    flag = 0
    while flag == 0:
        f = open("Sport_Schedule_Records.txt", "r") #opens a text file containing sport schedule records, mode read

        list1 = []
        for line in f:
            line = line.strip()
            line_list = line.split(",")
            list1.append(line_list)

        f.close() #closes text file
        
        tts = str(input("Choose text to replace in line (Search is case-senstitive): "))
        a = list1[ltr-1]
        for i in a:
            if i == tts:
                index1 = a.index(i)
                flag = 1
            if tts not in a:
                print("Word not found. Please try again.")
                break                

    ttr = str(input("Replacement text: "))
    a[index1] = ttr
    
    f = open("Sport_Schedule_Records.txt", "w") #opens a text file containing sport schedule records , mode write; if no such file new file will be created; if exists overwrites its contents
    for i in list1:
        f.write(",".join(str(j) for j in i))
        f.write("\n")
    f.close()

    print("\nUpdates have been saved. \n\nUpdated record:")
    print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format("SC_Code","SC_Name","Sports_Code","Sports_Name","Coach_ID","Coach_Name","Day","Date","Start_Time", "End_Time"))
    with open("Sport_Schedule_Records.txt", "r") as f: #opens a text file containing sport schedule records, mode read
        for line in f:
            SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time = line.split(",")
            print("{0:<10}{1:<30}{2:<15}{3:<15}{4:<10}{5:<15}{6:<15}{7:<15}{8:<15}{9:<10}".format(SC_Code, SC_Name, Sports_Code, Sports_Name, Coach_ID, Coach_Name, Day, Date, Start_Time, End_Time))
   

#Modify Self Record
def modselfrec():
    while True: #initialise loop structure to repeat if inputs are incorrect
        data = input("\nEnter your name (search is case-sensitive): ") #assign value to variables using input
        with open("Registered_Students_Records.txt", "r") as f: #opens a text file containing registered student records, mode read

            #code block for creating a list of lists from lines in text file
            list1 = []
            for line in f: #iterate through all lines in text file
                line = line.strip() #remove leading and trailing whitespaces
                line_list = line.split(",") #split line with comma
                list1.append(line_list) #append lines to list of lists

            #code block for searching matching data in list from list of lists
            for i in list1: #traverse all lists in list1
                for j in i: #traverse all elements of all lists in list1
                    if j == data: #check for matching data
                        index1 = list1.index(i) #index of list containing matching data from list of lists
                        a = list1[index1] #list created from index of specific list from list of lists
                        print("Line to modify is :", a)

                        flag = 0
                        while flag == 0: #initialise loop structure to repeat if inputs are incorrect   
                            tts = str(input("Choose text to replace in line (Search is case-senstitive): "))
                            for i in a: #iterate through all elements in a
                                if i == tts: #check for matching data
                                    index2 = a.index(i) #index of element containing matching data from list
                                    flag = 1 #returns flag value 1, break out of nested loop, returns to main loop
                                if tts not in a: #check for non-matching elements
                                    print("Word not found. Please try again.")
                                    break #break out of nested loop, returns to main loop

                        ttr = str(input("Replacement text: "))
                        a[index2] = ttr #replaces element of a at index2 with ttr 
                        print("\nUpdates have been saved.")
                        print("Line after modification: ", a)
        break #break out of the main loop

    #code block for writing lists into text file as strings, see comments in sortcoachname for detail.               
    f = open("Registered_Students_Records.txt", "w")
    for i in list1:
        f.write(",".join(str(j) for j in i))
        f.write("\n")
    f.close()   

#Feedback Directory
def feedback():
    flag = 0
    f = open("Feedback.txt","a") ##opens a text file containing feedback records, mode append; if no such file new file will be created
    while flag == 0: #initialise loop structure to repeat if inputs are incorrect
        print("Feedback Details:")

        #assign value to variables using inputs
        name1 = input("Enter your name: ")
        name2 = input("Enter coach's name: ")
        fdbck = input("Feedback: ")
        rate = input("Rating (1-5): ")

        while True: #initialise loop structure to repeat if inputs are incorrect
            ask = int(input("\nWould you like to add another entry? (0 for yes, 1 for no)"))
            if ask == 0:
                break #break out of nested loop, return to main loop
            elif ask ==1:
                flag = 1 #return flag value 1, break out of main loop
                print("Thanks for the feedback!")
                break #break out of nested loop, return to main loop
            else:
                print("Invalid input, please try again.")            
        f.write(name1 + "," + name2 + "," + fdbck + "," + rate +"\n") #writes inputs into text file
    f.close()#closes text file

#Add Records Main Menu     
def addrec():
    while True: #initialise loop structure to repeat if inputs are incorrect
        print("\nADD RECORDS MENU")
        print("1. Coach\n2. Sports\n3. Sport Schedule\n4. Exit")
        action = int(input("Choose item to add records of (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            addcoachrec() #to Add Coach Record interface
        elif action == 2:
            addsportrec() #to Add Sport Record interface
        elif action == 3:
            addsportschedulerec() #to Add Sport Schedule Record interface
        elif action == 4:
            break #to admin menu interface
        else:
            print("Invalid input. Please enter numbers 1-4 only.")

#Display Records Main Menu
def disrec():   
    while True: #initialise loop structure to repeat if inputs are incorrect
        print("\nDISPLAY RECORDS MENU")
        print("1. Coach\n2. Sports\n3. Registered Students\n4. Exit")
        action = int(input("Choose item to display records of (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            showcoachrec() #to Show Coach Record interface
        elif action == 2:
            showsportrec() #to Show Sport Record interface
        elif action == 3:
            showregstudrec() #to Show Registered Student Record interface
        elif action == 4:
            break #to admin menu interface
        else:
            print("Invalid input. Please enter numbers 1-4 only.")

#Search Records Main Menu
def searchrec():
    while True:
        print("\nSEARCH RECORDS MENU")
        print("1. Coach by Coach ID\n2. Coach by Overall Performance (Rating)\n3. Sport by Sport ID\n4. Student by Student ID\n5. Exit")
        action = int(input("Choose item to search specific records of (Enter numbers 1-4) or exit (Enter number 5): "))
        if action == 1:
            searchcoachid() #to Search Coach ID interface
        elif action == 2:
            searchcoachrating() #to Search Coach Rating interface
        elif action == 3:
            searchsportid() #to Search Sport ID interface
        elif action == 4:
            searchstudid() #to Search Student ID interface
        elif action == 5:
            break #to admin menu interface
        else:
            print("Invalid input. Please enter numbers 1-5 only.")

#Sort and Display Records Main Menu
def sortdisrec():
    while True:
        print("\nSORT AND DISPLAY RECORDS MENU")
        print("1. Coaches in Ascending Order by Names\n2. Coaches Hourly Pay Rate in Ascending Order\n3. Coaches Overall Performance in Ascending Order\n4. Exit")
        action = int(input("Choose item to sort and display (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            sortcoachname() #to Sort and Display Coach Name interface
        elif action == 2:
            sortcoachpay() #to Sort and Display Coach Hourly Pay Rate interface
        elif action == 3:
            sortcoachrating() #to Sort and Display Coach Rating interface
        elif action == 4:
            break #to admin menu interface
        else:
            print("Invalid input. Please enter numbers 1-5 only.")

#Modify Records Main Menu
def modrec():
    while True:
        print("\nMODIFY RECORDS MENU")
        print("1. Coach Records\n2. Sports Records\n3. Sport Schedule Records\n4. Exit")
        action = int(input("Choose item modify (Enter numbers 1-3) or exit (Enter number 4): "))
        if action == 1:
            modcoachrec() #to Modify Coach Record interface
        elif action == 2:
            modsportrec() #to Modify Sport Record interface
        elif action == 3:
            modsportschedulerec() #to Modify Sport Schedule Record interface
        elif action == 4:
            break #to admin menu interface
        else:
            print("Invalid input. Please enter numbers 1-4 only.")

mainmenu()
