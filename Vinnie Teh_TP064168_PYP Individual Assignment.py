#Vinnie Teh
#TP064168
  
#list would not save the data input by the user after the user closed the program.
#text file could save the data input by the user although the user closed the program.
#list should be keep updated by adding the data from text file whenever the user hits run.

#list of grocery_list will contain the latest grocery information from txtfile input when the user start running the program.

#update grocery list
def update_grocerylist(txtfile):            #txtfile is parameter of this function, the caller should input the name of text file.
    grocery_list = []                       #grocery_list is an empty list created to store all groceries and their detail
    
    grocery_txt = open(txtfile,"r")         #grocery_txt is a variable that stores the txtfile with read mode
    
    grocery = []                            #grocery is an empty list created to store a grocery with its detail
    
    i = 1                                   #set the value of i to 0
    
    for information in grocery_txt:         #information is each line in grocery_txt. For loop is to iterate through each information in grocery_txt.
        if information.startswith("-"):     #to return True if the word starts with "-"
            pass                            #nothing will be executed
        else:
            try:
                topic,info = information.split(":") #":"is the separator to seperate the information and assign to topic and info accordingly.
                grocery.append(info.strip())    #Strip() eliminate any whitespace from the string's beginning and end.
                                                #append function allows the new elements be added to the end of the grocery list.  
                i = i + 1                       # the value of i will be reassigned to i + 1 when the information is not start with "-"
                if i % 5 == 0:                  #i modulo 5 == 0 means the remainder of i divide by 5 is zero
                    i = 1                       #i will be reassigned by 1 again
                    grocery_list.append(grocery)#append function allows the grocery list be added to the end of the grocery_list.
                    grocery = []                #grocery variable will be reassigned to empty list again
            except:
                pass
            
    return(grocery_list)                    #return the result of grocery_list to the caller.



#to update the customer order from text file into the list whenever the user hit run.
#Thus, the registered_order list will contain the latest order information from "RegisteredOrder.txt" when the user start running the program.

#update order list
def update_orderlist(): 
    registered_order = []                   #registered_order is an empty list created to store all the customer orders and detail
    
    order_txt = open("RegisteredOrder.txt","r") #order_txt is a variable that stores the "RegisteredOrder.txt" with read mode
    
    customer = []                           #customer is an empty list created to store a customer orders with its detail
    
    i = 0                                   #set the value of i to 0
    for order in order_txt:                 #order is each line in order_txt. For loop is to iterate through each order in order_txt.
        if order.startswith("-"):           #to return True if the word starts with "-"
            pass                            #nothing will be executed
        else:
            try:
                topic,info = order.split(":")   #":"is the separator to seperate the information and assign to topic and info accordingly.
                customer.append(info.strip())   #Strip() eliminate any whitespace from the info's beginning and end. The \n will be elimated also
                                                #append function allows the stripped info be added to the end of the customer list. 
                i = i + 1                       # the value of i will be reassigned to i + 1 when the information is not start with "-"
                if i % 5 == 0:                  #i modulo 5 == 0 means the remainder of i divide by 5 is zero
                    registered_order.append(customer) #append function allows the customer list be added to the end of the registered_order list.
                    customer = []               #customer variable will be reassigned to empty list again
            except:
                pass
            
    return(registered_order)                #return the result of registered_order to the caller.
   


#update "RegisteredOrder.txt" with the element of registered_order list after the customer placed order.

#update order text
def updateorder_txt(customer):              #customer is parameter of this function, caller should input a variable inside the parenthesis.
    order_txt = open("RegisteredOrder.txt","a") #order_txt is a variable that stores the "RegisteredOrder.txt" with append mode
    order_txt.write("\nUsername: ")         #create a new line and write "Username: " into the order_txt
    order_txt.write(customer[0])            #write the first element of customer list into the order_txt
    order_txt.write("\nGrocery Name: ")     #create a new line, write "Grocery Name: " into the order_txt
    order_txt.write(customer[1])            #write the second element of customer list into the order_txt
    order_txt.write("\nPrice Per Quantity: ")#create a new line, write "Price Per Quantity: " into the order_txt
    order_txt.write(customer[2])            #write the third element of customer list into the order_txt
    order_txt.write("\nQuantity: ")         #create a n new line, write "Quantity: " into the order_txt
    order_txt.write(str(customer[3]))       #write the fourth element of customer list into the order_txt
    order_txt.write("\nTotal Price: ")      #create a new line, write "Total Price: " into the order_txt
    order_txt.write(customer[4])            #write the fifh element of customer list into the order_txt
    order_txt.write("\n----------------------------------") #create a new line, write "----------------------------------" into the order_txt

    order_txt.close()                       #close "RegisteredOrder.txt"



#update the txtfile with element of category list after the admin change the grocery and groceries detail.

#update grocery text    
def updategrocery_text(txtfile,category):   #txtfile and category parameters of this function, caller should input two variables inside the parenthesis.
    grocery_txt = open(txtfile,"w")         #grocery_txt is a variable that opens the txtfile with read mode
    for content in category:                #category is a list contain content lists, content is each list in category. 
                                            #For loop is to iterate through each content in category.
        name = content[0]                   #the first element in content is assigned to name variable
        price = content[1]                  #the second element in content is assigned to price variable
        expired_date = content[2]           #the third element in content is assigned to expired_date variable
        details = content[3]                #the fourth element in content is assigned to details variable
        grocery_txt.write("\nName:")        #create a new line and write "Quantity: " in the grocery_txt       
        grocery_txt.write(name)             #write the value of name into the grocery_txt 
        grocery_txt.write("\n")             #create a new line
        grocery_txt.write("Price:")         #write "Price: " into the grocery_txt
        grocery_txt.write(price)            #write the value of price into the grocery_txt 
        grocery_txt.write("\n")             #create a new line
        grocery_txt.write("Expired Date:")  #write "Expired Date: " into the grocery_txt
        grocery_txt.write(expired_date)     #write the value of expired_date into the grocery_txt 
        grocery_txt.write("\n")             #create a new line
        grocery_txt.write("Details:")       #write "Details: " into the grocery_txt
        grocery_txt.write(details)          #write the value of details into the grocery_txt 
        grocery_txt.write("\n----------------------------------") #create a new line, then write "----------------------------------" 
    grocery_txt.close()                     #close txtfile
    


#prompt users in Menu Page

#Menu Page    
def menu():
    invalid = True                          #assign a Boolean value which is True for invalid variable. Boolean contains True or False only
    while invalid:                          #the code block inside the while loop would repeatedly executed until the value of invalid variable becomes False
            users = input('''\nPlese select the type of users for this system to proceed: \n
                  Type 1 to proceed to Admin Page. \n
                  Type 2 to proceed to New Customer Page. \n
                  Type 3 to proceed to Registered Customer Page. \n
                  Type 4 to exit this program.\n>''') #get and input the answer from user and assign it in users variable
            if users == "1":                #if the value of users equal to "1" 
                admin()                     #call admin function
                invalid = False             #the boolean value of invalid variable will become False to escape from while loop
            elif users == "2":              #if the value of users equal to "2" 
                newCustomerMenu()           #call newCustomerMenu function
                invalid = False             #the boolean value of invalid variable will become False to escape from while loop 
            elif users == "3":              #if the value of users equal to "3" 
                registeredlogin()           #call registered function
                invalid = False             #the boolean value of invalid variable will become False to escape from while loop
            elif users == "4":              #if the value of users equal to "4"
                print("Thank You! Come Again!")
                exit()                      #call exit function
                invalid = False             #the boolean value of invalid variable will become False to escape from while loop
            else:                           #if not all the condition stated above
                print("Invalid Input.\n")#display "Invalid Input."
                invalid = True              #the boolean value of invalid variable will mantain True and could not escape from while loop

        
# to reset password if the admin or registered customers forgot their password

#reset password                
def resetpassword(txtfile, oripass,changepass):  #txtfile, oripass, changepass is the parameters of this function
                                                 #caller should input three variables inside the parenthesis.
    text = open(txtfile, "r")                    #readtext is a variable that opens the txtfile with read mode
    readtext = text.read()                       #read the information in the readtext
    readtext = readtext.replace(oripass,changepass) #the value of changepass will replace with the value of oripass in readtext
    text_edit = open(txtfile, "w")               #text_edit is a variable that opens the txtfile with write mode
    text_edit.write(readtext)                    #text_edit will be overwritten with the content of readtext
    text_edit.close()                            #close txtfile



#ensure two decimal places    
def twodecimal(price):                           #price is the parameter of this function, caller should input one variable to call this function
    price = str(price)                           #price is declare as string
    try:                                         #the block of code could be tested for errors using try block
        beforedecimal, afterdecimal = price.split('.')  #"."is the separator to seperate the price and assign to beforedecimal and afterdecimal accordingly.
        afterdecimal = afterdecimal.strip()      #Strip() eliminate any whitespace from the afterdecimal's beginning and end. The \n will be elimated also
        if len(afterdecimal) == 1:               #if the number of characters in the value of aferdecimal is 1
            price = price + "0"                  #reassign the value that concatenate the value of price with "0" to the price variable
        elif len(afterdecimal) == 2:             #else if the number of characters in the value of aferdecimal is 2
            pass                                 #nothing will be executed
        elif len(afterdecimal) >2:               #else if the number of characters in the value of aferdecimal is greater than 2
            afterdecimal = afterdecimal[:2]      #reassign the value of afterdecimal to afterdecimal that slice from beginning to the second character only
            price = beforedecimal + "." + afterdecimal #reassign the value that concatenate the value of beforedecimal, "." and afterdecimal to the price 
    except:                                      #the error could be dealt with except code without display red code when the user runs the program
        price = price + ".00"                    #reassign the value that concatenate the price with ".00"  to the price variable                     
    return price                                 #return the result of price to the caller




#display the specific category of grocery and groceries details

#view specific cateory
def viewcategory(num):                           #num is the parameter of this function, caller should input one variable to call this function
    category = num                               #assign the value of num to the category variable
    if category == 1:                            #if the value of category eqauals to 1
        print("\t\t\tMedicine Category\n")       #create the new tabs for three time, display "Medicine Category"
        medicines = open("medicine.txt","r")     #medicines is a variable that opens "medicine.txt" with read mode
        for medicine in medicines:               #medicine indicates each line in medicines. For loop is to iterate through each medicine in medicines.
            print(medicine)                      #display every value of medicine while iterating through medicines
        medicines.close()                        #close "medicine.txt"
    elif category == 2:                          #else if the value of category equals to 2
        print("\t\t\tVegetable Category\n")      #create the new tabs for three time, display "Vegetable Category"
        vegetables = open("vegetable.txt","r")   #vegetables is a variable that opens "vegetable.txt" with read mode
        for vege in vegetables:                  #vege indicates each line in vegetables. For loop is to iterate through each vege in vegetables.
            print(vege)                          #display every value of vege while iterating through vegetables
        vegetables.close()                       #close "vegetable.txt"
    elif category == 3:                          #else if the value of category equals to 3
        print("\t\t\tFruit Category\n")          #create the new tabs for three time, display "Fruit Category"
        fruits = open("fruit.txt","r")           #fruits is a variable that opens "fruit.txt" with read mode
        for fruit in fruits:                     #fruit indicates each line in fruits. For loop is to iterate through each fruit in fruits.
            print(fruit)                         #display every value of fruit while iterating through fruits
        fruits.close()                           #close "fruit.txt"
    elif category == 4:                          #else if the value of category equals to 4
        print("\t\t\tDairy Category\n")          #create the new tabs for three time, display "Dairy Category"
        dairies = open("dairy.txt","r")          #dairies is a variable that opens "dairy.txt" with read mode
        for dairy in dairies:                    #dairy indicates each line in dairies. For loop is to iterate through each dairy in dairies.
            print(dairy)                         #display every value of dairy while iterating through dairies
        dairies.close()                          #close "dairy.txt"
    elif category == 5:                          #else if the value of category equals to 5
        print("\t\t\tHousehold Category\n")      #create the new tabs for three time, display "Household Category"
        households = open("household.txt","r")   #households is a variable that opens "household.txt" with read mode
        for household in households:             #household indicates each line in households. For loop is to iterate through each household in households.
            print(household)                     #display every value of household while iterating through households
        households.close()                       #close "household.txt"


#display all the name of grocery according to the category without details

