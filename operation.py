import read as rd
import write as wr
import datetime

"""
Here Initializing Global variable
here with name , no of items name of customer as string
"""
#sell product method
Name_=""
No_Of_Items=""
nameofcustomer=""
Sell_counter=0
def Selling_Laptops():  # define the Selling_Laptops function
    sell = True  # set the initial value of sell to True
    while sell:   # loop while sell is True
        repeat=True     # set the initial value of repeat to True   
        while repeat:
            print()
            print("+-----------------------------------------------------------------------------------------------+")
            name = input(" Enter The Product Name : ") # prompt the user to enter the product name and assign it to the variable name
            print("+-----------------------------------------------------------------------------------------------+")
            print()
            if name.isnumeric(): ## check if the product name is numeric
                 print()
                 print("The Product Name Cannot Be Numeric")
                 print()
            else:
                found = False
                for i in rd.Laptops:
                    if name.lower() in [item.lower() for item in i]:
                        found = True
                        repeat=False 
                        break
                if found:
                    global Name_ # access the global variable Name_
                    Name_ = name
                else:
                    print()
                    print(" SORRY IT IS OUT OF THE STOCK")
                    print()

        global No_Of_Items
        while True:
         try:
             global Sell_counter
             print()
             print("-----------------------------------------------------------------------------------------------")
             Sell_counter = int(input(" Enter The Number Of Items You Want To Sell : "))
             print("-----------------------------------------------------------------------------------------------")
             print()
             if Sell_counter > 0:
                No_Of_Items = Sell_counter
                break
             else: 
               
               print()
               print(" Error: Please enter a valid Value . ") 
               print()    
         except ValueError:
             print("-----------------------------------------------------------------------------------------------")
             print()
             print()
             print(" Error: Please enter a Valid value. ")
             
             print()

        # iterate through the Laptops list in the read module
        for Stack in rd.Laptops:
            for Inner_Element in Stack: # iterate through each element in the current list item
                if name.lower() == Inner_Element.lower(): # check if the product name is in the current list item, ignoring case
                    if Sell_counter>int(Stack[3]) or int(Stack[3])<= 0: # check if there are enough items in stock to sell
                        print()
                        print(" THE ITEM IS OUT OF STOCK!")
                        sell = False
                    else:
                        print()
                        print("-----------------------------------------------------------------------------------------------")
                        print(" ***Products That Are Available In Our Stock*** ", Stack[3])
                        print("-----------------------------------------------------------------------------------------------")
                        print()
                        Left_Product = int(Stack[3]) - Sell_counter  # calculate the number of items left in stock
                        Stack[3] = " "+str(Left_Product) # update the number of items in stock in the current
                        print()
                        print("-----------------------------------------------------------------------------------------------")    
                        ans = input(" DO YOU WANT TO BUY MORE PRODUCTS !! Enter 'Y/y' for YES and 'N/n' for NO --> ")
                        print("-----------------------------------------------------------------------------------------------")
                        if ans.lower() == "n":
                            sell = False
                            print()
                            print()
                            print("===============================================================================================")
                            print("\t\t THANK YOU! THE STOCK IS UPDATED AND  BILL IS GENERATED ")
                            print("===============================================================================================")

                            print()
                        wr.update()
                        wr.sell_invoice()




