"""Functions to manage a users shopping cart items."""
from IPython.core.events import pre_run_cell


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_cart = {}
    for note in notes:
        shopping_cart[note] = shopping_cart.get(note, 0) + 1
    return shopping_cart


def update_recipes(ideas: dict, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for item in recipe_updates:
        item_to_update = item[0]
        new_ingredients = item[1]


        ideas[item_to_update] = new_ingredients

    return ideas




def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item, quantity in cart.items():

        location_data = aisle_mapping[item]

        quantity_as_list = [quantity]

        combined_list = quantity_as_list + location_data
        fulfillment_cart[item] = combined_list
    return dict(sorted(fulfillment_cart.items(), reverse=True))







def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart:
    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    # {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
    # {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}

    # {'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False], 'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]}


    # dict_keys(['Orange', 'Milk', 'Banana', 'Apple'])
    # 0
    # 2
    # 12
    # 10
    # [1, 2, 3, 2]

    product_cart_list = fulfillment_cart.keys()
    for product in product_cart_list:
        quantity_to_send = fulfillment_cart.get(product)[0]
        quantity_on_stoke = store_inventory[product][0] - quantity_to_send
        if quantity_on_stoke <= 0:
            store_inventory[product][0] = "Out of Stock"
        else:
            store_inventory[product][0] = quantity_on_stoke
    return store_inventory

