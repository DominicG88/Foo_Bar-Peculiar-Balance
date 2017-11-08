
# Peculiar balance
#
# Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
# obstacle.The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
# at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in
# some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this
# peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant
# mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.
# To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
# weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
# The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
# and so on. Each string is one of:
# "L" : put weight on left-hand side "R" : put weight on right-hand side "-" : do not use weight
# To ensure that the output is the smallest possible, the last element of the list must not be "-".
# x will always be a positive integer, no larger than 1000000000.

# Test cases
#
# Inputs: (int) x = 2
# Output: (string list) ["L", "R"]
#
# Inputs: (int) x = 8
# Output: (string list) ["L", "-", "R"]

from math import ceil

# Find the string of numbers in reverse order starting with the nearest power of 3
# The sum of all previous powers of 3 = (the next-1)/2, i.e. ...
# So every number is reachable by summing or subtracting the correct powers of 3.


# Tidy up the bellow, this section doesn't need a generator

def create_powers_list(number):

    new_power_function = powers_of_three_gen()
    next_power = new_power_function.__next__()
    power_list = []
    while sum(power_list) < number:
        power_list.append(next_power)
        next_power = new_power_function.__next__()

    return power_list


def powers_of_three_gen():
    n = 0
    while True:
        yield 3**n
        n += 1


def find_placement(number):
    return (number-1)/2


def cubed_route(number):
    # This is potentially much slower than itterating through a cubed list
    return number ** (1./3)


def which_side(number):
    if number>0:
        return 'R'
    elif number<0:
        return 'L'


# Use both versions then test speeds
# sign of remaining diff, +ve next weight goes on the opposite, -ve next weight goes on same side, greedy algorthm?

def answer(input_weight):

    output = []
    remaining_diff = input_weight
    powers = create_powers_list(input_weight)

    while remaining_diff!=0:

        largest_power = powers.pop(-1)
        if abs(remaining_diff) > find_placement(largest_power):
            output.insert(0,which_side(remaining_diff))
            remaining_diff = abs(remaining_diff) - largest_power
        else:
            output.insert(0,'-')

    return output

answer(6378628837)