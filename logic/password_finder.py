#This file define the class Password_finder and her methods
#No repeated characters are allowed

import unittest

class Password_finder:
    """
    This class wrap the process of obtain a password from the sequences
    """

    def __init__(self, sequences):
        """
        Constructor of the class Password_finder
        _password_list (list): Contain a list of each password caracter.
        sequences (list): List of strings with the sequences obtained from the user file.
        status (bool): Status about the process
        password (string): Contain the shortest founded password
        """
        self._password_list = []
        self.sequences = sequences
        self.status = False
        self.password = ""

    def find_password(self):
        """
        Method to wrap the password detection process

            Parameters:
                    Nothind

            Returns:
                    (str) the password detected
        """

        #Initialization of the password list with  the first sequence [0]
        self._password_list = [i for i in self.sequences[0]]

        #Iterate over the n-1 remainig sequences
        for sequence in self.sequences[1:]:

            #Obtain the list with the indexes of the _password_list characters 
            # that are in the current sequence. -1 if not founded
            indexes = self.find_indexes(sequence)

            #Count not founded values to validade some scenarios
            not_founded_values = indexes.count(-1)

            if not_founded_values == len(sequence):
                #All characters are new, sequence moved to the end
                self.sequences.append(sequence)
                continue

            elif not_founded_values == len(sequence)-1:
                #Only one character is in the _password_list at this time
                # no order routine needed.
                self.insert_new_characters(sequence, indexes)
                continue

            elif not_founded_values == 0:
                #All characters are in the _password_list only order needed
                self.sort_sequence(sequence, indexes)
                continue

            # If are atleast two characters in the _password_list order the list
            self.sort_sequence(sequence, indexes)

            #Update indexes after sort - order routine to the _password_list
            indexes = self.find_indexes(sequence)

            #insert the remaining characters of the sequence
            self.insert_new_characters(sequence, indexes)

        #After all the sequences validated wrap the _password_list to the password variable
        self.password = ''.join(self._password_list)
        self.status = True

        return self.password

    def find_indexes(self, sequence):
        """
        Method to find a vector with the same size of the sequence
        with the index of the elementes in _password_list, -1 if not founded

            Parameters:
                    sequence (str): a single sequence

            Returns:
                    indexes (list): numerical list with the detected indexes
        """

        indexes = []

        for character in sequence:

            try:
                #If the element is in the list, append the index
                index = self._password_list.index(character)
                indexes.append(index)

            except ValueError:
                #Manage the error appending -1 to indexes
                indexes.append(-1)

        return indexes

    def sort_sequence(self, sequence, indexes):
        """
        Sort the _password_list with the given information of the current sequence

            Parameters:
                    sequence (str): a single sequence
                    indexes (list): list with the index of the current sequences

            Returns:
                    Nothing
        """

        for i, index in enumerate(indexes):

            if i == 0:
                #Only the 2nd to the last element can be compared with the previous
                continue

            if indexes[i-1] != -1 and indexes[i] != -1 and indexes[i-1] > indexes[i]:
                #The previos element and the current element are different of -1 and are unsorted
                #Insert the element in the correct position and delete the previous (first occurencie)
                self._password_list.insert(self._password_list.index(sequence[i-1]) + 1, sequence[i])
                self._password_list.remove(sequence[i])

    def insert_new_characters(self, sequence, indexes):
        """
        Insert the new elements into the _password_list in the correct position

            Parameters:
                    sequence (str): a single sequence
                    indexes (list): list with the index of the current sequences

            Returns:
                    Nothing
        """

        #Auxiliar variables to manage the process
        to_be_inserted = []
        last_index_found_in_password = -1
        insert_position = 0
        offset = 0                #To record if and element was inserted before the current element

        for i, index in enumerate(indexes):

            if index == -1:
                #If the character sequence[i] is not in the _password_list
                try:
                    #Evaluate the next character can result in a IndexError exception
                    if indexes[i+1] == -1:
                        #Next element also no in the password
                        to_be_inserted.append(sequence[i])
                    else:
                        #Next element in the sequence is in the password
                        to_be_inserted.append(sequence[i])
                        index_to_insert = indexes[i+1]

                        while len(to_be_inserted) > 0:
                            #insert the remaining elements in the position before the element that is the _password_list
                            self._password_list.insert(index_to_insert, to_be_inserted.pop())

                            #Update indexes (only if is not -1)
                            indexes = [i if i == -1 else i + 1 for i in indexes]
                            offset += 1

                except IndexError:
                    #No element [i+1] but the current character is not in the _password_list
                    to_be_inserted.append(sequence[i])

                    #calculate the position to insert the character
                    insert_position = last_index_found_in_password + offset + 1

                    #iterate over the remaining elements
                    while len(to_be_inserted) > 0:
                        self._password_list.insert(insert_position, to_be_inserted.pop(0))
                        insert_position += 1

            else:
                #The current character are in the _password_list, store index to future use.
                last_index_found_in_password = index


class Insert_new_charactersTests(unittest.TestCase):
    """
    The next test evaluate all the scenarios of founded and not founded characters
    between two consecutives sequences, to evaluate the find_password routine
    """

    def test_first_two_new(self):
        sequences = ["568", "126"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "51268")

    def test_first_and_last_new(self):
        sequences = ["568", "157"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "15768")

    def test_two_last_new(self):
        sequences = ["568", "612"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "56128")

    def test_first_new(self):
        sequences = ["568", "268"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "5268")

    def test_middle_new(self):
        sequences = ["568", "526"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "5268")

    def test_last_new(self):
        sequences = ["568", "589"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "5689")

    def test_all_new(self):
        sequences = ["568", "123"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        #If the new sequence is totally new is sended to the end until
        #a common caracter comes in another sequence
        self.assertEqual(password, "568")

    def test_all_in_list(self):
        sequences = ["56874", "584"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "56874")

class Sort_charactersTests(unittest.TestCase):
    """
    The next test evaluate sequences that requiere sort the previos password
    """

    def test_sort_1(self):
        sequences = ["568", "862"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "5862")

    def test_sort_2(self):
        sequences = ["568", "165"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "1658")

    def test_all_in_list_unsorted(self):
        sequences = ["56874", "547"]
        pass_finder = Password_finder(sequences)
        password = pass_finder.find_password()

        self.assertEqual(password, "56847")

class File_decodeTests(unittest.TestCase):
    """
    This test evaluate the requiered file with the 50 sequences
    """

    def test_keylog_file(self):
        keylog_file = open("keylog.txt", "r")

        #Reading and converting to a list of strings
        data_set = keylog_file.read()
        data_list = data_set.splitlines()
        keylog_file.close()

        pass_finder = Password_finder(data_list)
        password = pass_finder.find_password()

        print("The founded password is: {}".format(password))

        self.assertEqual(password, "73162890")


if __name__ == "__main__":

    unittest.main()