#view all uploaded Groceries        
def viewgrocery():
    print("\n\t\t\tMedicine Category\n")         #create a new line and three new tabs, display "Medicine Category"
    mcount = 1                                   #assign 1 to the value of mcount 
    for medicine in medicine_detail:             #medicine_detail is a list contain medicine lists, medicine is each list in medicine_detail. 
                                                 #For loop is to iterate through each medicine in medicine_detail.
        print(f"{mcount}. {medicine[0]}")        #f-string could join two variables without spaces between them.
                                                 #display the value of mcount, ".",and the first element of medicine while iterating through medicine_detail
        mcount = mcount+1                        #reassign the value of mcount plus 1 to mcount variable while iterating through medicine_detail
        
    print("\n\t\t\tVegetable Category\n")        #create a new line and three new tabs, display "Vegetable Category"
    vcount = 1                                   #assign 1 to the value of mcount 
    for vege in vege_detail:                     #vege_detail is a list contain vege lists, vege is each list in vege_detail. 
                                                 #For loop is to iterate through each vege in vege_detail.
        print(f"{vcount}. {vege[0]}")            #f-string could join two variables without spaces between them.
                                                 #display the value of vcount, ".",and the first element of vege while iterating through vege_detail
        vcount = vcount + 1                      #reassign the value of vcount plus 1 to vcount variable while iterating through vege_detail
    
    print("\n\t\t\tFruit Category\n")            #create a new line and three new tabs, display "Fruit Category"
    fcount = 1                                   #assign 1 to the value of fcount 
    for fruit in fruit_detail:                   #fruit_detail is a list contain fruit lists, fruit is each list in fruit_detail. 
                                                 #For loop is to iterate through each fruit in fruit_detail.
        print(f"{fcount}. {fruit[0]}")           #f-string could join two variables without spaces between them.
                                                 #display the value of fcount, ".",and the first element of fruit while iterating through fruit_detail
        fcount = fcount + 1                      #reassign the value of fcount plus 1 to fcount variable while iterating through fruit_detail
        
    print("\n\t\t\tDairy Category\n")            #create a new line and three new tabs, display "Dairy Category"
    dcount = 1                                   #assign 1 to the value of dcount 
    for dairy in dairy_detail:                   #dairy_detail is a list contain dairy lists, dairy is each list in dairy_detail. 
                                                 #For loop is to iterate through each dairy in dairy_detail.
        print(f"{dcount}. {dairy[0]}")           #f-string could join two variables without spaces between them.
                                                 #display the value of dcount, ".",and the first element of dairy while iterating through dairy_detail
        dcount = dcount + 1                      #reassign the value of dcount plus 1 to dcount variable while iterating through dairy_detail
        
    print("\n\t\t\tHousehold Category\n")        #create a new line and three new tabs, display "Household Category"
    hcount = 1                                   #assign 1 to the value of hcount 
    for household in household_detail:           #household_detail is a list contain household lists, household is each list in household_detail. 
                                                 #For loop is to iterate through each household in household_detail.
        print(f"{hcount}. {household[0]}")       #f-string could join two variables without spaces between them.
                                                 #display the value of hcount,".",and the first element of household while iterating through household_detail         
        hcount = hcount + 1                      #reassign the value of hcount plus 1 to hcount variable while iterating through household_detail

    ans = False                                  #assign a Boolean value which is False for ans variable. Boolean contains True or False only
    while not ans:                               #the code block inside the while loop would repeatedly executed until the Boolean value of ans becomes True.
        back = input("Type 'N' to back to Admin Menu Page.\n>") #get the value of back from the user by displaying "Type 'N' to back to Admin Menu Page."
                                                                #create a new line
        if back == "N":                          #check if the value of back is equal to "N"
            adminMenu()                          #call adminMenu()
            ans = True                           #reassign the Boolean value of ans to True
            break                                #escape from while not ans loop
        else:                                    #check if the value of back is not equal to "N"
            print("Invalid Input.")              #display "Invalid Input".
                                                 #while not ans loop would repeatedly executed the code block until the Boolean value of ans becomes True.  
    


#to allow the admin to upload groceries and groceries detail

#upload Groceries detail in system            
def admin_upload():
    number = False                               #assign a Boolean value which is False for number variable. Boolean contains True or False only.
    while not number:                         #the code block inside the while loop would repeatedly executed until the Boolean value of number becomes True.
        print("\nPlease enter the category of the grocery that needs to be uploaded.") #display a sentence.
        try:                                     #the block of code could be tested for errors using try block.
            category = int(input("Type 1 - Medicine\nType 2 - Vegetable\nType 3 - Fruits\nType 4 - Dairy\nType 5 - Household\n>"))
                                                 #get the value of cateogry from the user by displaying some sentences.
                                                 #declare the type of value of the category as integer, so the user can only enter number.
            if category >= 0 and category <= 5:  #check if the value of category is larger or equal to 0 and smaller or equal to 5.
                number = True                    #reassign the Boolean value of number to True.
                break                            #escape from while not number loop.
            else:                                #check if doesn't meet the condition above
                print("The number is out of range.\n") #display "The number is out of range." and create a new line.
                number = False                   #remain the Boolean value of number which is False.
                                              #while not number loop would repeatedly executed the code block until the Boolean value of number becomes True.
        except:                                  #the error could be dealt with except code without display red code when the user runs the program.
            print("Invalid Input. Please enter a number.\n") #display "Invalid Input. Please enter a number." and create a new line.
            number = False                       #remain the Boolean value of number which is False.
                                              #while not number loop would repeatedly executed the code block until the Boolean value of number becomes True.
    if category == 1:                            #check if category is equal to 1.
        category = medicine_detail               #reassign medicine_detail to the value of category.
    elif category == 2:                          #check if category is equal to 2.
        category = vege_detail                   #reassign vege_detail to the value of category.
    elif category == 3:                          #check if category is equal to 3.
        category = fruit_detail                  #reassign fruit_detail to the value of category.
    elif category == 4:                          #check if category is equal to 4.
        category = dairy_detail                  #reassign dairy_detail to the value of category.
    elif category == 5:                          #check if category is equal to 5.
        category = household_detail              #reassign household_detail to the value of category.
    
    newdetail = []                               #newdetail is an empty list created to store the grocery with its detail.
    upload_name = False                          #assign a Boolean value which is False for upload_name variable. Boolean contains True or False only.
    proceed = True
    while not upload_name:                    #the code block inside the while loop would repeatedly executed until the Boolean value of number becomes True.
        test = False
        existing_name = "-"                      #assign "-" to existing_name
        groceries_name = input("\nPlease enter the name of grocery that need to be uploaded.\n*Press'x' to back to Admin Main Page.*\n>")
                                                 #get the value of groceries_name by displaying the text
        strip_name = groceries_name.strip()      #strip() eliminate any whitespace from the groceries_name's beginning and end.
        if strip_name == "":                                    #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                 #display text
            upload_name = False                                   #remain the Boolean value of upload_name to False.
            test = True
                                                                  #will repeat while not upload_name loop if the user keep leaving it blank.
            
        elif groceries_name == "x":                               #to check if the user enter "x"
            adminMenu()                                           #call adminMenu
            upload_name = True                                    #reassign the Boolean value of upload_name to True
            proceed = False
            break                                                 #stop repeating while not upload_name loop if the user enter"x"
        
        else:
            groceries_name = groceries_name[0].upper()+ groceries_name[1:].lower()
            for existing_category in category:       #category is a list contain existing_category lists, existing_category is each list in category. 
                                                     #For loop is to iterate through each existing_category in category.
                if existing_category[0] == groceries_name: #to check if the grocery has been uploaded or not
                                       existing_name = groceries_name #reassign the value of groceries_name to existing_name
                                       
            if existing_name == groceries_name:                       #to check if existing_name is equal to groceries_name
                    print("This grocery has been uploaded before.")   #print text
                    upload_name = False                               #remain the Boolean value of upload_name which is False.
                                                                      #will repeat while not upload_name loop if the user keep typing the uploaded grocery name.
                    
            else:                                                     #if not meet all the condition above
                try:                                                  #the block of code could be tested for errors using try block.
                    groceries_name = int(groceries_name)              #to check if the user type number only
                    print("Invaid name. Please enter the actual name of the grocery.") #display text
                    upload_name = False                               #remain the Boolean value of upload_name as False.
                                                                      #will repeat while not upload_name loop if the user keep typing number only.
                    
                except:                                               #if the user does not enter integer, the program will not display red code
                    groceries_name = groceries_name[0].upper()+ groceries_name[1:].lower()
                    newdetail.append(groceries_name)                  #the groceries_name would be added to the newdetail list
                    upload_name = True                                #reassign the Boolean value of upload_name to True
                    break                                             #stop repeating while not upload_name loop if the user enter a valid grocery name
            
    upload_price = False                                              #assign a Boolean value to upload_price which is False
    if proceed:
        while not upload_price:                                       #the program will keep asking the price if the user enter invalid input.
            print("\nPlease enter the price of",groceries_name)         #print text
            groceries_price = input("> RM ")                          #get the value of groceries_price. The user could only enter number.
            strip_price = groceries_price.strip()                     #to eliminate any whitespace from the groceries_price's beginning and end.
            
            if strip_price == "":                                     #to check if the user leave it blank or click space only
                print("Please don't leave it blank.")                 #display text
                upload_price = False                                  #the program will keep asking the user to enter the price again
                
            else:                                                     #if the user didn't leave it blank or click space only
                isfloat = False                                       #set the boolean value of isfloat to True
                
                try:                                                  #the block of code could be tested for errors using try block.
                    groceries_price = float(groceries_price)          #the user could only enter number with decimal or without decimal
                    isfloat = True                                    
                    
                except:                                               #the program will not display red code if the user does not enter number
                    print("Invalid input. Please enter number.")      #display text
                    isfloat = False                                   #the program will keep asking the user to enter the price again
                    upload_price = False
                    
                if isfloat:
                    groceries_price = "RM" + twodecimal(groceries_price)#to set the groceries_price to the price format (RMXX.XX)
                    newdetail.append(groceries_price)                 #add the price input by the user to the newdetail list
                    upload_price = True                               #reassign the boolean value of upload_price to True
                    break                                             #the program will not keep asking the user to enter the price again                                                                                     
                
        upload_date = False                                           #to set the Boolean value of upload_date to False
        while not upload_date:                                        #the program will keep asking the user to input expired date if the date is unvalid.
            print("\nPlease enter the expired date of",groceries_name, "(DD/MM/YYYY)")  #display text
            groceries_exp = str(input("> "))                          #ask the user to enter expired date
            strip_date = groceries_exp.strip()                        #remove white space and new line of the groceries_exp and assign it to strip_date
            if strip_date == "":                                      #to check if the user leave it blank or click space only
                print("Please don't leave it blank.")                 #display text
                upload_date = False                                   #remain the boolean value of the upload_date
                                                                      #the program will keep asking the user to input expired date as the date is unvalid.
                
            else:                                                     #if the user doesn't leave it blank or click space only
                formattrue = False                                    #assign the value of formattrue to False
                
                while not formattrue:                                 #the program will keep asking the true format if the date format is wrong.
                    try:                                              #the block of code could be tested for errors using try block.
                        day, month, year = groceries_exp.split("/")   #the content in groceries_exp is split using "/" and assign to day, month, year accordingly
                                                                      #to check if the date format is true (DD/MM/YYYY)
                        formattrue = True                             #reassign boolean value of formattrue to True
                        break                                         #the program will stop asking the true format
                    
                    except:                                           #the program will not show the red code if the date could not be splitted.
                        groceries_exp = input("\nPlease enter the true format which is DD/MM/YYYY.\n>")
                                                                      #the program will ask the true format as the date format is wrong.
                        formattrue = False
                if len(day)>2 or len(month)>2 or len(year)!= 4 :      #to check if the date or month is more than 2 digits, or the year is not 4 digits. 
                    print("The expired date is invalid.")             #display text
                    upload_date= False                                #the program will keep asking the user to input expired date as the date is unvalid.
                    
                else:                                                 #if the digits of date and month is true                                      
                    num = True                                        #set the Boolean value of num to True
                    try:                                              #the block of code could be tested for errors using try block.
                        day = int(day)                                #the user could only enter number
                        month = int(month)
                        year = int(year)
                    except:                                           #the program will not display red code if the user enter words
                        print("The expired date is invalid. Please enter number.") #display text
                        upload_date = False                           #remain the boolean value of upload_date
                        num = False                                   #reassign the boolean value of num to False
                                                                      #the program will keep asking the user to input expired date as the date is unvalid.
                        
                    if num:                                           #if the user enter number. To check if the user enter the month that is out of range.
                        if month > 12 or month < 0:                   #one year has 12 month only           
                            print("The expired date is invalid.")     #display text
                            upload_date = False                       #the program will keep asking the user to input expired date as the date is unvalid.
                            
                        else:                                                         #if the month enter by the user is true
                            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  #to check if it is a leap year
                                if month == 2:                                        #in leap year, february has 29 days
                                    if day<0 or day> 29:                              #to check if the day enter by the user is more than 29 or less than 0
                                        print("The expired date is invalid.")         #print text            
                                        upload_date = False                           #the program will keep asking the user to input expired date 
                                        
                                    else:                                             #if the date is valid
                                        newdetail.append(groceries_exp)               #groceries_exp will be added to newdetail list
                                        upload_date = True                            #reassign the boolean value of upload_date to True
                                        break                                         #the program will stop asking the user to input expired date
                                    
                            else:
                                if month == 2:                                            #february have 28 days only if it is not the leap year
                                    if day>0 and day<= 28:                                #to check if the day enter by the user is less than 29 or more than 0
                                        newdetail.append(groceries_exp)                   #groceries_exp will be added to newdetail list
                                        upload_date = True                                #reassign the boolean value of upload_date to True   
                                        break                                             #the program will stop asking the user to input expired date
                                    
                                    else:                                                 #the date is invalid             
                                        print("The expired date is invalid.")             #the program will keep asking the user to input expired date
                                        upload_date = False
                                            
                            if (month % 2 == 0 and month<= 7 and month!=2) or (month % 2 != 0 and 7<month<13and month!=2):
                                                                                                     #to check if the month has 30 days
                                if 0 < day < 31:                                                     #check if the date is valid
                                    newdetail.append(groceries_exp)                                  #groceries_exp will be added to newdetail list
                                    upload_date = True                                               #reassign the boolean value of upload_date to True    
                                    break                                                            #the program will stop asking the user to input expired date
                                
                                else:                                                                #the date is invalid  
                                    print("The expired date is invalid.")                            #display text
                                    upload_date = False                                              #the program will keep asking the user to input expired date
                                    
                            elif (month % 2 != 0 and month<= 7 and month!=2) or (month % 2 == 0 and 7<month<13 and month!=2):
                                                                                                     # the left month have 31 days
                                if 0 < day < 32:                                                     # check if the date is valid  
                                    newdetail.append(groceries_exp)                                  #groceries_exp will be added to newdetail list 
                                    upload_date = True                                               #reassign the boolean value of upload_date to True 
                                    break                                                            #the program will stop asking the user to input expired date
                                
                                else:                                                                #the date is invalid                    
                                    print("The expired date is invalid.")                            #display text
                                    upload_date = False                                              #the program will keep asking the user to input expired date


        upload_spec = False                                           #assign the boolean value to upload_spec which is false                                                                    
        while not upload_spec:                                        #the program will keep asking the true format if the specification unable to upload.
            print("\nPlease enter the specification of",groceries_name) #display text
            groceries_specification = input("> ")                     #get the value of groceries_specification from user
            strip_spec = groceries_specification.strip()              #remove white space and new line of the groceries_specification and assign it to strip_spec
            if strip_spec == "":                                      #to check if the user leave it blank or click space only
                print("Please don't leave it blank.")                 #display text
                upload_spec = False                                   #the program will keep asking the user to input the value of groceries_specification
                
            else:                                                     #if the user does not leave it blamk
                newdetail.append(groceries_specification)             #groceries_specification will be added to newdetail list
                upload_spec = True                                    #reassign the boolean value of upload_spec to True 
                break                                                 #the program will stop asking the user to input the value of groceries_specification
            
        if category == medicine_detail:                               #to check if the value of category is medicine_detail
            medicine_detail.append(newdetail)                         #newdetail will be added to medicine_detail
            updategrocery_text("medicine.txt",medicine_detail)        #the content of medicine_detail will be updated to "medicine.txt"
            
        elif category == vege_detail:                                 #to check if the value of category is vege_detail
            vege_detail.append(newdetail)                             #newdetail will be added to vege_detail
            updategrocery_text("vegetable.txt",vege_detail)           #the content of vege_detail will be updated to "vegetable.txt"
            
        elif category == fruit_detail:                                #to check if the value of category is fruit_detail
            fruit_detail.append(newdetail)                            #newdetail will be added to fruit_detail
            updategrocery_text("fruit.txt",fruit_detail)              #the content of fruit_detail will be updated to "fruit.txt"
            
        elif category == dairy_detail:                                #to check if the value of category is dairy_detail
            dairy_detail.append(newdetail)                            #newdetail will be added to dairy_detail
            updategrocery_text("dairy.txt",dairy_detail)              #the content of dairy_detail will be updated to "dairy.txt"
            
        elif category == household_detail:                            #to check if the value of category is household_detail 
            household_detail.append(newdetail)                        #newdetail will be added to household_detail
            updategrocery_text("household.txt",household_detail)      #the content of household_detail will be updated to "household.txt"
            
        print(groceries_name, "successfully uploaded.")               #display text
        
        ans = False                                                   #assign the boolean value to ans which is false 
        while not ans:                                                #the program will keep asking the value of back if the input is invalid.
            back = input("\nType 'Y' to upload other grocery. Type 'N' to back to Admin Menu Page.\n>") #ask the user to enter 'Y' or 'N'
            if back == "Y":                                           #if the user enter 'Y'
                admin_upload()                                        #call admin_upload()
                ans = True                                            #reassign the boolean value to ans which is True
                break                                                 #the program will stop asking the value of back
            
            elif back == "N":                                         #if the user enter 'N'
                adminMenu()                                           #call adminMenu()
                ans = True                                            #reassign the boolean value to ans which is True
                break                                                 #the program will stop asking the value of back
            
            else:                                                     #if the user enter invaid input
                print("Invalid Input.")                               #display text
                                                                      #the program will keep asking the value of back
            


