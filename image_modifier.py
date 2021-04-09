"""
    CS051P Lab Assignments: PPM Image Modifier

    Author: Charles Rak
    Partner: Theodore Brown

    Date:   October 20 2020

    The goal of this assignment is to give you practice working with lists
    by writing a program that manipulates image files in various ways.
"""
from math import sqrt


def decode(in_filename, out_filename):
    """ 
    :param in_filename(str): name of file given as input    
    :param out_filename(str): name of new file created by program   
    :return: none
    """
    in_file = open(in_filename, "r")
    out_file = open(out_filename, "w")
    count = 1
    #Cycles through the lines of the in_file
    for line in in_file:
        # Accounts for header of file
        if(count <= 3):
            out_file.write(line)
        # Accounts for body of file
        if(count > 3):
            modified_string = ""
            for a in line.split():
                a = int(a)
                # Modifies a based on value
                if (a % 3 == 0):
                    a = 0
                elif (a % 3 == 1):
                    a = 153
                elif (a % 3 == 2):
                    a = 255
                modified_string += str(a) + " "
            #Writes A to file
            out_file.write(modified_string)
        count += 1
    in_file.close()
    out_file.close()

# commit 1

def main_part1():
    # TODO: call the <decode> function you developed to decode
    #  the image <files/part1.ppm>
    decode("files/part1.ppm", "files/newfile.ppm")
    pass


def negate(line):
    """
    Takes a set of color values, and returns a set with all of those color values negated.
    :param line(str): string supplied by user
    :return output_string(str): string with all values in line negated
    """
    output_string = ""
    # Checks to see that number of elements is divisible by 3
    if(len(line.split()) % 3 == 0):
        for a in line.split():
            a = int(a)
            # Negates value
            a = 255 - a
            a = str(a)
            output_string += a + " "
    else:
        return ""
    
    return output_string


def grey_scale(line):
    """
    Takes a set of color values, and returns a set with all those color values assigned to a grey color value.
    :param line (str): Input parameter
    :return gray_string(str): line with each set of three r, g, b values replaced by three grey values
    """
    grey_list = line.split()
    gray = 0
    gray_string = ""
    # Cycles through values by 3
    for a in range(0, len(grey_list), 3):
        grey_list[a] = int(grey_list[a])
        grey_list[a + 1] = int(grey_list[a+1])
        grey_list[a + 2] = int(grey_list[a+2])
        # Calculation of grey value
        gray = sqrt(grey_list[a] ** 2 + grey_list[a+1] ** 2 + grey_list[a+2] ** 2)
        gray = int(gray)
        # Accounts for too high of value
        if (gray > 255):
            gray = 255
        # Adds 3 values
        gray_string += str(gray) + " "
        gray_string += str(gray) + " "
        gray_string += str(gray) + " "
    return gray_string


def remove_color(line, color):
    """
    Takes a line and a string that contains a primary color name. Assigns all the values of that color
    occurence in the string to zero, essentially removing the character.
    :param line(str): Line of color values that the color is removed from
    :param color(str): Indicates which color to remove.
    :return colorless_string(str): line with all values of color parameter equal to 0
    """
    start_value = 0
    colorless_string = ""
    # Checks for color to remove, alters start point accordingly
    if(color == "red"):
        start_value = 0
    elif(color == "green"):
        start_value = 1
    elif(color == "blue"):
        start_value = 2
    color_list = line.split()
    for a in range(start_value, len(color_list), 3):
        color_list[a] = 0
    # Cycles through list to make final string
    for a in range(len(color_list)):
        colorless_string += str(color_list[a]) + " "
    return colorless_string


def main():
    """
    1. Ask the user for an input file.
    2. Ask the user for an output file.
    3. List the possible image manipulation functions and ask the user to
       choose one of them. If they don't enter a valid choice, ask them again.
    4. Perform the requested manipulation on the input file and write the
       result to the output file in ppm format (don't forget to write out
       the header information!).
    """
    #Takes file names
    input_file_name = input("input file name: \n\t")
    output_file_name = input("output file name: \n\t")
    #Opens files with given names
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")
    #Lists possible things user can do
    modifications = "modifications are: \n 1. negate\n 2. greyscale\n 3. remove red\n 4. remove green\n 5. remove blue"
    print(modifications)
    #Prompts the user for what kind of modification they would like
    modification = int(input("enter the number of the desired modification:\n\t"))
    while(not (modification in range(1, 6))):
        print("please enter a valid number\n")
        modification = int(input("enter the number of the desired modification:\n\t"))
    # creates new output file that is a photo-negative of the input file
    if(modification == 1):
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        for line in input_file:
            output_file.write(negate(line))
    # creates a new output file that is a grayscale version of the input file
    if(modification == 2):
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        for line in input_file:
            output_file.write(grey_scale(line))
    # creates a new output file that is the input file with the color red removed
    if(modification == 3):
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        for line in input_file:
            output_file.write(remove_color(line, "red"))
    # creates a new output file that is the input file with the color green removed 
    if(modification == 4):
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        for line in input_file:
            output_file.write(remove_color(line, "green"))
    # creates a new output file that is the input file with the color blue removed 
    if(modification == 5):
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        output_file.write(input_file.readline())
        for line in input_file:
            output_file.write(remove_color(line, "blue"))
    # prints "done" and closes the input and output files
    print("done")
    input_file.close()
    output_file.close()
  


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
