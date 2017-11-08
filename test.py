import solution_pc, solution_pc2
import timeit
import pdb
import pytest
import random

# Use cProfile from command line to get time breakdown

def unpack_scales(scale_list,input_scale):

    power_list, length_list = solution_pc.create_powers_list(input_scale)
    scale_balance = input_scale
    weights_used = 0

    print('Putting %d on the left scale' % input_scale)
    for n,m in enumerate(scale_list):
        scale_balance = scale_balance + (power_list[n]*scale_position(m,power_list[n]))
        if m != '-':
            weights_used += 1

    return scale_balance,weights_used


def scale_position(side,weight):

    if side == 'R':
        print('adding %d to the right' % weight)
        return -1
    elif side == 'L':
        print('adding %d to the left' % weight)
        return 1
    else:
        return 0

def main():

    # Check 200 random inputs up to max, test this 100 times
    max_scale = 39872982929282822829082398323290786328768723737699877383765

    start_time = timeit.default_timer()
    for n in range(1):

        input_scale = random.randrange(max_scale)
        scale_list = solution_pc.answer(input_scale)
        scale_balance, weights_used = unpack_scales(scale_list, input_scale)
        print(scale_balance, weights_used)
        assert scale_balance ==0

    stop_time = timeit.default_timer()
    print(stop_time-start_time)

if __name__ == "__main__":

    main()