#to allow the admin to update grocery and its detail

#update/modify Groceries information if required            
def admin_update():
    number = False                                               #assign the false boolean value to number 
    while not number:                                            #the program will keep asking the user to enter the value of category
        print("\nPlease enter the category of grocery that requires update.\n") #display text
        try:                                                     #the block of code could be tested for errors using try block.
            category = int(input("\t\tType 1 - Medicine\n\t\tType 2 - Vegetable\n\t\tType 3 - Fruits\n\t\tType 4 - Dairy\n\t\tType 5 - Household\n>"))
                                                                 #the user could enter number only
            
            if category >= 1 and category <=5:                   #to check the user enter the number between 1 to 5
                number = True                                    #reassign the True boolean value to number 
                break                                            #the program will stop asking the value of category
            
            else:                                                #to check the user enter the number out of range
                print("The number is out of range.\n")           #display text
                number = False                                   #the program will keep asking the value of category
                
        except:                                                  #the program will not display red code if the user enter words
            print("Invalid Input. Please enter a number.\n")     #display text
            number = False                                       #the program will keep asking the value of category
            
    if category == 1:                                            #if the user enter 1
        category = medicine_detail                               #reassign the medicine_detail to the value of category
        viewcategory(1)
    elif category == 2:                                          #if the user enter 2
        category = vege_detail                                   #reassign the vege_detail to the value of category
        viewcategory(2)
    elif category == 3:                                          #if the user enter 3
        category = fruit_detail                                  #reassign the fruit_detail to the value of category
        viewcategory(3)
    elif category == 4:                                          #if the user enter 4
        category = dairy_detail                                  #reassign the dairy_detail to the value of category
        viewcategory(4)
    elif category == 5:                                          #if the user enter 5
        category = household_detail                              #reassign the household_detail to the value of category
        viewcategory(5)
        
    name = False                                                 #assign the False boolean value to name 
    update = False                                               #assign the False boolean value to update 
    need_to_update = "no"                                        #assign "no" to the value of need_to_update
    
    while not name:                                              #the program will keep asking the user to input groceries_name if the user's input is invalid
        groceries_name = input("\nPlease enter the name of grocery that requires update. \n*Press'x' to back to Admin Main Page.*\n>")
                                                                 #store the user's input in groceries_name

        stripped_groceries_name = groceries_name.strip()         
        if stripped_groceries_name == "":                        #if the user leave it blank or click space only
            print("Please don't leave it blank.")                #display text
            name = False                                         #the program will ask the user to input groceries_name again
        
        elif groceries_name == "x":                              #to check if user enter "x"
            adminMenu()                                          #back to Admin Menu page
            name = True                                          #reassign the True boolean value to name
            break                                                #the program will stop asking the user to input groceries_name

        else:
            for i in category:                                       #i is each list in category. Category is the list contain i lists.
                                                                     #For loop is to iterate through each i in category
                if i[0] == groceries_name[0].upper()+ groceries_name[1:].lower(): #if the grocery name exist in the category
                    groceries_name = groceries_name[0].upper()+ groceries_name[1:].lower()
                    need_to_update = i                               #assign the value of i into need_to_update variable
                    break                                            #the iteration through the following i in category will stop
                
            if need_to_update != "no":                               #if the value of need_to_update reassigned with the user's input
                name = True                                          #reassign the True boolean value to name
                update = True                                        #reassign the True boolean value to update
                break                                                #the program will stop asking the user to input groceries_name
            
            else:                                                    #if the grocery name is not exist in the category
                name = False                                         #the program will keep asking the user to input groceries_name
                print (groceries_name, "not found. Please try again.") #display text

    if update:                                                   #if the value of need_to_update reassigned with the user's input
        update_name = False                                      #assign the False boolean value to update_name
        updated_price = False                                    #assign the False boolean value to update_price
        updated_date = False                                     #assign the False boolean value to update_date
        updated_spec = False                                     #assign the False boolean value to update_spec
        
        while not update_name:                                   #the program will keep asking the user to input new_name if the user's input is invalid
            print("\nPlease enter the new name of",groceries_name,". \nType 'x' to keep the same name of", groceries_name)
                                                                 #display text
            new_name = str(input(">"))                           #the user's input will be converted to string
            
            strip_new_name = new_name.strip()                    #eliminate any whitespace from the new_name's beginning and end 
            if strip_new_name == "":                             #if the user leave it blank or click space only
                print("Please don't leave it blank.")            #display text
                update_name = False                              #the program will ask the user to input new_name again
                
            elif new_name == "x":                                #if the user enter "x"
                update_name = True                               #reassign the True boolean value to update_name
                break                                            #the program will not ask the user to input new_name again
            else:
                new_name = new_name[0].upper()+ new_name[1:].lower()
                if new_name != need_to_update[0]:                #if the user's input is different with the first element of need_to_update list
                        need_to_update[0] = new_name            #the user's input will replace the first element of need_to_update list
                        print("Successfully updated.\n")         #display text
                        update_name = True                       #reassign the True boolean value to update_name
                        break                                    #the program will not ask the user to input new_name again
                    
                else:                                                #if the user's input is same with the first element of need_to_update list
                    print("This new name is same as before.\n")      #display text
                    update_name = True                               #reassign the True boolean value to update_name
                    break                                            #the program will not ask the user to input new_name again
                
        while not updated_price:                                 #the program will keep asking the user to input new_price if the user's input is invalid
            print("\nPlease enter the new price of",groceries_name,". \nType 'x' to keep the same price of", groceries_name)
                                                                 #display text
            new_price = input("> RM")                            #store the user's input in new_price
            strip_new_price = new_price.strip()                  #eliminate any whitespace from the new_price's beginning and end
            
            if strip_new_price == "":                            #if the user leave it blank or click space only
                print("Please don't leave it blank.")            #display text
                updated_price = False                            #the program will ask the user to input new_price again
                
            elif new_price == "x":                               #if the user enter "x"
                updated_price = True                             #the program will not ask the user to input new_price again
                
            else:                                                #if the user not leave it blank or enter "x"
                isfloat = False                                  #assign the False boolean value to isfloat
                try:                                             #the block of code could be tested for errors using try block.
                    new_price = float(new_price)                 #the user can enter number only
                    isfloat = True                               #reassign the True boolean value to isfloat
                    
                except:                                          #the program will not display red code if the user enter words
                    print("Please enter number.")                #display text
                    isfloat = False                              #the program will ask the user to input new_price again
                    
                if isfloat:                                      #if the user enter number
                    new_price = twodecimal(new_price)            #convert the format of new_price to XX.XX
                    RM_new_price = "RM" + new_price              #become RMXX.XX
                    if RM_new_price == need_to_update[1]:        #if the price is same as the second element of need_to_update
                        print("This new price is same as before.\n") #display text
                        
                    else:                                        #if the price is not same as the second element of need_to_update
                        need_to_update[1] = RM_new_price         #replace the second element of need_to_update with user's input     
                        print("Successfully updated.\n")         #display text
                    updated_price = True                         #reassign the True boolean value to updated_price
                    break                                        #the program will not ask the user to input new_price again

        while not updated_date:                                  #the program will keep asking the user to input new_date if the user's input is invalid
            print("\nPlease enter the new expired date of",groceries_name,". (DD/MM/YYYY)\nType 'x' to keep the same expired date of", groceries_name)
                                                                 #print text
            new_date = str(input(">"))                           #store the input from user as a string
            strip_new_date = new_date.strip()                    #eliminate any whitespace from the new_date's beginning and end
            
            if strip_new_date == "":                             #if the user leave it blank or click space only
                print("Please don't leave it blank.")            #display text
                updated_date = False                             #the program will ask the user to input new_date again
                
            elif new_date == "x":                                #if the user enter"x"
                updated_date = True                              #reassign the True boolean value to updated_date
                break                                            #the program will not ask the user to input new_date again
            
            elif new_date != need_to_update[2]:                  #if the user's input is not same with the original date
                formattrue = False                               #assign False boolean value to formattrue
                while not formattrue:                            #the program will keep asking the user to input true format of new_date
                    
                    try:                                         #the block of code could be tested for errors using try block
                        day, month, year = new_date.split("/")   #split the value of new_date by "/" and assign the value to day, month, year accordingly
                        formattrue = True                        #the program will not ask the user to input  true format of new_date again
                        break 
                    except:                                      #the program will not display red code if the new_date can't split
                        new_date = input("\nPlease enter the true format which is DD/MM/YYYY.\n>")
                                                                 #the program will ask the user to input true format of new_date again
                        formattrue = False
                        
                if len(day)>2 or len(month)>2 or len(year)!= 4 : #to check if the date or month is more than 2 digits, or the year is not 4 digits. 
                    print("The expired date is invalid.")        #display text    
                    updated_date = False                         #the program will ask the user to input new_date again
                    
                else:                                            #if the number of digits for day, month, year is true
                    num = True                                   #assign True Boolean valud to num
                    
                    try:                                         #the block of code could be tested for errors using try block
                        day = int(day)                           #test if the user input number only
                        month = int(month)
                        year = int(year)
                    except:                                      #the program will not display red code if the user's input is not number
                        print("The expired date is invalid. Please enter number.") #display text
                        updated_date = False                     #the program will ask the user to input new_date again
                        num = False                              #reassign False Boolean value to num
                        
                    if num:                                      #if the user input number only
                        
                        if month > 12 or month < 0:              #one year has 12 month only
                            print("The expired date is invalid.")#display text
                            updated_date = False                 #the program will ask the user to input new_date again
                            
                        else:                                    #if the user's input is from 1 - 12
                            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #to check it is a leap year or not
                                if month == 2:                   #in leap year, february has 29 days
                                    if day<0 or day> 29:         #if the day is out of range
                                        print("The expired date is invalid.")#display text
                                        updated_date = False     #the program will ask the user to input new_date again
                                        
                                    else:                        #if the day is from 1 - 29
                                        need_to_update[2] = new_date #update the new_date to the list
                                        print("Successfully updated.\n")#display text
                                        updated_date = True      #the program will not ask the user to input new_date again
                                        break
                            else:                             
                                if month == 2:                     #this is not the leap year
                                    if day>0 and day<= 28:           #if the year is not the leap year, february has 28 days only
                                        need_to_update[2] = new_date #update the new_date to the list
                                        print("Successfully updated.\n")   #display text
                                        updated_date = True          #the program will not ask the user to input new_date again
                                        break
                                    
                                    else:                            #if the day is out of range
                                        print("The expired date is invalid.") #display text
                                        updated_date = False         #the program will ask the user to input new_date again
                                        
                            if (month % 2 == 0 and month<= 7 and month!=2) or (month % 2 != 0 and 7<month<13 and month!=2):
                                                                          # to check if the month has 30 days
                                if 0 < day < 31:                          #if the day is from 1 - 30
                                    need_to_update[2] = new_date          #update the new_date to the list
                                    print("Successfully updated.\n")      #display text
                                    updated_date = True                   #the program will not ask the user to input new_date again
                                    break
                                
                                else:                                     #if the day is out of range
                                    print("The expired date is invalid.") #display text
                                    updated_date = False                  #the program will ask the user to input new_date again
                                    
                            elif (month % 2 != 0 and month<= 7 and month!=2) or (month % 2 == 0 and 7<month<13 and month!=2 ):
                                                                          # the left month have 31 days
                                if 0 < day < 32:                          #if the day is from 1 - 31
                                    need_to_update[2] = new_date          #update the new_date to the list
                                    print("Successfully updated.\n")      #display text
                                    updated_date = True                   #the program will not ask the user to input new_date again
                                    break
                                
                                else:                                     #if the day is out of range
                                    print("The expired date is invalid.") #display text
                                    updated_date = False                  #the program will ask the user to input new_date again
                    
            else:                                                         #if the date is same as the original date
                print("This new expired date is same as before.\n")       #display text       
                updated_date = True                                       #the program will not ask the user to input new_date again
                break
            
        while not updated_spec:                                  #the program will keep asking the user to input new_spec if the user's input is invalid
            print("\nPlease enter the new specification of",groceries_name,". \nType 'x' to keep the same specification of", groceries_name)
                                                                 #display text
            new_spec = str(input(">"))                           #store the user's input as string
            strip_new_spec = new_spec.strip()                    #eliminate any whitespace from the new_spec's beginning and end
            if strip_new_spec == "":                             #if the user leave it blank or click space only
                print("Please don't leave it blank.")            #display text
                updated_spec = False                             #the program will ask the user to input new_spec again
                
            elif new_spec == "x":                                #if the user enter "x"
                updated_spec = True                              #the program will not ask the user to input new_spec again
                break
            
            elif new_spec != need_to_update[3]:                  #if the new_spec is different with the original specification
                need_to_update[3] = new_spec                     #update the new_spec to the list
                print("Successfully updated.\n")                 #display text
                updated_spec = True                              #the program will not ask the user to input new_spec again
                break
            
            else:                                                #if the new_spec is same with the original specification
                print("This new spefication is same as before.\n") #display text
                updated_spec = True                              #the program will not ask the user to input new_spec again
                break
            
        if category == medicine_detail:                          #if value of cateogory is medicine_detail
            updategrocery_text("medicine.txt",medicine_detail)   #call updategrocery_text and input 2 parameters.
        elif category == vege_detail:                            #if value of cateogory is vege_detail
            updategrocery_text("vegetable.txt",vege_detail)      #call updategrocery_text and input 2 parameters.
        elif category == fruit_detail:                           #if value of cateogory is fruit_detail
            updategrocery_text("fruit.txt",fruit_detail)         #call updategrocery_text and input 2 parameters.
        elif category == dairy_detail:                           #if value of cateogory is dairy_detail
            updategrocery_text("dairy.txt",dairy_detail)         #call updategrocery_text and input 2 parameters.
        elif category == household_detail:                       #if value of cateogory is household_detail
            updategrocery_text("household.txt",household_detail) #call updategrocery_text and input 2 parameters.
        print("\nYou had reached the end of updating the information of",groceries_name,".") #display text
   
        YN = False                                               #set False Boolean value to YN
        while not YN:                                            #the program will keep asking the user to input newupdate if the user's input is invalid
            newupdate = input("\n\nType 'Y' to update other grocery information. Type 'N' to back to Admin Menu Page.\n>") #ask the user and get input
            if newupdate == "Y":                                 #if the user enter "Y"
                admin_update()                                   #call admin_update()
                YN = True                                        #the program will not ask the user to input newupdate again
                break
            elif newupdate == "N":                               #if the user enter "N"
                adminMenu()                                      #call adminMenu()
                YN = True                                        #the program will not ask the user to input newupdate again
                break
            else:                                                #if the user does not enter "Y" or "N"              
                print("Invalid Input")                           #display text
                YN = False                                       #the program will ask the user to input newupdate again



