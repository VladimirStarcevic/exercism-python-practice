"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
from pycparser.c_ast import While


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    new_list = []
    for _ in range(3):
        new_list.append(number)
        number += 1
    return new_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total_card = 0
    num_of_cards = len(hand)
    for cart in hand:
        total_card += cart
    return float(total_card/ num_of_cards)



def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    if not hand:
        raise ValueError("Cannot calculate the median of an empty list")
    n = len(hand)
    average_value_of_cards = card_average(hand)
    first_lats_avg = float((hand[0] + hand[n - 1]) / 2)

    sorted_data = sorted(hand)
    n = len(sorted_data)

    median_avg = 0.0
    if n % 2 == 1:

        median_avg = sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median_avg = (mid1 + mid2) / 2
    is_first_last_avg_equal = (first_lats_avg == average_value_of_cards)
    is_median_equal = (median_avg == average_value_of_cards)

    return is_first_last_avg_equal or is_median_equal




def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    sum_even = 0
    sum_odd = 0
    count_even = 0
    count_odd = 0
    for i in range(len(hand)):
        if i % 2 == 0:
            sum_even += hand[i]
            count_even += 1
        else:
            sum_odd += hand[i]
            count_odd += 1
    avg_even_idx = float(sum_even/count_even)
    avg_odd_idx = float(sum_odd/count_odd)
    return avg_even_idx == avg_odd_idx



def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    last_card = hand[len(hand) - 1] == 11
    new_hand = list(hand)
    if last_card:
        new_hand[len(new_hand) - 1] = 11 * 2
        return new_hand
    return hand


