
import sys, re, random

class Grammatics:

    def __init__(self:classmethod, file_name:str):
        try:
            self.VN = []
            self.VT = []
            self.S = []
            self.Productions = []

            self.read_from_file(file_name)

            self.validating()

            print(self.S, end=' ')
            self.generating_the_word(self.S)
            
            try:
                self.VN.clear()
            except:
                pass
            try:
                self.S.clear()
            except:
                pass

            self.VT.clear()
            self.Productions.clear()
        except Exception as err:
            try:
                self.VN.clear()
            except:
                pass
            try:
                self.S.clear()
            except:
                pass

            self.VT.clear()
            self.Productions.clear()
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def read_from_file(self:classmethod, file_name:str):
        """
        This function is for reading the content of rules and vocabulary for the Generative Grammatics from the txt file
        Param file_name: str with name of the txt file
        Returns: None
        """    
        try:
            are_they_rules = False

            with open(file_name, 'r') as file_Reading:
                for line in file_Reading:
                    if not are_they_rules:
                        element = line.strip().split('{')
                        #G = ({S}, {a,b}, S, P)
                        #G = (VN, VT,S,P)
                        self.VN = element[1].split('}')[0].split(',')
                        self.VT = element[2].split('}')[0].split(',')
                        self.S = element[2].split('}')[1].split(',')[1]
                        #self.Productions = element[2].split('}')[1].split(',')[len(element[2].split('}')[1].split(','))-1].split(')')[0]
                        are_they_rules = True

                    else:
                        arrow_index = line.find('->')
                        self.Productions.append(line[:int(arrow_index)].strip())
                        self.Productions.append(line[int(arrow_index)+2:].strip())

            txt_file_stage_flag = True
            self.display_content( txt_file_stage_flag)
        
        except Exception as err:
            if not file_Reading.closed:
                file_Reading.close()
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def display_content(self:classmethod, txt_file_stage_flag:bool = False, word_modified:str = "None"):
        """
        This function is for displaying the content of rules and vocabulary for the Generative grammatics from the txt file and the modification of the word
        Param txt_file_stage_flag: bool, flag for printing the content from the txt file
        Param word_modified: str, for printing all the words in the process
        Returns: None
        """
        try:
            if txt_file_stage_flag:

                print("Fie gramatica: G = ({", end='')
                for element in self.VN:
                    if element == self.VN[-1]:
                        print(str(element), end='')
                    else:
                        print(str(element), end=', ')

                print("},{", end='')
                for element in self.VT:
                    if element == self.VT[-1]:
                        print(str(element), end='')
                    else:
                        print(str(element), end=', ')

                print("},", end='')
                print(str(self.S) + ", P), P conținând următoarele producții:")
                index_enumerate = 1
                for index, element in enumerate(self.Productions):
                    
                    if index % 2 == 0:
                        print("(" + str(index_enumerate) +") "+ str(element), end=' -> ')
                        index_enumerate = index_enumerate + 1
                    else:
                        print(str(element))


            else:
                print("=> " + str(word_modified) , end=' ')
                self.generating_the_word(word_modified)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def validating(self:classmethod):
        """
        This function is for validating the grammatic base on some hardcoded rules
        Returns: True if all the elements in the grammatics verify all the conditions, otherwise false
        """
        try:
            if set(self.VN) & set(self.VT):
                print("The inserted grammatics does not comply with the First Rule")
                return False
            
            second_rule = re.search(re.escape(self.S), str(self.VN))
            if str(second_rule) == "None":
                print("The inserted grammatics does not comply with the Second Rule")

                return False
            
            for index, elem in enumerate(self.Productions):
                if index % 2 == 0:
                    third_rule = re.search(re.escape(elem), str(self.VN))
                    if  str(third_rule) == "None":
                        print("The inserted grammatics does not comply with the Third Rule")
                        return False
                    
            fourth_rule = re.search(re.escape(self.S), str(self.Productions))
            if str(fourth_rule) == "None":
                print("The inserted grammatics does not comply with the Fourth Rule")
                return False
            
            for elem in self.Productions:
                if len(elem) > 1:
                    for every_str_from_elem in elem:
                        fifth_rule = re.search(re.escape(every_str_from_elem), str(self.VT) + str(self.VN))
                        if str(fifth_rule) == "None":
                            print("The inserted grammatics does not comply with the Fifth Rule")
                            return False
                else:
                    fifth_rule = re.search(re.escape(elem), str(self.VT) + str(self.VN))
                
                if str(fifth_rule) == "None":
                    print("The inserted grammatics does not comply with the Fifth Rule")
                    return False
                
            
            return True
        except Exception as err:

            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def generating_the_word(self:classmethod, derivated_word):
        """
        This function is for modificating the content of the word 
        Param derivated_word: str, word which we would apply the modification
        Returns: True, if is the finished word
        """
        list_of_possible_positions = []
        list_of_possible_rules = []

        for index_produt, element_product in enumerate(self.Productions):
            if index_produt % 2 == 0:
                for index_word, word_element in enumerate(derivated_word):
                    if element_product == word_element:

                        if not (index_word in list_of_possible_positions):
                            list_of_possible_positions.append(index_word)

                        if not ((index_produt+1) in list_of_possible_rules):
                            list_of_possible_rules.append(index_produt+1)
        
        try:
            random_rule = random.choice(list_of_possible_rules)
            random_position = random.choice(list_of_possible_positions)

            list_of_possible_rules.clear()
            list_of_possible_positions.clear()
            if not (str(self.Productions[random_rule]) == "*"):
                derivated_word = derivated_word[:random_position] + str(self.Productions[random_rule]) + derivated_word[random_position + 1:]
            else:
                derivated_word = derivated_word[:random_position] + derivated_word[random_position + 1:]

            self.display_content(False, derivated_word)
        
        except:
            return True
        
Grammatics("Generative_grammatics.txt")


