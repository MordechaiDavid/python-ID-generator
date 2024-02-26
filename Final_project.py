
def chek_id_valid(id_number):
    """ checking valid ID.
    :param id_number: ID digits
    :type id_number: int
    :return: True if the ID is valid, and False if not.
    :rtype: boolean
    """
    List = [int(digit) for digit in str(id_number)]  # converting to a list
    gen = (2 if i % 2 == 0 else 1 for i in range(1, len(List)+1))
    multi_list = [i * next(gen) for i in List]
    return (lambda a, b: a + b)(sum(sum(int(digit) for digit in str(num))  # computing sum of all
                                    for num in multi_list if num > 9), sum(i for i in multi_list if i <= 9)) % 10 == 0


def id_generator(id_number):
    """ creates the next valid ID
    :param id_number: initial ID
    :type id_number: int
    :yield: next ID valid
    :yield type: int
    """
    id_number += 1
    while id_number < 999999999:
            if chek_id_valid(id_number):
                yield id_number
                id_number += 1
            else:
                id_number += 1


class IDIterator:
    """
    A class to generate ID numbers.
    """
    def __init__(self, id=99999999):
        """ initialization method.
        :param id: start- range(99999999+1)/input ID number
        :type id: int
        """
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        """ creates the next ID after what was received from the user/in range.
        :return: the next valid ID
        :raise: StopIteration: raises an exception
        """
        self._id += 1
        while chek_id_valid(self._id) is False:
            self._id += 1
        if self._id >= 999999999:
            raise StopIteration
        return self._id


def main():
    input_id_user = int(input("Enter ID:"))
    input_question = input("Generator or Iterator? (gen/it)?")
    iter_id_user = IDIterator(input_id_user)  # creating an iterator object
    gen_id_user = id_generator(input_id_user)  # creating a generator object

    if input_question == "it":  # using iterator
        try:
            for i in range(10):
                print(next(iter_id_user))
        except StopIteration:
            print("Out of range of valid ID numbers")

    elif input_question == "gen":  # using generator
        try:
            for i in range(10):
                print(next(gen_id_user))
        except StopIteration:
            print("Out of range of valid ID numbers")


if __name__ == "__main__":
    main()