"""
Here Initializing Global variable
here with ProductName ,BrandName, Processor price of laptops graphic card
nameofcustomers as string and Quantites as int
"""
#ordering producs  method
ProductName=""
Brand_Name_=""
Processor_=""
Price_of_Laptop=""
Graphics_Card=""
Quantities_=""
nameofcustomer=""
path ="Products.txt"
def Ordering_Laptops():
    print()
    print("# Please Enter The Following INFORMATION OF LAPTOP TO PLACE ORDER --> \n")
    
    repeat = True
    while repeat:
        while True:
            global ProductName
            print()
            print("-----------------------------------------------------------------------------------------------")
            Product_name = input(" ENTER THE PRODUCT NAME YOU WANT TO ORDER: ")
            print("-----------------------------------------------------------------------------------------------")
            print()
            if not Product_name.isnumeric() and Product_name != "":
                ProductName = Product_name
                break
            else:
                print()
                print("Invalid input! Product Name should not contain numeric values and Empty Values")
                print()

        while True:
            global Brand_Name_
            print()
            print("-----------------------------------------------------------------------------------------------")
            Brand_name = input(" ENTER THE BRAND NAME YOU WANT TO ORDER: ")
            print("-----------------------------------------------------------------------------------------------")
            print()
            if not Brand_name.isnumeric() and Brand_name != "":
                Brand_Name_ = Brand_name
                break
            else:
                print()
                print("Ops Sorry! Please Enter the Brand Name")
                print()

        while True:
            global Processor_
            print()
            print("-----------------------------------------------------------------------------------------------")
            PROCESSOR = input(" ENTER THE PROCESSOR YOU WANT TO ORDER: ")
            print("-----------------------------------------------------------------------------------------------")
            print()
            if not PROCESSOR.isnumeric() and PROCESSOR != "":
                Processor_ = PROCESSOR
                break
            else:
                print()
                print("Ops Sorry! Processor Name should not contain numbers or be empty")
                print()

        while True:
            try:
                global Price_of_Laptop
                print()
                print("-----------------------------------------------------------------------------------------------")
                PRICE = int(input(" ENTER THE PRICE OF THE PRODUCT YOU WANT TO ORDER: "))
                print("-----------------------------------------------------------------------------------------------")
                print()
                if PRICE > 0:
                    Price_of_Laptop = PRICE
                    break
                else:
                    print()
                    print(" Error: Please enter a valid Price of the Product ")
                    print()
            except ValueError:
                print("-----------------------------------------------------------------------------------------------")
                print()
                print()
                print(" Ops Sorry! Please enter the value in digits for PRICE.")
                print()

        while True:
            global Graphics_Card
            print()
            print("-----------------------------------------------------------------------------------------------")
            GRAPHICS = input(" ENTER THE GRAPHICS/GPU YOU WANT TO ORDER: ")
            print("-----------------------------------------------------------------------------------------------")
            print()
            if not GRAPHICS.isnumeric() and GRAPHICS != "":
                Graphics_Card = GRAPHICS
                break
            else:
                print()
                print("Ops Sorry! Please Enter Valid Graphics Card")
                print()

        while True:
            try:
                global Quantities_
                print()
                print("-----------------------------------------------------------------------------------------------")
                Quantity = int(input(" ENTER THE NO. OF QUANTITY YOU WANT TO ORDER: "))  # Convert input to integer
                print("-----------------------------------------------------------------------------------------------")
                print()
                if Quantity > 0:
                    Quantities_ = Quantity
                    break
                else:
                    print()
                    print("Error: Please enter a valid Quantity")
                    print()
            except ValueError:
                print("-----------------------------------------------------------------------------------------------")
                print()
                print()
                print("Invalid input! Please enter an integer value for QUANTITY.")
                print()
        ans = input("\n Do you want to place another order? (Enter 'Y' or 'y' for YES, or any other key to exit): ")
        print()
        if ans.lower() != "y":
            repeat = False
            print("=============================================================================================================")
            print("\t\t    THANK YOU! FOR BUYING OUR PRODUCTS, YOUR ORDER BILL IS GENERATED ")
            print("=============================================================================================================")
        else:
             # Update the stock here
             laptop_found = False
             for Stack in rd.Laptops:
                 for Inner_Element in Stack:
                     if ProductName.lower() == Inner_Element.lower():
                         Left_Product = int(Stack[3]) + Quantities_
                         Stack[3] = str(Left_Product)
                         laptop_found = True
    
             # If laptop is not found, add it to the stock
             if not laptop_found:
                 new_laptop = [ProductName, Brand_Name_, str(Price_of_Laptop), str(Quantities_), Processor_, Graphics_Card]
                 rd.Laptops.append(new_laptop)
    
             # Update the stock in the file
             with open(path, 'w') as file:
                  for laptop in rd.Laptops:
                      line = ','.join(laptop)
                      file.write(line + '\n')

        wr.order_bill()
        wr.udpate_order()

        

def get_customer_name():
     while True:
                print()
                print("-----------------------------------------------------------------------------------------------")
                customername = input(" PLEASE ENTER YOUR NAME  : ")
                print("-----------------------------------------------------------------------------------------------")
                print()
                if not customername.isnumeric() and customername != "":# Check if input contains numeric values
                    global nameofcustomer
                    nameofcustomer = customername
                    break
                else:
                     print()
                     print("Ops Sorry ! Please Enter a Valid Name !! ")
                     print()
           
