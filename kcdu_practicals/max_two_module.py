# Create a self-executable module to find the bigger of the two numbers
import json

class MaxTwo:

    def __init__(self):
        pass

    @staticmethod
    def greater_of_two(self, first_number, second_number):
        bigger_number = 0
        if first_number > second_number:
            bigger_number = first_number
            print("Entered number {} is greater than {}".format(first_number, second_number))
        elif first_number == second_number:
            bigger_number = first_number
            print("Entered number", first_number, " and ", second_number, " are same")
        else:
            bigger_number = second_number
            print("Entered number {} is smaller than {}".format(first_number, second_number))
        return  bigger_number

    def take_input(self):
        print("Enter the first number: ")
        first_number = int(input())
        print("Enter the second number: ")
        second_number = int(input())
        return first_number, second_number


if __name__ == "__main__":
    mt = MaxTwo()
    first_number, second_number = mt.take_input()
    b = mt.greater_of_two(first_number, second_number)





















