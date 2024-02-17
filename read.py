# Create an empty list to store laptop data
Laptops = []
# Set the path to the file containing laptop data
path ="Products.txt"
# Read in each line of file and append to data list
with open(path, 'r') as file:
    for line in file:
        line = line.strip().split(",")
        if len(line) >= 6:
            Laptops.append(line)
#Define a function to display the laptop data in a formatted table       
def display_interface():
    #Printing table header 
    print("|**************************************************************************************************************|")
    print("| {:<24} | {:<19} | {:<10} | {:<15} | {:<15} | {:<10} |".format("Product", " Brand", " Price", " Quantity", " Processor", " Graphics"))
    print("|**************************************************************************************************************|")
    #Prinitng table row with laptops data
    for i in Laptops:
        print("| {:<24} | {:<19} | {:<10} | {:<15} | {:<15} | {:<10} |".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        print("|**************************************************************************************************************|")


