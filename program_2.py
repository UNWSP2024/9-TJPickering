#Programmer: Timothy Pickering
#Date: 3/23/25
#Title: Random number list generator

#Required library
import random

def write_random_numbers():

    try:
        #Prompt user for the number of random numbers to generate
        num_count = int(input("Enter how many random numbers to generate (1-1000): "))

        #Validate that input is within the allowed range
        if num_count < 1 or num_count > 1000:
            print("Error: Please enter a number between 1 and 1000.")
            return

        #Open the file 'numbers.txt' in write mode
        with open("numbers.txt", "w") as file:
            #Generate and write the specified number of random numbers
            for _ in range(num_count):
                file.write(f"{random.randint(1, 500)}\n")

        #Confirm successful write operation
        print(f"{num_count} random numbers written to numbers.txt successfully.")

    except ValueError:
        #Handle case where user input is not a valid integer
        print("Error: Please enter a valid integer.")


#Run the function
if __name__ == '__main__':
    write_random_numbers()
