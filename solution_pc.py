# Solution

# The sum of all previous powers of 3 = (the next-1)/2, i.e. sum(k=1:n-1)f(k) = (f(n)-1)/2, where f(k) = 3^k
# So every number is reachable by summing or subtracting the correct powers of 3.
# sign of remaining diff, +ve next weight goes on the opposite, -ve next weight goes on same side


def answer(input_weight):

    # Set the input weight as the remaining unbalance on the scales
    # Create the powers of 3 list and set the output to be same length,
    # as we know we need an symbol for each weight.

    remaining_unbalance = input_weight
    powers, power_length = create_powers_list(input_weight)
    scale_out = ['-']*power_length
    counter = 1

    # Repeat algorithm until scales are balanced

    while remaining_unbalance != 0:

        # Check the sign of the unbalanced scales, and determine which side
        # of the scales the next weight needs to be placed (if at all)
        side, sign = _which_side(remaining_unbalance)

        # Work from the largest power in the array and work towards smallest
        largest_power = powers.pop(-1)

        # Check if the absolute value of the unbalanced scales is larger than the
        # (next largest power -1)/2, if so we need to use this weight to balance scales.

        if abs(remaining_unbalance) > _lower_bound(largest_power):
            scale_out[power_length-counter] = side

            # If weight is placed re-calculate the scale balance
            remaining_unbalance = remaining_unbalance + (sign*largest_power)

        counter += 1

    return scale_out


def create_powers_list(number):
    n = 0
    power_list = []
    while sum(power_list) < number:
        power_list.append(3**n)
        n += 1

    return power_list, len(power_list)


def _lower_bound(number):
    return (number-1)/2


def _which_side(number):
    if number > 0:
        return 'R', -1
    elif number < 0:
        return 'L', 1
