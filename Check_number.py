print("\nThis program will check if your input is a number.")

is_number = input("\nEnter something :")

try :
    int(is_number)
    print(str(is_number)+ " is a number.") 

except ValueError:
    print(str(is_number)+ " is not a number.") 

