import read as rd
import operation as op

# Define function to display main menu
def display_main_menu():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("|                                                                    |")
    print("|                                Namaste                             |")
    print("|                                                                    |")
    print("|                         LAPTOPS TECH PVT.LTD                       |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("+====================================================================+")
    print("|                                                                    |")
    print("|                               Main Menu                            |")
    print("|                                                                    |")
    print("+--------------------------------------------------------------------+")
    print("|                                                                    |")
    print("|                               1) Enter                             |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                               2) Exit                              |")
    print("|                                                                    |")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()
    
# Infinite loop to keep displaying main menu and getting user input
while True:
    display_main_menu()
    user_input = input(" PLEASE ENTER OPTION TO PROCEED !! ")
    print()

    # If user enters '1', display available items and options for ordering/selling
    if user_input == '1':
        print(" THESE ARE THE ITEMS THAT ARE AVAILABLE IN OUR SHOP !! \n")
        rd.display_interface()

         # Inner loop for ordering/selling
        while True :
            print()
            print(" PLEASE CHOOSE ANY OF THE OPTIONS BELOW !! \n")
            print("╔═══════════════════════════╗")
            print("║    1   ║ ORDER            ║")
            print("║═══════════════════════════║")
            print("║    2   ║ SELL             ║")   
            print("║═══════════════════════════║")
            print("║    3   ║ BACK             ║")
            print("║═══════════════════════════║")
            print("║    4   ║ EXIT             ║")
            print("╚═══════════════════════════╝")
            print()
            # Get user choice for ordering/selling
            choice_for_order_and_sell = input(" PLEASE ENTER YOUR CHOICE ")
            print()
            # If user chooses '2', get customer name and proceed with selling laptops
            if choice_for_order_and_sell == '2':
                    op.get_customer_name()
                    op.Selling_Laptops()
            # If user chooses '1', proceed with ordering laptops
            elif choice_for_order_and_sell == '1':
                   op.Ordering_Laptops()
            elif choice_for_order_and_sell == '3':
                    break
            elif choice_for_order_and_sell == '4':
                    exit()
            else:
                print("Invalid Selection. Please enter a valid option.")




    elif user_input == '2':
            exit()
    # If user enters invalid input, prompt them to enter a valid option
    else:
            print(" Invalid Selection. Please enter a valid option.")
            print()
            

            


            

            
            
        
