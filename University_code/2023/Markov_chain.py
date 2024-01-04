
import sys,re
class Markov:

    def __init__(self:classmethod, file_name:str):
        try:
            self.markov_vocabulary = []
            self.markov_rules = []
            self.flag_another_word:bool = True
            self.read_from_file(file_name)


            while bool(self.flag_another_word):

                #self.flag_another_word:bool = input("Do you wanna read a word from the txt_file?(Input 1 = True): ") == "1"
                if not self.flag_another_word:
                    continue

                try:
                    user_input_word = str(input("Introduce the word in which we want to apply the markov chain: "))
                    print(user_input_word, end=' ')
                    if not self.validating(user_input_word):
                        raise ValueError
                except ValueError as ve:
                    print(f"Error: {ve}. Please enter a valid word for markov chain.")
                    continue

                

                self.derivating(user_input_word)

            self.markov_rules.clear()
            self.markov_vocabulary.clear()
            self.initial_rule.clear()
            self.resulted_rule.clear()
        except Exception as err:
            self.initial_rule.clear()
            self.resulted_rule.clear()
            self.markov_rules.clear()
            self.markov_vocabulary.clear()
            print(f"Unexpected {err=}, {type(err)=}")
            raise
    
    def read_from_file(self:classmethod, file_name:str):
        """
        This function is for reading the content of rules and vocabulary for the Markov Chain from the txt file
        Param file_name: str with name of the txt file
        Returns: None
        """    
        try:
            self.initial_rule = []
            self.resulted_rule = []
            with open(file_name, 'r') as file_Reading:
            
                are_they_rules = False
                for line in file_Reading:

                    if line.strip() == "Rules:":
                        are_they_rules = True
                        continue
                    if not are_they_rules:
                        self.markov_vocabulary.extend( line.strip().split() )
                    else:
                        self.markov_rules.extend( line.strip().split() )


                        arrow_index = line.find('->')
                        self.initial_rule.append(line[:int(arrow_index)].strip())
                        self.resulted_rule.append(line[int(arrow_index)+2:].strip())
                        
            txt_file_stage_flag = True
            self.display_content( txt_file_stage_flag)
            
        except Exception as err:
            if not file_Reading.closed:
                file_Reading.close()
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def display_content(self:classmethod, txt_file_stage_flag:bool = False, word_modified:str = "None", index_of_law:int = 1):
        """
        This function is for displaying the content of rules and vocabulary for the Markov Chain from the txt file and the modification of the word
        Param txt_file_stage_flag: bool, flag for printing the content from the txt file
        Param word_modified: str, for printing all the words in the process
        Param index_of_law: int, for which law was use in the process of modification
        Returns: None
        """
        try:
            if txt_file_stage_flag:

                print("SR=({", end='')
                for index, element in enumerate(self.markov_vocabulary):
                    if index ==( len(self.markov_vocabulary) -1):
                        print(str(element), end='')
                    else:
                        print(str(element), end=', ')

                print("},{", end='')
                for index, element in enumerate(self.markov_rules):
                    if index ==( len(self.markov_rules) -1):
                        print(str(element), end='')
                    else:
                        print(str(element), end=', ')

                print("})")



            else:
                print("|-" + str(index_of_law + 1) + "--" + str(word_modified) , end=' ')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def validating(self:classmethod, word:str):
        """
        This function is for validating the word in the vocabulary from the Markov Chain
        Param word: str, checks if all the elements in the word are in the vocabulary read from the txt file
        Returns: True if all the elements in the str are inside the vocabulary, otherwise false
        """
        try:
            for element_in_str in word:
                matches = re.search(re.escape(element_in_str), str(self.markov_vocabulary))
                if str(matches) == "None":
                    return False
            return True
        except Exception as err:
            self.markov_rules.clear()
            self.markov_vocabulary.clear()
            print(f"Unexpected {err=}, {type(err)=}")
            raise


    def derivating(self:classmethod, word_for_derivating:str):
        """
        This function is for derivating the content of the Markov Chain
        Param word_for_derivating: select the word which we want to derivate
        """
        try:
            while( not (word_for_derivating.endswith('.') or word_for_derivating.startswith('.'))):
                there_has_been_any_modification = False
                for index, rule in enumerate(self.initial_rule):
                    for index_word, particular_element in enumerate(word_for_derivating.strip()):

                        if particular_element == rule:
                            there_has_been_any_modification = True

                            
                            resulted_rule_value = str(self.resulted_rule[index]).strip()

                            if resulted_rule_value != '*':
                                word_for_derivating = word_for_derivating[:index_word] + resulted_rule_value + word_for_derivating[index_word+1:] 
                            elif len(word_for_derivating) == 1:
                                word_for_derivating = "*"
                            else:
                                if index_word > (len(word_for_derivating) - 1):
                                    word_for_derivating = word_for_derivating[:index_word - 1] + word_for_derivating[index_word:]
                                else:
                                    word_for_derivating = word_for_derivating[:index_word] + word_for_derivating[index_word + 1:]

                            self.display_content(False, word_for_derivating, index)
                            
                        if (word_for_derivating.endswith('.') or word_for_derivating.startswith('.')):
                            print()
                            return True

                    if (word_for_derivating.endswith('.') or word_for_derivating.startswith('.')):
                        print()
                        return True
                if not there_has_been_any_modification:
                    print()
                    return True
                

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

Markov("markov_chain.txt")

