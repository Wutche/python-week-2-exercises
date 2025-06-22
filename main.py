def get_tx_count(tx_list):
    """
    TODO: Return the number of transactions in the list.
    Input: List of transaction IDs (strings)
    Output: Integer count
    """

def filter_large_txids(tx_list, min_length):
    """
    TODO: Return a list of txids with length greater than or equal to min_length.
    Input: List of txids (strings), minimum length (int)
    Output: Filtered list of strings
    """

def process_txids(tx_list):
    """
    TODO: Iterate over txids and return list of tuples (index, txid)
    only for txids that start with 'tx'. Use enumerate, continue as needed.
    Input: List of txids (strings)
    Output: List of (int, string) tuples
    """

def example_while_loop(limit):
    """
    TODO: Using a while loop, build a list of integers from 0 up to limit.
    Break the loop if integer reaches 5.
    Input: Integer limit
    Output: List of integers
    """

def unpack_tuple(block_header):
    """
    TODO: Unpack the tuple representing a Bitcoin block header (height, previous hash, timestamp).
    Input: Tuple (int, str, int)
    Output: Unpacked tuple values
    """

def dict_methods_example(block):
    """
    TODO: Given a dict representing a Bitcoin block with keys 'height', 'hash', and 'tx_count',
    return three lists: keys, values, and items.
    Input: Dict
    Output: Tuple of (list, list, list)
    """

def multiple_assignment(a, b):
    """
    TODO: Demonstrate multiple assignments and swapping two variables.
    Input: two integers
    Output: Tuple of two ints (swapped)
    """

def set_example(addresses):
    """
    TODO: Given a list of Bitcoin addresses with duplicates,
    return a set of unique addresses.
    Input: List of strings
    Output: Set of strings
    """


class BitcoinTransaction:
    def __init__(self, txid, amount):
        """
        TODO: Initialize transaction with txid (string) and amount (float).
        """

    def __str__(self):
        """
        TODO: Return string representation: "Tx {txid} of {amount} BTC"
        """

class Wallet:
    def __init__(self):
        """
        TODO: Initialize an empty list to hold transactions.
        """

    def add_tx(self, tx):
        """
        TODO: Add a BitcoinTransaction to the wallet's transaction list.
        """

    def total_balance(self):
        """
        TODO: Calculate and return the sum of amounts of all transactions.
        Output: Float
        """


def txid_generator(tx_list):
    """
    TODO: Yield each txid from the list one by one.
    Input: List of strings
    """

def filter_txids_gen(tx_list, prefix="tx"):
    """
    TODO: Yield txids from list that start with given prefix.
    Default prefix is 'tx'.
    Input: List of strings, prefix string
    """
