#   Given a text, find the decoded text using the shift 
#   To perform this task, first decode the character in the string LETTERS
#   Then find the shift of the characters in the cipher text 
#       This can be done by finding the most occuring character in the text
#           And finding the shift from that character to "e"
#           We use "e" because "e" is the most occuring character 
#       In order to do this use the enumerate method 
#   Then using the most occuring character and shift print the decoded text
#   Use ignore to ignore the spaces in the text 
#       If the spaces aren't ignored they will be the most occurring char
#   Call the defined functions in order to decode the text 
#   Using a while loop ask the user if the decoded text is readable or not 
#       if not readable run all the process again until the user inputs yes 
#   End the program if the text is readable in english 


import string #importing string because there is use of string LETTERS 

index = 0
LETTERS = string.ascii_uppercase #converts the string LETTERS to uppercase 

#decodes the character in the string LETTERS 
def decode_char(ch, shift): 
    ch = ch.upper()
    if ch not in LETTERS:
        return ch
    else:
        index = LETTERS.find(ch) #finds the index of ch in string LETTERS
        plainTxtChar = index
        cipherTxtChar = (plainTxtChar + shift) % 26 #Converts cipher text 
                                                #index in terms of plain text 
        return LETTERS[cipherTxtChar] 

#finds the shift of the string(s) from the most occurring character(e)
def get_shift(s, ignore):
    index = 0 #defines index 
    #s = s.replace(" ", "")
    s = s.upper()
    char_most = "" #defines the most occurring character 
    char_times = 0 #defines the number of times that character occurs in s
    for i, ch in enumerate(LETTERS): 
        if ch in ignore:
            continue
        #counts which character occurs the most in the string(s)
        count = s.count(ch) 
        if count > char_times: 
            char_most = ch
            char_times = count
            index = i
    shift = 4 - index #index of e is 4 
    return shift, char_most 
    
#function that prints the decoded text 
def output_plaintext(s, shift):
    s = s.upper()
    s_new = "" #defines the new decoded string 
    for ch in s:
        ch_new = decode_char(ch, shift) 
        s_new += ch_new #updates new string with the new character 
    print(s_new) #prints the decoded text 

#where most part of the process occurs 
def main():
    print("Cracking a Caesar cypher.")
    cipher = input("\nInput cipherText: ") #input the text to be decoded 
    cipher = cipher.upper() #converts the text in uppercase 
    ignore = "" #defines the ignore 
    shift, char_most = get_shift(cipher, ignore) #calls the get_shift function
    ignore += char_most #updates the ignore with most occurring ch 
    output_plaintext(cipher, shift) #calls the output_plaintext function
    read = input("\nIs the plaintext readable as English? (yes/no): ")
    read = read.lower()
    
    while read != "yes": #while loop if the text is not readable 
        #all the decoding process occurs again until the text is readable
        shift, char_most = get_shift(cipher, ignore) 
        ignore += char_most
        output_plaintext(cipher, shift)
        read = input("\nIs the plaintext readable as English? (yes/no): ") 
        read = read.lower()
    #once the text is readable it prints done and ends the program
    print("\nDone.")

#calls the main function 
if __name__ == "__main__":
    main()
    
