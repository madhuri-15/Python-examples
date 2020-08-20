#palindrome string or not.

def palindrome_str(string):
    
    string = string.lower()
    str1 = list(string)
    str2 = list(reversed(str1))
    
    #print(str1, str2)
    
    if str1 == str2:
        print("The string is Palindrome string")
    else:
        print("The string is Not a Palindrome string")
        
        
string = 'abcdcba'
palindrome_str(string)