#delete Groceries information                
def admin_delete():
    number = False                                               #set False boolean value to number
    while not number:                                            #the program will keep asking the user to input category if the user's input is invalid
        print("\nPlease enter the category of grocery that needs to be deleted.\n") #display text
        try:                                                     #the block of code could be tested for errors using try block
            category = int(input("\t\tType 1 - Medicine\n\t\tType 2 - Vegetable\n\t\tType 3 - Fruits\n\t\tType 4 - Dairy\n\t\tType 5 - Household\n>"))
                                                                 #the user should enter number only
            if category >= 1 and category <=5:                   #if the user enter number from 1 - 5
                number = True                                    #the program will not ask the user to input category again
                break
            else:                                                #if the user enter number out of range (1-5)
                print("The number is out of range.\n")           #display text
                number = False                                   #the program will ask the user to input category again
                
        except:                                                  #the program will not display red code if the user enter words
            print("Invalid Input. Please enter a number.\n")     #display text
            number = False                                       #the program will ask the user to input category again
            
    if category == 1:                                            #if the user enter 1
        category = medicine_detail                               #assign medicine_detail to the value of category
        viewcategory(1)
    elif category == 2:                                          #if the user enter 2
        category = vege_detail                                   #assign vege_detail to the value of category
        viewcategory(2)
    elif category == 3:                                          #if the user enter 3
        category = fruit_detail                                  #assign fruit_detail to the value of category
        viewcategory(3)
    elif category == 4:                                          #if the user enter 4
        category = dairy_detail                                  #assign dairy_detail to the value of category
        viewcategory(4)
    elif category == 5:                                          #if the user enter 5
        category = household_detail                              #assign household_detail to the value of category
        viewcategory(5)
        
    name = False                                                 #assign False Boolean value to name
    delete = False                                               #assign False Boolean value to delete
    need_to_delete = "no"                                        #assign "no" to the value of need_to_delete
    
    while not name:                                              #the program will keep asking user to input groceries_name if the user's input is invalid
        groceries_name = input("\nPlease enter the name of grocery that needs to be deleted. \n*Press'x' to back to Admin Main Page.*\n>")
                                                                 #display text
        strip_groceries_name  = groceries_name.strip()             
        if strip_groceries_name == "":                           #if the user leave it blank or enter space only
            print("Please don't leave it blank.")                #display text
            name = False                                         #the program will ask the user to input groceries_name again
            
        elif groceries_name == "x":                              #if user enter "x"
            adminMenu()                                          #call adminMenu()
            name = True                                          #the program will not ask the user to input category again
            break
        else:
            for d in category:                                       #d is the lists in category.category is a list contain d lists.
                                                                     #iterate through each d in cateogry.
                if d[0] == groceries_name[0].upper()+ groceries_name[1:].lower(): #if the first element of d is euqal to the user's input
                    groceries_name = groceries_name[0].upper()+ groceries_name[1:].lower() #to ensure the first letter of grocery is capital letter.
                    need_to_delete = d                               #assign d to the value of need_to_delete
                    break                                            
            if need_to_delete != "no":                               #if d(groceries_name) is already assigned to the value of need_to_delete
                name = True                                          #the program will not ask the user to input groceries_name again
                delete = True                                        #reassign True boolean value to delete
                break
            else:                                                    #if d (groceries_name) is not assigned to the value of need_to_delete
                name = False                                         #the program will ask the user to input groceries_name again
                print (groceries_name, "not found. Please try again.") #display text
    

    if delete:                                                   #if d (groceries_name) is already assigned to the value of need_to_delete
        category.remove(need_to_delete)                          #remove d (groceries_name) from category list
        print("\nAll the information of",groceries_name,"has been successfully deleted.") #display text
        if category == medicine_detail:                          #if the value of category is medicine_detail
            updategrocery_text("medicine.txt",medicine_detail)   #call updategrocery_text and input 2 parameters.
        elif category == vege_detail:                            #if the value of category is vege_detail
            updategrocery_text("vegetable.txt",vege_detail)      #call updategrocery_text and input 2 parameters.
        elif category == fruit_detail:                           #if the value of category is fruit_detail
            updategrocery_text("fruit.txt",fruit_detail)         #call updategrocery_text and input 2 parameters.
        elif category == dairy_detail:                           #if the value of category is dairy_detail
            updategrocery_text("dairy.txt",dairy_detail)         #call updategrocery_text and input 2 parameters.
        elif category == household_detail:                       #if the value of category is household_detail
            updategrocery_text("household.txt",household_detail) #call updategrocery_text and input 2 parameters.
            
        YN = False                                               #assign False boolean value to YN
        while not YN:                                            #the program will keep asking user to input newdelete if the user's input is invalid
            newdelete = input("\n\nType 'Y' to delete other grocery information. Type 'N' to back to Admin Menu Page.\n>")
                                                                 #ask the user to input newdelete
            
            if newdelete == "Y":                                 #if the user enter "Y"
                admin_delete()                                   #call admin_delete()
                YN = True                                        #the program will not ask the user to input newdelete again
                break
            elif newdelete == "N":                               #if the user enter "N"
                adminMenu()                                      #call adminMenu()
                YN = True                                        #the program will not ask the user to input newdelete again
                break
            else:                                                #if the user does not enter "Y" or "N"
                print("Invalid Input")                           #display text
                YN = False                                       #the program will ask the user to input newdelete again



#seach specific Groceries detail                
def admin_search():
    number = False                                               #assign False Boolean value to number
    while not number:                                            #the program will keep asking user to input number if the user's input is invalid
        print("\nPlease enter the category of grocery that you want to search.\n") #display text
        try:                                                     #the block of code could be tested for errors using try block
            category = int(input("\t\tType 1 - Medicine\n\t\tType 2 - Vegetable\n\t\tType 3 - Fruits\n\t\tType 4 - Dairy\n\t\tType 5 - Household\n>"))
                                                                 #the user should enter number
            if category >= 1 and category <=5:                   #if the user enter number from 1 to 5
                number = True                                    #the program will not ask the user to input category again
                break
            else:                                                #if the user enter number out of range (1-5)
                print("The number is out of range.\n")           #display text
                number = False                                   #the program will ask the user to input category again
                
        except:                                                  #will not display code if the user enter words
            print("Invalid Input. Please enter a number.\n")     #display text
            number = False                                       #the program will ask the user to input category again
            
    if category == 1:                                            #if the user enter 1
        category = medicine_detail                               #assign medicine_detail to the value of category
    elif category == 2:                                          #if the user enter 2
        category = vege_detail                                   #assign vege_detail to the value of category
    elif category == 3:                                          #if the user enter 3
        category = fruit_detail                                  #assign fruit_detail to the value of category
    elif category == 4:                                          #if the user enter 4
        category = dairy_detail                                  #assign dairy_detail to the value of category
    elif category == 5:                                          #if the user enter 5
        category = household_detail                              #assign household_detail to the value of category
        
    name = False                                                 #assign False boolean value to False
    need_to_search = "no"                                        #assign "no" to need_to_search
    
    while not name:                                              #the program will keep asking user to input groceries_name if the user's input is invalid
        adminmenu = False
        groceries_name = input("\nPlease enter the name of grocery that you want to search. \n*Type'x' to back to Admin Main Page.*\n>")
                                                                 #ask the user to input groceries_name
        strip_name = groceries_name.strip()                      #eliminate any whitespace from the strip_name's beginning and end
        
        if strip_name == "":                                     #if the user leave it blank or click space only
            print("Please don't leave it blank.")                #display text
            name = False                                         #the program will ask the user to input groceries_name again
            
        elif groceries_name == "x":                              #if the user enter "x"
            adminMenu()                                          #call adminMenu()
            name = True                                          #the program will not ask the user to input groceries_name again
            adminmenu = True
            break
        else:                                                    #if the user enter a valid name
            for item in category:                                #iterate through each item in category
                if item[0] == groceries_name[0].upper()+ groceries_name[1:].lower(): #if the first element of item is equal to the user's input
                    need_to_search = item                        #the item is assign to the value of need_to_search
                    break                                        #the iteration through each item in category will stop
                
            if need_to_search != "no":                           #if need_to_search is not equal to "no" which is initially assigned
                name = True                                      #reassign True boolean value to name
                break                                            #escape from While not name loop
            
            else:                                                #if need_to_search is equal to "no" which is initially assigned
                name = False                                     #the value of name remained same
                print (groceries_name, "not found. Please try again.")  #display text

    if not adminmenu:                                            #to filter the "x" input from user
        print("\nName:",need_to_search[0],"\nPrice:",need_to_search[1],"\nExpired Date:",need_to_search[2],"\nDetails:",need_to_search[3])
                                                                 #display text
        ans = False                                              #assign True Boolean value to False
        while not ans:                                           #the program will keep asking user to input back if the user's input is invalid
            back = input("\nType 'Y' to search other grocery. Type 'N' to back to Admin Menu Page.\n>") #ask the user to input back
            if back == "Y":                                      #if the user enter "Y"
                admin_search()                                   #call admin_search() function
                ans = True                                       #reassign True boolean value to ans
                break                                            #the program will not ask the user to input back again
            
            elif back == "N":                                    #if the user enter "N"
                adminMenu()                                      #call adminMenu()function
                ans = True                                       #set ans = True
                break                                            #the program will not ask the user to input back again
            
            else:                                                #if the user does not enter "Y" or "N"
                print("Invalid Input.")                          #display text



