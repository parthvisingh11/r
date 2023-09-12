def str_to_binary(string):
    # Initialize empty list to store binary values
    binary_list = []
     
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
         
    # Join the binary values in the list and return as a single string
    return ''.join(binary_list)

#write a function to convert string to array
def str_to_array(string):
    # Initialize empty list to store binary values
    array_list = []
     
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        array_list.append(char)
         
    # Join the binary values in the list and return as a single string
    return array_list

def binary_to_str(binary):
    # Split the binary string into a list of 8-bit binary values
    binary_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
     
    # Initialize empty string to store ASCII values
    ascii_string = ''
     
    # Iterate through each binary value in the list
    for binary_value in binary_list:
        # Convert binary value to ASCII character and append to string
        ascii_string += chr(int(binary_value, 2))
         
    return ascii_string

def array_to_str(array):
    # Split the binary string into a list of 8-bit binary values
    #binary_list = [binary[i:i+8] for i in range(0, len(binary), 8)]
     
    # Initialize empty string to store ASCII values
    ascii_string = ''
     
    # Iterate through each binary value in the list
    for binary_value in array:
        # Convert binary value to ASCII character and append to string
        ascii_string += binary_value
         
    return ascii_string

def string_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

def str_to_binary_array(array):
    for i in range(len(array)):
        array[i] = str_to_binary(array[i])
    return array

def str_to_array_array(array):
    array1 = [[0 for i in range(len(array))] for j in range(len(array))]
    for i in range(len(array)):
        array1[i] = str_to_array(array[i])
    return array1

#write a function to convert string to binary stream
def str_to_binary_stream(string):
    # Initialize empty list to store binary values
    binary_list = []
     
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
    
    #convert all the elements in the list to arrays
    for i in range(len(binary_list)):
        binary_list[i] = str_to_array(binary_list[i][::-1])
    
    #convert all the elements in the list to int
    for i in range(len(binary_list)):
        for j in range(len(binary_list[i])):
            binary_list[i][j] = int(binary_list[i][j]) 
    # Join the binary values in the list and return as a single string
    return binary_list

#write a function to convert binary stream to string
def binary_stream_to_str(binary_list):

    #convert all the elements in the list to arrays
    for i in range(len(binary_list)):
        binary_list[i] = str_to_array(binary_list[i][::-1])
    
    #convert all the elements in the list to int
    for i in range(len(binary_list)):
        for j in range(len(binary_list[i])):
            binary_list[i][j] = int(binary_list[i][j]) 
    # Join the binary values in the list and return as a single string
    return binary_list

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in range(len(s)):
        for j in range(len(s[ele])):
            str1 += s[ele][j] + " "
        str1 += "|"
 
    # return string
    return str1

#write a function to convert string to array
def str_to_array(string):
    # Initialize empty 2d list to store binary values
    array_list = []

    #create an empty 2d list
    for i in range(len(string)):
        array_list.append([])
    i, j = 0, 0
    # Iterate through each character in the string
    for char in range(len(string)):
        # Convert character to binary, pad with leading zeroes and append to list
        if(char == '|'):
            i += 1
        array_list[i][j] = string[char]
        j += 1
         
    # Join the binary values in the list and return as a single string
    return array_list
    