#is_vowel deines a single parameter, p_one parameter obne is a string and will return a boolean
def is_vowel(p_one):
    vowels = 'aeiou'
    # loop each letter in vowels
    if p_one.lower() in vowels:
        #if it is, return true
        return True
    else:
        #if it is not, return false
        return False


#  is_constant defines a single parameter, c_param is a string and will return a boolean
def is_consonant(c_param):
    #if c_parm is in consonants list
    if c_param.lower() in consonants:
        #if it is, return true
        return True
    else:
        #if its not, return false
        return False
# creating the consonant variables with a list of consonants
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']



#up_word defines a single parameter, w_parameter (word) is a string and returns a string
def up_word(w_param):
    #checks if w_param's first letter is a constinant
    if is_consonant(w_param[0]):
        #if it is, it capitalizes the first letter
        return w_param.capitalize()
    else:
        #if its not, it returns the original string
        return w_param
    

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return'F'
    
def handle_commas(n_format):
    return int(n_format.replace(',',''))


def normalized_int(input):
    output =''
    for ints in input:
        if ints.isdigit() or ints == '.':
            output += ints
    return output

print(normalized_int('$2,097.02'))