#view all customer orders            
def adminview_allorder():
    registered_list = update_orderlist()                         #Call update_orderlist() and assign to registered_list
    view = False                                                 #assign False Boolean value to view
    print("\nView order: \n\n")                                  #display text
    for list in registered_list:                                 #iterate through each list in registered_list
        print(" Username: ",list[0], "\n",                       #display text
                "Grocery: ",list[1],"\n",
                "Price Per Quantity: ",list[2],"\n",
                "Quantity: ",list[3], "\n"
                "Total Price: ",list[4],"\n")
    ans = False                                                  #assign False Boolean value to ans
    while not ans:                                               #the program will keep asking user to input ans if the user's input is invalid
        back = input("\nType 'N' to back to Admin Menu Page.\n>")#ask the user to input back
        if back == "N":                                          #if the user enter "N"
            adminMenu()                                          #call adminMenu()
            ans = True                                           #reassign True boolean value to ans
            break                                                #the program will not ask the user to input back again
        
        else:                                                    #if the user enter invalid value to back
            print("Invalid Input.")                              #display text
            


#search specific customer order            
def adminsearch_order():
    registered_list = update_orderlist()                         #Call update_orderlist() and assign to registered_list
    valid_name = False                                           #set False boolean value to valid_name
    while not valid_name:                                        #the program will keep asking user to input valid_name if the user's input is invalid
        username = input("\nPlease enter the username. ")        #ask the user to input username
        strip_username = username.strip()                        #set strip_username = username.strip()
        if strip_username == "":                                 #if the user leave it blank or click space only
            print("Please don't leave it blank.")                #display text, the program will ask the user to input username again
            
        else:                                                    #if the user not leave it blank
            valid_name = True                                    #assign True boolean value to valid_name
            break                                                #the program will not ask the user to input username again
        
    view = False                                                 #assign False boolean value to view
    print(f"\nView {username}'s order: \n")                      #display text
    for list in registered_list:                                 #iterate through each list in registered_list
        if list[0] == username:                                  #if the user's input is same with the first element of list
            print(" Username: ",list[0], "\n",                   #display text, the program will ask the user to input username again
                      "Grocery: ",list[1],"\n",
                      "Price Per Quantity: ",list[2],"\n",
                      "Quantity: ",list[3], "\n"
                      " Total Price: ",list[4],"\n")
            view = True                                          #reassign True boolean value to view
    if not view:                                                 #if the user's input is not same with the first element of list
        print(username, "don't have any order.")                 #display text
        
    ans = False                                                  #assign False boolean value to ans
    
    while not ans:                                               #the program will keep asking user to input valid_name if the user's input is invalid
        back = input("\nType 'Y' to search other order. Type 'N' to back to Admin Menu Page.\n>") #ask the user to input back
        if back == "Y":                                          #if the user enter "Y"
            adminsearch_order()                                  #call adminsearch_order()
            ans = True                                           #set True boolean value to ans
            break                                                #the program will not ask the user to input back again
        
        elif back == "N":                                        #if the user enter "N"
            adminMenu()                                          #call adminMenu()
            ans = True                                           #assign True boolean value to ans
            break                                                #the program will not ask the user to input back again
        
        else:                                                    #if the user enter invalid value to back
            print("Invalid Input.")                              #display text, the program will ask the user to input back again
        
        
#Admin Menu Page
def adminMenu():
    print("\nWelcome to Groceries Management System Admin Menu Page!\n")  #display text
    invalid = True                                                        #set True boolean value to Invalid
    while invalid:                                               #the program will keep asking user to input menu_num if the user's input is invalid
        in_num_range = False
        
        print('''\tType 1 to upload groceries detail in system.            
        Type 2 to view all uploaded groceries.
        Type 3 to update or modify groceries information.
        Type 4 to delete groceries info.
        Type 5 to search groceries detail.
        Type 6 to view all customer orders.
        Type 7 to search specific customer order.
        Type 8 to exit Groceries Management System Admin Menu Page.''')  #display text
        menu_num  = input(">")                                           #ask the user to input menu_num
        
        strip_menu_num = menu_num.strip()                                #eliminate any whitespace from the menu_num's beginning and end.
        if strip_menu_num == "":                                         #if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
            invalid = True                                               #assign True boolean value to invalid
                                                                         #the program will ask the user to input menu_num again
            
        try:                                                             #the block of code could be tested for errors using try block                                                 
            menu_num = int(menu_num)                                     #the user can enter integer only
            if menu_num>0 and menu_num<9:                                #if menu_num is greater than 0 and smaller than 9
                in_num_range = True                                      #assign True boolean value to in_num_range
                
            else:                                                        #if menu_num is smaller than 0 and greater than 9
                print("Please enter a valid number.")                    #display text
                invalid = True                                           #assign True boolean value to invalid
                                                                         #the program will ask the user to input menu_num again
                
        except:                                                          #will not display code if the user enter words                                                       
            print("Please enter number.")                                #display text                    
            invalid = True                                               #assign True boolean value to invalid
                                                                         #the program will ask the user to input menu_num again
            
        if in_num_range:                                                 #if the user enters the number in range 1-8
            if menu_num == 1:                                            #if user enters 1
                admin_upload()                                           #call admin_upload() 
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 2:                                          #if user enters 2
                viewgrocery()                                            #call viewgrocery()
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 3:                                          #if user enters 3
                admin_update()                                           #call admin_update()
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 4:                                          #if user enters 4
                admin_delete()                                           #call admin_delete()
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 5:                                          #if user enters 5
                admin_search()                                           #call admin_search()
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 6:                                          #if user enters 6
                adminview_allorder()                                     #call adminview_allorder() 
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 7:                                          #if user enters 7
                adminsearch_order()                                      #call adminsearch_order() 
                invalid = False                                          #the program will not ask the user to input menu_num again
                
            elif menu_num == 8:                                          #if user enters 8
                menu()                                                   #call menu() 
                invalid = False                                          #the program will not ask the user to input menu_num again


        
#Admin Login Page -check Admin's password                
def admincheck(textusername, textpassword):                              
    
    password = input("Please enter your password: ")                     #ask the user to input password
    if password == textpassword:                                         #if the user's input is equal to textpassword
        print("\nLogin Success! You could access to Admin Menu Page now.\n") #display text
        adminMenu()                                                      #call adminMenu() 
    else:                                                                #if the user's input is not equal to textpassword
        for i in range(4):                                               #repeat 4 times
            checkfailed = True                                           #assign True Boolean value to checkfailed
            password = input("Wrong Password. Please try again.\n\nPlease enter your password: ") #ask the user to input password
            if password == textpassword:                                 #if the user's input is equal to textpassword
                print("\nLogin Success! You could access to Admin Menu Page now.\n")#display text
                adminMenu()                                              #call adminMenu()
                
                checkfailed = False                                      #set False boolean value to checkfailed
                break                                                    #the program will not ask the user to input password again
            
            else:
                checkfailed = True                                       #set True boolean value to checkfailed
        if checkfailed:                                                  #if user does not input the true password for 4 times
            checkrepeat = True                                           #assign True Boolean value to checkrepeat
            print("Wrong Password.\n\nOops! You've reached the maximum password attempt.\n")#display text
            while checkrepeat:                                           #the program will keep asking user to input select if the user's input is invalid
                select = input('''
              Type 1 to back to Menu Page. \n
              Type 2 to proceed to Forgot Password Page. \n''')          #ask the user to input select
                if select == "1":                                        #if the user enters 1
                    menu()                                               #call menu()
                    checkrepeat = False                                  #reassign False boolean value to checkrepeat
                    
                elif select == "2":                                      #if the user enters 2
                    print("Forgot your password? Let us help you!")      #display text
                    security = open("Adminsecurity.txt", "r")            #open the text file as read mode and assign the value to security
                    for text in security:                                #iterating through each text in security
                        if text.startswith(textusername):                #if text starts with the user's username
                            username, security = text.split("|")#split text with "|" and assign to admin_username, admin_security accordingly
                            username = username.strip()                  #eliminate any whitespace from the admin_username's beginning and end.
                            security = security.strip()                  #eliminate any whitespace from the admin_security's beginning and end.
                            if username == textusername:
                                admin_username = username
                                admin_security = security
                            
                    ask = True                                           #set True boolean value to ask
                    attempts = 3                                         #set 3 to the value of attempts
                    for i in range(attempts):                            #repeat for 3 times
                        admin_ans = input("Please enter your favourite colour (you set it in the profile of this system before): ")
                                                                         #ask the user to input admin_ans
                        if admin_ans == admin_security:                  #if the user's input is same with admin_security
                            print("\nCorrect Answer! You can now change the password.\n") #display text
                            print("\nYour new password: ")
                            print("- must be 8-30 characters \n-don't include '|' in your password.\n")
                            password_valid = False                       #assign False boolean value to password_valid
                            while not password_valid:               #the program will keep asking user to input admin_newpass if the user's input is invalid
                                admin_newpass = input("Please enter your password: ") #ask the user to input admin_newpass
                                if len(admin_newpass) < 8:               #the user needs to enter the password which is more than 8 characters
                                    print("Your password is not strong enough. Please make sure your password has 8-30 characters.\n")
                                elif len(admin_newpass)>30:              #the user needs to enter the password which is less than 30 characters
                                    print("Your password is too lengthy. Please make sure your password has 8-30 characters only.\n")
                                elif "|" in admin_newpass:               # the user could not include "|" in their password
                                    print("Your password is invalid. Please don't include '|' in your password.")
                                else:                                    #check if the user enter the password that meets all requirements
                                    password_valid = True                #reassign True boolean value to password_valid  
                                    break                                #the program will not ask the user to input admin_newpass again

                            admin_rewrite = True                         #assign True boolean value to admin_rewrite
                            while admin_rewrite:                         #the program will keep asking user to input admin_rewrite if the user's input is invalid
                                admin_reenter = input("Please reenter the new password.")#ask the user to input admin_reenter
                                if admin_newpass == admin_reenter:       #if the user reenter the same password
                                    admin_rewrite = False                #the program will not ask the user to input admin_reenter again
                                    break
                                else:                                    #if the user reenter the different password
                                    print("\nPassword does not match.")  #display text
                                    admin_rewrite = True                 #the program will ask the user to input admin_reenter again
                                    
                            print("\nYou have successfully changed the password! We will bring you back to Admin login page again!\n") #display text
                            resetpassword("Adminlogin.txt",textpassword,admin_newpass)  #call reset function and include 3 parameters
                            changed = True                                              #assign True boolean value to changed
                            admin()                                                     #call admin
                            break
                        else:
                            attempts = attempts - 1                                 #the attempts will deduct by 1 if the user enter wrong security answer
                            print("Your answer is wrong.",attempts,"attempts left.")#display text
                            changed = False                                         #assign False boolean value to changed
                    if not changed:                                                 #if the password has not been changed
                        print("\nSorry. To ensure the privacy, you are not able to change the password. We will bring you back to Menu Page.\n")
                                                                                    #display text
                        menu()                                                      #call menu()
                    checkrepeat = False                                             #assign False boolean value to checkrepeat 
                    break                                                           #the program will not ask the user to input select again
                else:                                                               #if the user didn't enter 1 or 2 for select
                    print("Invalid Input")                                          #display text, the program will ask the user to input select again



        
#Admin Login Page - Check Admin's Username                   
def adminlogin(username):
    admintext = open("Adminlogin.txt", "r")                             #the text had been open with read mode and assign the value to admintext
    for text in admintext:                                              #iterate each text in admintext
        if text.startswith(username):                                   #if text starts with user's username 
            admintext_username,admintext_password = text.split("|")     #split text by "|" and assign the value to admintext_username,admintext_password                  
            admintext_username = admintext_username.strip()             #eliminate any whitespace from the admintext_username's beginning and end.
            admintext_password = admintext_password.strip()             #eliminate any whitespace from the admintext_password's beginning and end.
            if username == admintext_username:                          #if the textfile has the username
                admincheck(admintext_username, admintext_password)      #call admincheck and assign two parameters
                true_username = True                                    #assign True boolean value to true_username
                break                                                   #the for loop will stop looping
            else:                                                       #if the textfile does not have the username
                true_username = False                                   #assign False boolean value to true_username
        else:                                                           #if the textfile does not have the username
            true_username = False                                       #assign False boolean value to true_username
            
    if not true_username:                                               #if the textfile does not have the username
        print(username, "not found. Please try again.\n")               #display text
        admin()                                                         #call admin()
                    

            

    
