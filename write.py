#sell invoice generator method
import os
import datetime
import operation as op
import read as rd
now = datetime.datetime.now()

def sell_invoice():
    # Generate unique filename for the invoice
    base_filename = f"{op.Name_}_sell_Bill.txt"
    Count = 1

    # Checking if file already exists, and if so, generate a new filename
    while os.path.exists(base_filename):
            # If the file already exists, generate a new filename by appending the Count to the base filename
            new_filename = f"{op.Name_}_sell_Bill_{Count}.txt"
            # Increment the Count
            Count += 1
            # Update the base filename to the new filename
            base_filename = new_filename
    # Open the file for writing
    path1 = r"{}".format(base_filename)
    # Loop through the laptops in the inventor
    with open(path1, "w", encoding='utf-8') as sellBill:
        for Stack in rd.Laptops:
            for Inner_Element in Stack:
                if op.Name_.lower() == Inner_Element.lower():
                    Bill_data = Stack
                    Delivery_Charge = (0.02 * int(Stack[2][2:])) * op.No_Of_Items  # slicing to remove _ and $ check by removing  #print(Stack[2][2:])
                    Totalamt_ofdelivery = Delivery_Charge + (int(Stack[2][2:])) * (op.No_Of_Items)
                    # Create the invoice header, data, and footer
                    head="""                    +======================================================================================================+
                    |                                           LAPTOPS TECH PVT.LTD                                       |
                                                                Contact : 9816344823                                       |
                    +======================================================================================================+
                    |                                                                                                      |
                    | --------------------------------------------SELLING BILL --------------------------------------------|"""

                    data="""
                    |                                                                                                      |
                       ♦ CUSTOMER NAME:                                                           {}                       
                    |                                                                                                      |
                       ♦ LAPTOP NAME:                                                             {}                       
                    |                                                                                                      |
                    |  ♦ BRAND NAME:                                                              {}
                                                                                                                         
                    |  ♦ Quantity :                                                              {}
                    |
                       ♦ BUYING DATE:                                                            {}                       
                    |                                                                                                      |
                       ♦ BUYING TIME:                                                            {}                       
                    |                                                                                                      |
                       ♦ TOTAL AMOUNT EXCLUDING DELIVERY CHARGE:                                 {}                       
                    |                                                                                                      |
                       ♦ DELIVERY CHARGE:                                                        {}                       
                    |                                                                                                      |
                                                                                                                          
                    |______________________________________________________________________________________________________|
                    |                                                                                                      |
                       ♦ GRAND TOTAL(INCLUDING DELIVERY CHARGE):                                 {}                       
                    |______________________________________________________________________________________________________|""".format( op.nameofcustomer, Bill_data[0], Bill_data[1],op.No_Of_Items
                                                                                                                                ,now.date(), now.time(),"$ "+str((int(Bill_data[2][2:])) * op.No_Of_Items), "$ "+str(Delivery_Charge), "$ "+str(Totalamt_ofdelivery))

                    foot="""
                    |                                                                                                      |
                    |--------------------------- THANK YOU! FOR BUYING OUR PRODUCTS ☺☺☺ !!! -----------------------------|
                    |                                                                                                      |
                    +======================================================================================================+
                """  # Write the header, data, and footer to the file
                    sellBill.write(head) 
                    sellBill.write(data) 
                    sellBill.write(foot) 
                   


# data update method after sell
def update():
    with open(rd.path, 'w') as file:
       for Stack in rd.Laptops: #for each loop
          para=",".join(Stack)
          file.write(para+"\n")





#order invoice generator method
def order_bill():
    
    # Creating the order invoice file
    Order_Folder=f"{op.ProductName}_order_bill.txt"

    Count=1

    while os.path.exists(Order_Folder):

        Order_FolderNew=f"{op.ProductName}_order_bill_{Count}.txt"

        Count +=1
        
        Order_Folder=Order_FolderNew

    path2 = r"{}".format(Order_Folder)
    
    # Calculating the net amount, VAT amount, and gross amount
    Net_amount=(int(op.Price_of_Laptop)*int(op.Quantities_))
    VAT_amount=(int(op.Price_of_Laptop)*0.13)*int(op.Quantities_)
    Gross_amount = Net_amount+VAT_amount
    # Writing the data to the order invoice file
    with open(path2,"w", encoding='utf-8') as orderBill:
        
        head="""                          ╔══════════════════════════════════════════════════════════════════════════════╗
                          ║                                          LAPTOPS TECH PVT.LTD                                        ║
                                                                     Putalisadak,Ktm                                                     
                          ║                                          Contact : 9816344823                                        ║ 
                           ====================================================================================================== 
                          ║                                                                                                      ║
                            --------------------------------------------ORDER BILL----------------------------------------------- """

        data="""
                          ║                                                                                                      ║
                             ♦ NAME:                                                        {}                 
                          ║                                                                                                      ║
                             ♦ LAPTOP NAME:                                                             {}                         
                          ║                                                                                                      ║
                             ♦ BRAND :                                                                  {}                        
                          ║                                                                                                      ║
                             ♦ PROCESSOR:                                                               {}                         
                          ║                                                                                                      ║
                             ♦  GRAPHICS CARD / GPU:                                                    {}                        
                          ║                                                                                                      ║
                             ♦  NO. OF QUANTITY:                                                        {}                        
                          ║                                                                                                      ║
                             ♦  LAPTOP PRICE:                                                           {}                        
                          ║                                                                                                      ║
                             ♦  VAT AMOUNT :                                                            {}                        
                          ║                                                                                                      ║                   
                             ♦  ORDERING DATE:                                                          {}                                                                                                                         
                          ║                                                                                                      ║
                             ♦  ORDERING TIME:                                                          {}                        
                          ║______________________________________________________________________________________________________║
                                                                                                                                  
                          ║  ♦  TOTAL AMOUNT(TOTAL COST INCLUDING SERVICE AND TAXES):                   {}                       
                           ______________________________________________________________________________________________________    """.format("LAPTOPS TECH PVT.LTD", op.ProductName, op.Brand_Name_, op.Processor_, op.Graphics_Card, op.Quantities_, "$ "+str(Net_amount), "$ "+str(VAT_amount), now.date(),now.time(),"$ "+str(Gross_amount))
        foot="""                                                                                                            
                                                                                                                                  
                          ║----------------------------------THANK YOU ☺☺☺ PLEASE VISIT AGAIN----------------------------------║
                                                                                                                                 
                          ╚═══════════════════════════════════════════════════════════════════════════════╝
                      """  
          
        orderBill.write(head)
        orderBill.write(data)
        orderBill.write(foot)
                    

def udpate_order():

    for Laptop_List in rd.Laptops:
        
       if op.Brand_Name_.lower() in [Items.strip().lower() for Items in Laptop_List] and op.Processor_.lower() in [Items.strip().lower()
            for Items in Laptop_List] and op.Graphics_Card.lower() in [Items.strip().lower() for Items in Laptop_List]:
            update_no_of_Items = int(Laptop_List[3])+int(op.Quantities_)
            Laptop_List[3]=" "+str(update_no_of_Items)
            update()
            break
    
