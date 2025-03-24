#Programmer: Timothy Pickering
#Date: 3/23/25
#Title: Average numbers from list

def sum_numbers_from_file():

    try:
        #Open the file for reading
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()  #Read all lines into a list

        #Convert strings to integers, handling potential errors
        numbers = [int(num.strip()) for num in numbers]  #Remove whitespace and convert to integers

        #Calculate total and average
        total = sum(numbers)
        average = total / len(numbers) if numbers else 0  #Avoid division by zero

        #Display results
        print(f"Total of numbers: {total}")
        print(f"Average of numbers: {average:.2f}")

    except FileNotFoundError:
        #Handle case where file does not exist
        print("Error: The file 'numbers.txt' was not found. Please run Program #2 first.")

    except ValueError:
        #Handle case where a line in the file is not a valid integer
        print("Error: The file contains non-numeric data and cannot be processed.")

    except Exception as e:
        #Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


#Run the function
if __name__ == '__main__':
    sum_numbers_from_file()
