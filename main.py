#function to check if two strings are 
#anagram or not

def find_anagram(word, anagram):
    
    # the sorted strings are checked
    if(sorted(word)==sorted(anagram)):
        print(True)
    else:
        print(False)
        
#Example 1
find_anagram("hello", "check")
#Example 2
find_anagram("Binary", "Brainy")
    