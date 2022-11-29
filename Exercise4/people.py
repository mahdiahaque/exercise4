"""A template for a python script deliverable for INST326.

Driver: Mahdia Haque
Navigator: Ali Behrami
Assignment: Exercise 4
Date: 12/03/2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import re




def parse_name(text):
    

    pattern = r'^(\w+\s\w+)'
    regex = re.compile(pattern)

    name = regex.findall(text)
    print(name)
    return name


def parse_address(text):
    
    #pattern = r'(\d+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'
    pattern = r'(\d{1,}[\w\s]+)\s(\w+)\s([A-Z]{2})'
    regex = re.compile(pattern)

    address = regex.finditer(text)
    
    for match in address:
        street = (match.group(1))
        city = (match.group(2))
        state = (match.group(3))
        print(street)
        print(city)
        print(state)
        
        return street,city,state
    

    


def parse_email(text):

    pattern = r'[\w+.?_?]+@\w+.\w+'
    regex = re.compile(pattern)

    email = regex.findall(text)
    print(email)
    
    return email

    

























def main(parameter1, parameter2):
    #Note that this function does not do anything.
    #You would insert functional code here.
    #Instead we will use the pass keyword to avoid doing that.
    pass

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence. 
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('required', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.

    return args

if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
    main(arguments.required, arguments.optional)