#New Customer Menu Page    
def newCustomerMenu():
    print("\nWelcome to Groceries Management System New Customer Page!\n")#display text
    invalid = True                                                        #assign True boolean value to true_invalid
    while invalid:                                                        #keep asking user to input menu_num if the user's input is invalid
        print('''\tType 1 to view all groceries detail in system.
        Type 2 to create new account.
        Type 3 to exit Groceries Management System New Customer Page.''') #display text
        menu_num  = input(">")                                           #ask user to input menu_num
        if menu_num == "1":                                              #if user enter "1"
            new_viewdetail()                                             #call new_viewdetail() 
            invalid = False                                              #the program will not ask the user to input menu_num again
            
        elif menu_num == "2":                                            #if user enter "2"
            createaccount()                                              #call createaccount()
            invalid = False                                              #the program will not ask the user to input menu_num again
            
        elif menu_num == "3":                                            #if user enter "3"
            menu()                                                       #call menu()
            invalid = False                                              #the program will not ask the user to input menu_num again
            
        else:                                                            #if user enter the number out of 1,2,3
            print("Invalid Input. Please enter number.")                 #display text, the program will ask the user to input menu_num again

#new customer registration    
def createaccount():
    valid_name = False                                                   #assign False boolean value to valid_name
    while not valid_name:                                                #keep asking user to input name if the user's input is invalid
        name = input("\nPlease enter your name: ")                       #ask the user to input name
        strip_name = name.strip()                                        #eliminate any whitespace from the name's beginning and end.
        if strip_name == "":                                             #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
        else:                                                            #if the user does not leave it blank
            name = name.lstrip()                                         #lstrip() eliminate whitespace from the name's beginning.
            valid_name = True                                            #the program will not ask the user to input name again

    valid_address = False                                                #assign False boolean value to valid_address
    while not valid_address:                                             #keep asking user to input address if the user's input is invalid
        address = input("\nPlease enter your address: ")                 #ask the user to input address
        strip_address = address.strip()                                  #eliminate any whitespace from the address's beginning and end.
        if strip_address == "":                                          #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
        else:                                                            #if the user does not leave it blank
            valid_address = True                                         #the program will not ask the user to input address again

    valid_email = False                                                  #assign False boolean value to valid_email
    while not valid_email:                                               #keep asking user to input email if the user's input is invalid
        email = input("\nPlease enter your Email ID: ")                  #ask the user to input email
        strip_email = email.strip()                                      #eliminate any whitespace from the email's beginning and end.
        if strip_email == "":                                            #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
        else:                                                            #if the user does not leave it blank
            valid_email = True                                           #the program will not ask the user to input email again


    valid_contact = False                                                #assign False boolean value to valid_contact
    while not valid_contact:                                             #keep asking user to input contact if the user's input is invalid
        contact = input("\nPlease enter your contact number without space or dash: ")#ask the user to input contact
        strip_contact = contact.strip()                                  #eliminate any whitespace from the contact's beginning and end.
        if strip_contact == "":                                          #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
            valid_contact = False                                        #the program will ask the user to input contact again
                                                             
        else:                                                             #if the user does not leave it blank
            try:                                                         #the block of code could be tested for errors using try block                                
                contact = int(contact)                                   #the user could enter number only
                valid_contact = True                                     #assign the True boolean value to valid_contact
                break                                                    #the program will not ask the user to input contact again
            except:                                                      #the program will not show red code although the user does not input number
                print("Invalid contact number. Please enter number.")    #display text
    
    valid_gender = False                                                 #assign False boolean value to valid_gender
    while not valid_gender:                                              #keep asking user to input gender if the user's input is invalid
        gender = input("\nPlease enter your gender (Male/Female): ")     #ask the user to input gender
        strip_gender = gender.strip()                                    #eliminate any whitespace from the gender's beginning and end.
        
        if strip_gender == "":                                           #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
            valid_gender = False                                         #the program will ask the user to input gender again
            
        elif gender == "Male":                                           #if the user enter "Male"
            valid_gender = True                                          #the program will not ask the user to input gender again
            break
        elif gender == "Female":                                         #if the user enter "Female"
            valid_gender = True                                          #the program will not ask the user to input gender again
            break
        else:                                                            #if the user enter other words
            print("Invalid input. *Please enter Male / Female.")         #display text, the program will ask the user to input gender again

    birth_date = False                                                   #assign False boolean value to birth_date
    while not birth_date:                                                #keep asking user to input birthday if the user's input is invalid
        birthday = input("\nPlease enter your date of birth(DD/MM/YYYY): ")#ask the user to input birthday
        strip_date = birthday.strip()                                    #ask the user to input birthday
        if strip_date == "":                                             #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                        #display text
            birth_date = False                                           #the program will ask the user to input birthday again
            
        else:                                                            #if the user didnt leave it blank
            formattrue = False                                           #assign False boolean value to formattrue
            while not formattrue:                                        #keep asking user to input birthday if the user's input is invalid
                try:                                                     #the block of code could be tested for errors using try block.                            
                    day, month, year = birthday.split("/")               #split birthday by "/"and assign to  day, month, year accordingly
                    formattrue = True                                    
                    break
                except:                                                  #not show the red code if the user does not wirte the true date format
                    birthday = input("\nPlease enter the true format which is DD/MM/YYYY.\n>") #ask the user to input birthday again
                    formattrue = False                                   
            if len(day)>2 or len(month)>2 or len(year)!= 4 :            #to check if the date or month is more than 2 digits, or the year is not 4 digits. 
                print("The date of birth is invalid.")                  #display text
                birth_date= False                                       #will ask the user to input  birthay again
            else:                                                       #if the user enter the true numbers of digit
                num = True                                              #assign True boolean value to True
                try:                                                    #try to convert the string to integer
                    day = int(day)
                    month = int(month)
                    year = int(year)
                except:                                                 #does not show the red code although the string could not convert to integer
                    print("The date of birth is invalid. Please enter number.")
                    birth_date = False                                  #ask the user to input birthday again
                    num = False
                if num:  
                    if month > 12 or month < 0:                         #one year has 12 months only
                        print("The date of birth is invalid.")
                        birth_date = False      
                    else:                                               #if the month input is true
                        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #to check it is a leap year or not
                            if month == 2:                                       #in February in leap year
                                if day<0 or day> 29:                             #has 29 days 
                                    print("The date of birth is invalid.")
                                    birth_date = False
                                else:
                                    birth_date = True
                                    break
                        else:                                                   #if it is not the leap year
                            if month == 2:                                      #in february
                                if day>0 and day<= 28:                          #has 28 days only
                                    birth_date = True
                                    break
                                else:
                                    print("The date of birth is invalid.")      #display text
                                    birth_date = False                          #ask the user to input birthday again
                                        
                        if (month % 2 == 0 and month<= 7 and month!=2) or (month % 2 != 0 and 7<month<13 and month!=2):
                                                                                # to check if the month has 30 days
                            if 0 < day < 31:                                                  
                                birth_date = True
                                break
                            else:                                               #check if the day is out of range
                                print("The date of birth is invalid.")          #display text
                                birth_date = False                              #ask the user to input birthday again
                        elif (month % 2 != 0 and month<= 7 and month!=2) or (month % 2 == 0 and 7<month<13 and month!=2):
                                                                                # the left month have 31 days
                            if 0 < day < 32:
                                birth_date = True
                                break
                            else:                                               #check if the day is out of range
                                print("The date of birth is invalid.")          #display text
                                birth_date = False                              #ask the user to input birthday again



    print("Registered user detail updated successfully! A few steps left to register your username and password!") #display text
    
    username_exist = True                                                       #assign True boolean value to username_exist                                           
    while username_exist:                                                       #keep asking user to input new_username if the user's input is invalid
        can_use_username = True                                                 #assign True boolean value to can_use_username
        new_username = input("\nPlease enter your username: ")                  #ask the user to input new_username
        new_username = new_username.strip()
        if new_username == "":
            print("Please don't leave it blank.")
            can_use_username = False
        else:
            registeredLogin_text = open("Registeredlogin.txt", "r")                 #open text file with read mode as registeredLogin_text 
            for line in registeredLogin_text:                                       #iterate through each line in registeredLogin_text
                if line.startswith(new_username):                                   #search if line starts with the user's input
                    username, password = line.split("|")
                    if new_username == username.strip():                            #if the user's input same with the existing username
                        print("This username is already taken. Please try with another one.")   #display text
                        username_exist = True                                       #ask the user to input new_username again
                        can_use_username = False
        if can_use_username:                                                        #if the username is valid
            username_exist = False                                                  #will not ask the user to input new_username again
            password_valid = False
            print("\nYour password: ")
            print("- must be 8-30 characters \n-don't include '|' in your password.")   #display password details
            
    while not password_valid:                                                   #keep asking user to input new_password if the user's input is invalid
        new_password = input("\nPlease enter your password: ")                  #ask the user to input new_password
        if len(new_password) < 8:                                               #the password should more than 8 characters
            print("Your password is not strong enough. Please make sure your password has 8-30 characters.\n") #display text
        elif len(new_password)>30:                                              #the password should less than 30 characters
            print("Your password is too lengthy. Please make sure your password has 8-30 characters only.\n")
        elif "|" in new_password:                                               #the password should not include "|"
            print("Your password is invalid. Please don't include '|' in your password.")#display text
        else:                                                                   #if the password meets all criteria
            password_valid = True                                               #will not ask the user to input new_password again
            break

    rewrite = True  
    while rewrite:                                                              #keep asking user to input rewrite_password if the user's input is invalid
        rewrite_password = input("\nPlease reenter the password: ")             #ask the user to input rewrite_password
        strip_rewrite_password = rewrite_password.strip()                       #eliminate any whitespace from the gender's beginning and end.
        if strip_rewrite_password == "":                                        #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                               #display text
        elif rewrite_password == new_password:                                  #if rewrite_password  is same with new_password
            rewrite = False                                                     #will not ask the user to input rewrite_password again
            break
        else:                                                                   #if rewrite_password  is different with new_password
            print("Password does not match.")                                   #display text, will ask the user to input rewrite_password again

    detailtext = open("UserDetail.txt","a")                                     #open the text file with append mode as detailtext
    detailtext.write("\n")                                                      #append all the personal information in detailtext (text file)
    detailtext.write(new_username)
    detailtext.write(" | ")
    detailtext.write(name)
    detailtext.write(" | ")
    detailtext.write(address)
    detailtext.write(" | ")
    detailtext.write(email)
    detailtext.write(" | ")
    detailtext.write(str(contact))
    detailtext.write(" | ")
    detailtext.write(gender)
    detailtext.write(" | ")
    detailtext.write(birthday)
    detailtext.close()
            
    createtext = open("Registeredlogin.txt", "a")                               #open text file with append mode as createtext
    createtext.write("\n")                                                      #write username and password information in createtext
    createtext.write(new_username)
    createtext.write(" | ")
    createtext.write(new_password)
    createtext.close()
    print("Password matched. Security Question time now! (for reset password in future).")#display text
    valid_security_answer = False
    while not valid_security_answer:                                            #keep asking user to input security_question if the user's input is invalid
        security_question = input("\nWhat is your favourite color? : ")         #ask the user to input security_question
        strip_security_question = security_question.strip()                     #eliminate any whitespace from the gender's beginning and end.
        if strip_security_question == "":                                       #to check if the user leave it blank or click space only
            print("Please don't leave it blank.")                               #display text,will ask the user to input security_question again
        else:                                                                   #if the user does not leave it blank
            valid_security_answer = True                                        #will not ask the user to input security_question again
            break


    
    security_text = open("RegisteredSecurity.txt", "a")                         #open text file with append mode as security_text
    security_text.write("\n")                                                   #write the security info in security_text
    security_text.write(new_username)
    security_text.write(" | ")
    security_text.write(security_question)
    security_text.close()
    print("\nUser Registration Successful! We will now bring you to Registered User Login Page.")#display text
    registeredlogin()                                                           #call registeredlogin()to back to Registered Customer Login Page   


    
#new customer view Groceries detail    
def new_viewdetail():   
    medicines = open("medicine.txt","r")                                        #open "medicine.txt" with read mode as medicines                        
    print("\t\t\tMedicine Category\n")                                          #display text
    for medicine in medicines:                                                  #iterate through each medicine in medicines
        print(medicine)                                                         #display each medicine while iterating
    print("\t\t\tVegetable Category\n")                                         #display text
    vegetables = open("vegetable.txt","r")                                      #open "vegetable.txt" with read mode as vegetables
    for vege in vegetables:                                                     #iterate through each vege in vegetables
        print(vege)                                                             #display each vege while iterating
    print("\t\t\tFruit Category\n")                                             #display text
    fruits = open("fruit.txt","r")                                              #open "fruit.txt" with read mode as fruits
    for fruit in fruits:                                                        #iterate through each fruit in fruits
        print(fruit)                                                            #display each food while iterating
    print("\t\t\tDairy Category\n")                                             #display text
    dairies = open("dairy.txt","r")                                             #open "dairy.txt" with read mode as dairies
    for dairy in dairies:                                                       #iterate through each dairy in dairies
        print(dairy)                                                            #display each dairy while iterating
    print("\t\t\tHousehold Category\n")                                         #display text
    households = open("household.txt","r")                                      #open "household.txt" with read mode as households
    for household in households:                                                #iterate through each household in households
        print(household)                                                        #display each household while iterating
    medicines.close()                                                           #close all the text file opened as stated above
    vegetables.close()
    fruits.close()
    dairies.close()
    households.close()
    back = "-"                                                                  #assign "-" to back
    while back != "N":                                                          #keep asking user to input back if the user's input is invalid
        print("\nType 'N' to back to New Customer Menu Page.")                  #display text
        back = input("> ")                                                      #ask user to input back
        if back == "N":                                                         #if user enter "N"
            newCustomerMenu()                                                   #call newCustomerMenu()
            break                                                               #will not ask the user to input back again
        else:                                                                   #if the user enter words other than 'N'
            print("Invalid Input.")                                             #display text, will ask the user to input back again


