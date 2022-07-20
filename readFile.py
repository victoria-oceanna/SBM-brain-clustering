# function for converting txt file to array of strings
def readFile(fileName):
    #open the file in read mode
    file_obj = open(fileName, "r") 
    #put the file into an array
    string_array = file_obj.read().splitlines() 
    #close the txt file
    file_obj.close()
    return string_array