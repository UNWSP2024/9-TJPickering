#Programmer: Timothy Pickering
#Date: 3/23/25
#Title: Name counter

def count_file_lines():

    try:
        #Open the file in read mode
        with open("names.txt", "r") as file:
            #Read all lines into a list
            lines = file.readlines()

            #Count the number of lines
            num_of_names = len(lines)

            #Display the total count
            print(f'Total number of names in the file: {num_of_names}')

    except FileNotFoundError:
        #Handle the case where the file does not exist
        print("Error: The file 'names.txt' was not found. Please make sure it exists.")

    except Exception as e:
        #Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

#Run the function
if __name__ == '__main__':
    count_file_lines()