#Registered Customer placed order and do payment    
def registered_placed_order(username):
    customer = []                                                               #set customer as an empty list
    number = False                                                              #assign False boolean value to number
    while not number:                                                           #keep asking user to input category if the user's input is invalid
        print("\nPlease enter the category of grocery.\n")                      #display text
        try:                                                                    #the block of code could be tested for errors using try block.  
            category = int(input("\t\tType 1 - Medicine\n\t\tType 2 - Vegetable\n\t\tType 3 - Fruits\n\t\tType 4 - Dairy\n\t\tType 5 - Household\n>"))
            if category >= 1 and category <=5:                                  #the user could enter number from 1 to 5 only
                number = True                                                   #assign True boolean value to number
                break                                                           #will not ask the user to input category again
            else:                                                               #if the user's input is out of range
                print("The number is out of range.\n")                          #display text
                number = False                                                  #will ask the user to input category again
        except:                                                                 #will not show a red code if the user enter words
            print("Invalid Input. Please enter a number.\n")                    #display text
            number = False                                                      #will ask the user to input category again
            
    if category == 1:                                                           #if user enter 1
        category = medicine_detail                                              #assign medicine_detail to the value of category
        viewcategory(1)                                                         #call viewcategory and assign 1 parameter
    elif category == 2:                                                         #if user enter 2
        category = vege_detail                                                  #assign vege_detail to the value of category
        viewcategory(2)                                                         #call viewcategory and assign 1 parameter
    elif category == 3:                                                         #if user enter 3
        category = fruit_detail                                                 #assign fruit_detail to the value of category
        viewcategory(3)                                                         #call viewcategory and assign 1 parameter
    elif category == 4:                                                         #if user enter 4
        category = dairy_detail                                                 #assign dairy_detail to the value of category
        viewcategory(4)                                                         #call viewcategory and assign 1 parameter
    elif category == 5:                                                         #if user enter 5
        category = household_detail                                             #assign household_detail to the value of category
        viewcategory(5)                                                         #call viewcategory and assign 1 parameter
        
    name = False                                                                #assign False boolean value to name
    place_order = False                                                         #assign False boolean value to place_order
    need_to_order = "no"                                                        #assign "no" to need_to_order 
    while not name:                                                             #keep asking user to input name if the user's input is invalid
        groceries_name = input("\nPlease enter the grocery NAME to place order. \n*Press'x' to back to Registered Customer Main Page.*\n>")
                                                                                #ask the user to input groceries_name 
        strip_name = groceries_name.strip()                                     #eliminate whitespace from the username's beginning and end.
        if strip_name == "":                                                    #if the user leave it blamk or click space only
            print("Please don't leave it blank.")                               #display text
            name = False                                                        #will ask the user to input groceries_name again
        elif groceries_name == "x":                                             #if the user enter "x"
            registeredMenu(username)                                            #call registeredMenu() and assign one parameter
            name = True                                                         #will not ask the user to input groceries_name again
            break
        else:
            for order in category:                                              #iterate through each order in category
                if order[0] == groceries_name[0].upper()+ groceries_name[1:].lower(): #if first element of order is same with the groceries name
                    groceries_name = groceries_name[0].upper()+ groceries_name[1:].lower() #ensure the first character of the groceries name is upper case
                    need_to_order = order                                       #assign value of order to need_to_order
                    break                                                       #stop searching other order in category
            if need_to_order != "no":                                           #if need_to_order has the value of order
                name = True                                                     #assign True boolean value to name
                place_order = True                                              #assign True boolean value to place_order
                break                                                           #stop asking the user to input groceries_name again
            else:                                                               #if need_to_order does not have the value of order
                name = False                                                    #ask the user to input groceries_name again
                print (groceries_name, "not found. Please try again.")          #display text

    if place_order:                                                             #if need_to_order has the value of order
        num = False                                                             #assign False boolean value to NUM
        while not num:                                                          #keep asking user to input quantity if the user's input is invalid
            try:                                                                #the block of code could be tested for errors using try block. 
                quantity = int(input("\nEnter the quantity: "))                 #the user can enter number only
                if quantity <= 0:
                    print("Please enter a valid quantity.")
                    num = False
                else:
                    num = True                                                      #assign True boolean value to num if the user enter number only
                    break                                                           #will not ask the user to input quantity again
            except:                                                             #will not show red code if the user enter words
                print("Invalid Input.")                                         #display text, will ask the user to input quantity again
                num = False
                
        #placed order
        float_price = float(need_to_order[1].strip("RM"))                       #the user could enter number only
        total = float_price*quantity                                            #multiply float_price and quantity
        totalprice = twodecimal(total)                                          #call twodecimal() and assign a parameter
        print("Order Summary:  Grocery name:",need_to_order[0],"\n\t\tPrice per quantity:", need_to_order[1],"\n\t\tQuantity: ",
          quantity,"\n\t\tTotal Price: RM",totalprice)                          #display text
        total = float(totalprice)                                               #convert totalprice to float type and assign to total
        paid = False                                                            #assign False boolean value to paid                      
        num = False                                                             #assign False boolean value to num
        num2 = True                                                             #assign False boolean value to num2
        while not num:                                                          #keep asking user to input money if the user's input is invalid
            try:                                                                #the block of code could be tested for errors using try block. 
                money = float(input("\nEnter the amount you want to pay: RM"))  #the user must enter number
                num = True                                                      #will not ask the user to input money again
                break
            except:
                print ("\nInvalid Input. Please type the number.")              #display text
                num= False                                                      #will ask the user to input money again
                
        if num:                                                                 #if the user enter number
            if money == total:                                                  #if the user's input is same with total
                print("\nPayment has been made.\n")                             #display text
                num2 = False                                                    #assign False boolean value to num2
            elif money > total:                                                 #if the user's input is greater with total
                more = money - total                                            #calculate more by subtracting total from money
                more = twodecimal(more)                                         #call twodecimal() and assign a parameter
                                                                                #assign the return value to more
                print("\nPayment has been made. Here's your change: RM", more,"\n") #display text
                num2 = False                                                    #assign False boolean value to num2
            while money < total:                                                #if the user's input is lesser than total
                money = total - money                                           #calculate more by subtracting total from money
                money = twodecimal(money)                                       #call twodecimal() and assign a parameter,assign the return value to more
                print("\nPayment Unsucessful. You still need to pay RM",money,"to complete the payment.") #display text
                total = float(money)                                            #convert total to float
                num2 = False                                                    #assign False boolean value to num2
                while not num2:                                                 #keep asking user to input money if the user's input is invalid
                    try:                                                        #the block of code could be tested for errors using try block.  
                        money = float(input("\nEnter the amount you want to pay: RM")) #the user can enter number only
                        num2 = True                                             #set True boolean value to num2
                        break                                                   #will not ask the user to input money again
                    except:                                                     #will not display red code although the user enter words
                        print ("\nInvalid Input. Please type the number.")      #display text
                        num2= False                                             #will ask the user to input money again
                        
            if num2:                                                            #if the user enter number only
                money = float(money)                                            #convert money to float type
                more = money - total                                            #calculate the balance by subtracting money with total
                more = twodecimal(more)                                         #call twodecimal and assign a parameter to get xx.xx format
                print("\nPayment has been made. Here's your change: RM", more,"\n") #display text
                num2 = False                                                    #assign False boolean value to num2
                
        totalprice = "RM"+totalprice                                            #join "RM" and totalprice and assign the value to totalprice
        customer = []                                                           #set customer to empty list 
        customer.append(username)                                               #append username to customer list
        customer.append(need_to_order[0])                                       #append grocery name to customer list                                                       
        customer.append(need_to_order[1])                                       #append grocery price to customer list
        customer.append(quantity)                                               #append quantity to customer list
        customer.append(totalprice)                                             #append totalprice to customer list
        registered_order.append(customer)                                       #append customer list to registered_order list
        updateorder_txt(customer)                                               #call updateorder_txt and assign a parameter to update the element of
                                                                                #to update the element of list to text file
        
        back = "-"                                                              #assign "-" to back
        while back != "N" or "Y":                                               #keep asking the user to input back if the user's input is invalid
            print("Type 'Y' to place another order. Type 'N' to back to Registered Customers Menu Page.")#display text
            back = input("> ")                                                  #ask the user to input back
            if back == "N":                                                     #if the user enter "N"
                registeredMenu(username)                                        #call registeredMenu() and assign a parameter
                break                                                           #will not ask the user to input back again
            
            elif back == "Y":                                                   #if the user enter "Y"
                registered_placed_order(username)                               #call registered_placed_order and assign a parameter
                break                                                           #will not ask the user to input back again
            
            else:                                                               #if the user does not enter "Y" or "N"
                print("Invalid Input.")                                         #display text


#Registered Customer view own order
def registered_view_order(username):
    registered_list = update_orderlist()                                        #call update_orderlist() and assign the return value to registered_list
    view = False                                                                #assign false boolean value to view
    print("\nHere's your order:")                                               #display text
    print("----------------------------------------------------------------------")
    for list in registered_list:                                                #iterate through each list in registered_list
        if list[0] == username:                                                 #if the first element of list is equal to user's username
            print(" Username: ",list[0], "\n","Grocery: ",list[1],"\n",
                  "Price Per Quantity: ",list[2],"\n","Quantity: ",list[3], "\n"
                  " Total Price: ",list[4],"\n")                                #display the user's order information      
            view = True                                                         #assign true boolean value to view
            
    if not view:                                                                #if the first element of each list is not equal to user's username
        print("Oops! You don't have any order.")                                #display text
        
    back = "-"                                                                  #assign "-" to back
    while back != "N":                                                          #keep asking the user to input back if the user's input is invalid
        print("\nType 'N' to back to Registered Customers Menu Page.")          #display text
        back = input("> ")                                                      #ask the user to input back
        if back == "N":                                                         #if the user enter "N"
            registeredMenu(username)                                            #call registeredMenu() and assign a parameter to navigate the user to
                                                                                #Registered Customer Menu Page
            break                                                               #will not ask the user to input back again
        
        else:                                                                   #if the user does not enter "N"
            print("Invalid Input.")                                             #display text, will ask the user to input back again


#Registered Customer view peronal information                
def registered_personalinfo(username):
    information = open("UserDetail.txt", "r")                                   #open text file with read mode and assign it to information
    for info in information:                                                    #iterate through each info in information
        if info.startswith(username.strip()):                                   #if info starts with user's username
            usernameInTxt, name,address,gmail,phonenumber,gender,birthday = info.split("|")#split the info with "|" and assign to the variables stated accordingly
            if usernameInTxt.strip() == username.strip():
                print("\nHere's your Personal Info")                                #display the user's personal info
                print("----------------------------------------------------------------------")
                print("Name:", name, "\nEmail ID:", gmail, "\nPhone Number:", phonenumber, "\nGender:", gender,"\nDate of Birth:", birthday)
    back = "-"                                                                  #assign "-" to back
    while back != "N":                                                          #keep asking the user to input back if the user's input is invalid
        print("Type 'N' to back to Registered Customers Menu Page.")            #display text
        back = input("> ")                                                      #ask the user to input back
        if back == "N":                                                         #if the user enter "N"
            registeredMenu(username)                                            #call registeredMenu() and assign a parameter to navigate the user to
                                                                                #Registered Customer Menu Page
            break                                                               #will not ask the user to input back again
        else:                                                                   #if the user does not enter "N"
            print("Invalid Input.")                                             #display text, will ask the user to input back again
    
#Registered Customer view all Groceries detail        
def registered_viewdetail(username):
    medicines = open("medicine.txt","r")                                        #open text file with read mode as medicines
    print("\t\t\tMedicine Category\n")                                          #display text
    for medicine in medicines:                                                  #iterate through each medicine in medicines
        print(medicine)                                                         #display each medicine while iterating
    print("\t\t\tVegetable Category\n")                                         #display text
    vegetables = open("vegetable.txt","r")                                      #open text file with read mode as vegetables
    for vege in vegetables:                                                     #iterate through each vege in vegetables
        print(vege)                                                             #display each vege while iterating
    print("\t\t\tFruit Category\n")                                             #display text
    fruits = open("fruit.txt","r")                                              #open text file with read mode as fruits
    for fruit in fruits:                                                        #iterate through each fruit in fruits
        print(fruit)                                                            #display each fruit while iterating
    print("\t\t\tDairy Category\n")                                             #display text
    dairies = open("dairy.txt","r")                                             #open text file with read mode as dairies
    for dairy in dairies:                                                       #iterate through each dairy in dairies
        print(dairy)                                                            #display each dairy while iterating
    print("\t\t\tHousehold Category\n")                                         #display text
    households = open("household.txt","r")                                      #open text file with read mode as households
    for household in households:                                                #iterate through each household in households
        print(household)                                                        #display household
    medicines.close()                                                           #close all the text file that opened as stated above
    vegetables.close()
    fruits.close()
    dairies.close()
    households.close()
    back = "-"                                                                  #assign "-" to back
    while back != "N":                                                          #keep asking the user to input back if the user's input is invalid
        print("Type 'N' to back to Registered Customers Menu Page.")            #display text
        back = input("> ")                                                      #ask the user to input back
        if back == "N":                                                         #if the user enter "N"
            registeredMenu(username)                                            #call registeredMenu() and assign a parameter to navigate the user to
                                                                                #Registered Customer Menu Page
            break                                                               #will not ask the user to input back again
        else:                                                                   #if the user does not enter "N"
            print("Invalid Input.")                                             #display text, will ask the user to input back again

            
