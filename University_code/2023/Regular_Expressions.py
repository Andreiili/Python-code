
import re
# https://docs.python.org/3/howto/regex.html#regex-howto
# https://docs.python.org/3/library/re.html#re.finditer 

def first_is_a_Real_number_or_Integer(string: str)-> print:
    """
    This function is for finding if a number is real or integer
    Param string: string with the number that we want to verify in which category it does enter
    Returns: Print with in which category does the string enters
    """

    if ( not re.findall(r'\D', string) ) or ( re.findall(r'\D', string) == ['-'] ):
        return(print("număr întreg"))
    elif ( re.findall(r'\D', string) == ['-', ','] ) or ( re.findall(r'\D', string) == [','] ): #[','] for 421,34, or ['-', ','] for -421,34 
        return(print("număr real"))
    else:
        return(print("string-ul introdus nu este nici întreg, nici real"))


class second_verify_text:

    def __init__(self:classmethod, file_name:str):
        try:
            with open(file_name, 'r') as file_Reading:
                vocabulary = []

                for line in file_Reading:
                    vocabulary.extend( line.strip().split(',') )
                    print("input:", vocabulary)
                    self.first_requirement(line.strip())
                    self.second_requirement(vocabulary)
                    self.third_requirement(line.strip())

            
        except Exception as err:
            if not file_Reading.closed:
                file_Reading.close()
            print(f"Unexpected {err=}, {type(err)=}")
            raise


    def first_requirement(self:classmethod, list_of_all_elements:str):
        """
        Check how many words have an even number of "a"s at the beginning
        Param list_of_all_elements: string with all the elements that we propose to verify
        Returns: How many times does the string has words that contains a of even times
        """

        pattern_first_requirement = r'\b(?:a{2})\w*\b'
        number_of_words_with_even_two = 0
        list_of_elements = re.findall(pattern_first_requirement, list_of_all_elements.strip())

        for element in list_of_elements:
            add = 0
            for is_it_a in re.findall(r'\w',element):
                if is_it_a  == "a":
                    add = add + 1
            if add % 2 == 0 :
                number_of_words_with_even_two = number_of_words_with_even_two + 1

        print("a: ",  number_of_words_with_even_two)

    def second_requirement(self:classmethod, list_of_all_elements:str):
        """
        Replace each word that begins and ends with "b" with its length
        Param list_of_all_elements: string with all the elements that we propose to verify
        Returns: The list with the modified elements
        """
        pattern_first_requirement = r'\Ab.*b\Z'
        for elements in range(0,len(list_of_all_elements),1):
            if re.match(pattern_first_requirement, list_of_all_elements[elements]):
                list_of_all_elements[elements] = list_of_all_elements[elements].replace('b', str(len(list_of_all_elements[elements])))
        print("b: ",  list_of_all_elements)

    def third_requirement(self:classmethod, list_of_all_elements:list):
        """
        Concatenate all invalid words (there are no words beyond the given vocabulary)
        from the file, if any
        Param list_of_all_elements: list of str with all the elements that we propose to verify
        Returns: The concatenated string with all the invalid words
        """
        pattern_third_requirement_first_search = r'\w*[e-z]\w*|\w*[A-Z]\w*'
        
        first_search_list = re.findall(pattern_third_requirement_first_search, list_of_all_elements)
        result = ' '.join(first_search_list)
        print("c:",result)


def third_check_strong_password(password:str)-> print:
    """
    This function is for finding if a password is strong or not
    Param password: string with the password that we want to verify
    Returns: Print with if the password is strong or not
    """
    if (not re.search(r'[#$%]', password)) or ( not re.search(r'[A-Z]', password) ) or ( (len(re.findall(r'', password)) - 1 )< 10 ) or ( not re.search(r'\d{2}', password) ):
        return print("Password it is not strong")

    return print("Password it is strong")


print("First Question: ")
print("4214 = ",end=' ') 
first_is_a_Real_number_or_Integer("4214")
print("42,14 = ",end=' ') 
first_is_a_Real_number_or_Integer("42,14")
print("42,1a4 = ",end=' ') 
first_is_a_Real_number_or_Integer("42,1a4")

print("Second Question: ")
second_verify_text("Regular_expressions.txt")

print("Third Question: ")
print("fawfwafaASD3421# = ",end=' ') 
third_check_strong_password("fawfwafaASD3421#")
print("fa21# = ",end=' ') 
third_check_strong_password("fa21#")