#Registered Customer Menu    
def registeredMenu(registered_username):
    print("\nWelcome to Groceries Management System Registered Customer Page!\n")#display text
    invalid = True                                                               #assign True boolean value to invalid
    while invalid:                                                               #keep asking the user to input menu_num if the user's input is invalid
        print('''\tType 1 to view all groceries detail in system.
        Type 2 to place order of groceries and do payment.
        Type 3 to view your order.
        Type 4 to view your personal information.
        Type 5 to exit Groceries Management System Registered Customer Page.''') #display text
        menu_num  = input(">")                                                   #ask the user to input menu_num
        if menu_num == "1":                                                      #if the user enter "1"
            registered_viewdetail(registered_username)                           #call registered_viewdetail() and assign a parameter
            invalid = False                                                      #will not ask the user to input menu_num again
        elif menu_num == "2":                                                    #if the user enter "2"
            registered_placed_order(registered_username)                         #call registered_placed_order() and assign a parameter
            invalid = False                                                      #will not ask the user to input menu_num again
        elif menu_num == "3":                                                    #if the user enter "3"
            registered_view_order(registered_username)                           #call registered_view_order() and assign a parameter
            invalid = False                                                      #will not ask the user to input menu_num again
        elif menu_num == "4":                                                    #if the user enter "4"
            registered_personalinfo(registered_username)                         #call registered_personalinfo() and assign a parameter
            invalid = False                                                      #will not ask the user to input menu_num again
        elif menu_num == "5":                                                    #if the user enter "5"
            menu()                                                               #call menu()
            invalid = False                                                      #will not ask the user to input menu_num again
        else:                                                                    #if the user enter out of these 5 numbers
            print("Invalid Input. Please enter number.")                         #display text
            invalid = True                                                       #will ask the user to input menu_num again
            
#Registered Customer Login Page: check password
def registeredcheck(textusername, textpassword): 
    password = input("Please enter your password: ")                             #ask the user to input password
    if password == textpassword:                                                 #if the user's input is same with the textpassword set before
        print ("\nLogin Success! You could access to Registered Customer Menu Page now.\n")#display text
        registeredMenu(textusername)                                             #call registeredMenu() and assign a parameter to
                                                                                 #navigate the customer to Registered Customer Menu Page
    else:                                                                        #if the user's password is different with the textpassword set before
        for i in range(4):                                                       #the user have 4 chances to try
            password = input("Wrong Password. Please try again.\n\nPlease enter your password: ")#ask the user to input password again
            if password == textpassword:                                         #if the user's input is same with the textpassword set before
                print ("\nLogin Success! You could access to Registered Customer Menu Page now.\n") #display text
                registeredMenu(textusername)                                     #call registeredMenu() and assign a parameter to
                                                                                 #navigate the customer to Registered Customer Menu Page
                checkfailed = False                                              #assign False boolean value to checkfailed
                break                                                            #will stop the for loop and not ask the user to input password again
            
            else:                                                                #if the user's password is different with the textpassword set before                                         
                checkfailed = True                                               #assign True boolean value to checkfailed
                
        if checkfailed:                                                          #if the user's password is different with the textpassword set before 
            checkrepeat = True                                                   #set True boolean value to checkrepeat 
            print("Wrong Password.\n\nOops! You've reached the maximum password attempt.\n") #display text
            while checkrepeat:                                                   #keep asking the user to input select if the user's input is invalid
                select = input('''
              Type 1 to back to Menu Page. \n
              Type 2 to proceed to Forgot Password Page. \n''')
                if select == "1":                                                #if the user enter "1"
                    menu()                                                       #call menu() and navigate the customer to Menu Page
                    checkrepeat = False                                          #set False boolean value to checkrepeat
                    
                elif select == "2":                                              #if the user enter "2"
                    print("Forgot your password? Let us help you!")              #display text
                    security = open("RegisteredSecurity.txt", "r")               #open text file with read mode as security
                    for text in security:                                        #iterate through each text in security
                        if text.startswith(textusername):                        #if the text starts with user's username while iterating through security
                            username, security = text.split("|")                 #split the text and assign the value to two variables accordingly
                            username = username.strip()                          #Strip() eliminate any whitespace from the string's beginning and end.
                            security = security.strip()
                            if username == textusername:
                                registered_security = security 
                            
                    attempts = 3                                                 #assign 3 to the value of attempts
                    for i in range(attempts):                                    #the user has 3 chances to try
                        registered_ans = input("Please enter your favourite colour (you set it in the profile of this system before): ")
                                                                                 #ask the user to input registered_ans
                        if registered_ans == registered_security:                #if the registered_ans is same with the registered_security set before
                            print("\nCorrect Answer! You can now change the password.\n") #display the term of password
                            print("\nYour new password: ")
                            print("- must be 8-30 characters \n-don't include '|' in your password.\n")
                            password_valid = False                               #assign False boolean value to password_valid
                            while not password_valid:                        #keep asking the user to input registered_newpass if the user's input is invalid                         
                                registered_newpass = input("Please enter your password: ") #ask the user to input registered_newpass 
                                if len(registered_newpass) < 8:                  #the user should input more than 8 characters 
                                    print("Your password is not strong enough. Please make sure your password has 8-30 characters.\n")
                                elif len(registered_newpass)>30:                 #the user should enter less than 30 characters
                                    print("Your password is too lengthy. Please make sure your password has 8-30 characters only.\n")
                                elif "|" in registered_newpass:                  #the user's input should not include "|"
                                    print("Your password is invalid. Please don't include '|' in your password.")
                                else:                                            #if the user meets all the requirement
                                    password_valid = True                        #reassign True boolean value to password_valid      
                                    break                                        #will not ask the user to input registered_newpass again
                                
                            registered_rewrite = True                            #assign True boolean value to registered_rewrite
                            while registered_rewrite:                        #keep asking the user to input registered_rewrite if the user's input is invalid
                                registered_reenter = input("Please reenter the new password.") #ask the user to input registered_reenter
                                if registered_newpass == registered_reenter:     #if the user's input is same with registered_newpass 
                                    registered_rewrite = False                   #reassign False boolean value to registered_rewrite
                                    break                                        #will not ask the user to input registered_reenter again
                                
                                else:                                            #if the user's input is different with registered_newpass 
                                    print("\nPassword does not match.")          #display text
                                    registered_rewrite = True                    #will ask the user to input registered_reenter again
                                    
                            print("\nYou have successfully changed the password!We will bring you back to Registered Customer login page again!\n")
                                                                                 #display text
                            resetpassword("Registeredlogin.txt",textpassword,registered_newpass) #call resetpassword and assign 3 parameters
                            registeredlogin()                                    #call registeredlogin() to naviagate the user to Registered Login Page   
                            changed = True                                       #assign True boolean value to changed
                            break                                                #will not ask the user to input registered_ans again
                        
                        else:                                                    #if the registered_ans is different with the registered_security set before
                            attempts = attempts - 1                              #less one attempt chance
                            print("Your answer is wrong. ",attempts,"attempts left.")#display text
                            changed = False                                      #assign False boolean value to changed
                            
                    if not changed:                                              #if the user failed to answer security question
                        print("\nSorry. To ensure the privacy, you are not able to change the password.We will bring you back to Menu Page. to\n")
                                                                                 #display text
                        menu()                                                   #call menu() to navigate the customer to Menu Page
                    checkrepeat = False                                          #reassign False boolean value to checkrepeat
                    
                else:                                                            #if the user does not enter "1" or "2" to select input
                    print("Invalid Input")                                       #display text
                                                                                 #will ask the user to input select again


            
#Registered Customer Login Page: check username
def registeredlogin():
    print("\nRegistered Customer Login Page")                                    #display text
    valid_name = False                                                           #set False boolean value to valid_name
    while not valid_name:                                                   #keep asking the user to input registered_username if the user's input is invalid
        registered_username = input("\nPlease enter your username: ")            #ask the user to input registered_username
        strip_registered_username = registered_username.strip()                  #Strip() eliminate any whitespace from the string's beginning and end.
        if strip_registered_username == "":                                      #if the user leave it blank or click space only
            print("Please don't leave it blank.")                                #display text, will ask the user to input registered_username again
        else:                                                                    #if the user does not leave it blank
            valid_name = True                                                    #set True boolean value to valid_name
            break                                                                #will not ask the user to input registered_username again
        
    registeredtext = open("Registeredlogin.txt", "r")                            #open text file with read mode as registeredtext 
    found = False                                                                #assign False boolean value to found
    for text in registeredtext:                                                  #iterate each text in registeredtext
        if text.startswith(registered_username):                                 #if text starts with the user's input
            registeredtext_username,registeredtext_password = text.split("|")    #split the text using '|' and assign to two variables accordingly
            registeredtext_username = registeredtext_username.strip()            #strip() eliminate any whitespace from the string's beginning and end.
            registeredtext_password = registeredtext_password.strip()            
            if registeredtext_username == registered_username:                   #if the user's input is same with registeredtext_username
                found = True                                                     #assign True boolean value to found
                registeredcheck(registeredtext_username, registeredtext_password)#call registeredcheck() and assign two parameters
                break                                                            #stop searching other text
            else:                                                                #if the user's input is different with registeredtext_username
                found = False                                                    #assign False boolean value to found
                
    if not found:                                                                #if the user's input is different with registeredtext_username
        print("\nUsername not found.\n")                                         #display text
        new = 0                                                                  #assign 0 to new
        while new!= "Y" or new!= "N" or new!="":                                 #keep asking the user to input new if the user's input is invalid
            print("Don't have an account? Type 'Y' to create an account.")       #display text
            print("Type 'N' to back to Menu Page.")
            print("Hit enter without typing anything to try again.")
            new = input(">")                                                     #ask the user to input new
            if new == "Y":                                                       #if the user enter "Y"
                createaccount()                                                  #call createaccount()  
                break                                                            #will not ask the user to input new again
            elif new == "N":                                                     #if the user enter "N"
                menu()                                                           #call menu()       
                break                                                            #will not ask the user to input new again
            elif new == "":                                                      #if the user leave it blank
                registeredlogin()                                                #call registeredlogin() to ask the user to input registered_username again
                break                                                            #will not ask the user to input new again
            else:                                                                #if the user's input other than "Y", 'N" or ""
                print("Invalid input.")                                          #display text, will ask the user to input new again
                

#exit
def exit():                                           
    return "exit"                                                                #return 'exit' to caller

#Admin Page - Get username    
def admin():
    print("\nAdmin Login Page")                                                  #display text
    valid_username = False                                                       #assign False boolean value to valid_username
    while not valid_username:                                                   #keep asking the user to input admin_username if the user's input is invalid
        print("\nPlease enter your username or type 'x' to back to Menu Page.")  #display text
        admin_username = input(">")                                              #ask the user to input admin_username
        strip_admin_username = admin_username.strip()                            #eliminate any whitespace from the admin_username's beginning and end.
        if strip_admin_username == "":                                           #if the user leave it blank or click space on;y
            print("Please don't leave it blank.")                                #display text, will ask the user to input admin_username again
        elif admin_username == "x":                                              #if the user enter "x"
            menu()                                                               #call menu() and naviagate the user to Menu Page
            valid_username = True                                                #reassign True boolean value to valid_username
            break                                                                #will not ask the user to input admin_username again
        else:                                                                    #if the user's input is not blank or "x"
            valid_username = True                                                #reassign True boolean value to valid_username
            break                                                                #will not ask the user to input admin_username again
    if admin_username != "x":                                                    #to ensure that the user completely quit this page
        adminlogin(admin_username)                                               #call adminlogin() and assign a parameter


    

# Main Logic
while True:                                                             #keep running the code until break
    print("Hi there! Welcome to Groceries Management System by FRESHCO Sdn Bhd.\n") #display welcoming text
    print("There's just one more step you need to take to make our system works!\n")##display welcoming text
    registered_order = update_orderlist()                               #call update_orderlist()and assign the value to registered_order
    medicine_detail = update_grocerylist("medicine.txt")                #call update_grocerylist("medicine.txt") and assign the value to medicine_detail
    vege_detail = update_grocerylist("vegetable.txt")                   #call update_grocerylist("vegetable.txt") and assign the value to vege_detail
    fruit_detail = update_grocerylist("fruit.txt")                      #call update_grocerylist("fruit.txt") and assign the value to fruit_detail
    dairy_detail = update_grocerylist("dairy.txt")                      #call update_grocerylist("dairy.txt") and assign the value to dairy_detail
    household_detail = update_grocerylist("household.txt")              #call update_grocerylist("household.txt") and assign the value to household_detail
    menu()                                                              #call menu() to navigate the user to Menu Page
    if exit() == "exit":                                                #if the user enter "8" in Menu Page, exit() will be executed and return "exit"
        break                                                           #break the while True loop, the code will stop running

    
    
    
    
    
