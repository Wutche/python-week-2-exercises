import unittest
from main import *

class TestBitcoinFunctions(unittest.TestCase):
    def test_get_tx_count(self):
        self.assertEqual(get_tx_count(["tx1", "tx2"]), 2)
        self.assertEqual(get_tx_count([]), 0)

    def test_filter_large_txids(self):
        txs = ["tx1", "transaction2", "tx3"]
        filtered = filter_large_txids(txs, 4)
        self.assertEqual(filtered, ["transaction2"])

    def test_process_txids(self):
        txs = ["tx1", "abc", "tx3"]
        result = process_txids(txs)
        self.assertEqual(result, [(0, "tx1"), (2, "tx3")])

    def test_example_while_loop(self):
        self.assertEqual(example_while_loop(3), [0, 1, 2])
        self.assertEqual(example_while_loop(10), [0, 1, 2, 3, 4])

    def test_unpack_tuple(self):
        header = (123456, "0000000000000000000a7b7e", 1623456789)
        height, prev_hash, timestamp = unpack_tuple(header)
        self.assertEqual(height, 123456)
        self.assertTrue(prev_hash.startswith("0000"))
        self.assertIsInstance(timestamp, int)

    def test_dict_methods_example(self):
        block = {
            "height": 123456,
            "hash": "0000000000000000000a7b7e",
            "tx_count": 2500,
        }
        keys, values, items = dict_methods_example(block)
        self.assertIn("height", keys)
        self.assertIn(123456, values)
        self.assertIn(("tx_count", 2500), items)

    def test_multiple_assignment(self):
        a, b = multiple_assignment(1, 2)
        self.assertEqual((a, b), (2, 1))

    def test_set_example(self):
        addresses = ["addr1", "addr2", "addr1", "addr3"]
        s = set_example(addresses)
        self.assertIsInstance(s, set)
        self.assertEqual(len(s), 3)

    def test_bitcoin_transaction_and_wallet(self):
        tx1 = BitcoinTransaction("tx123", 0.5)
        tx2 = BitcoinTransaction("tx456", 1.0)
        wallet = Wallet()
        wallet.add_tx(tx1)
        wallet.add_tx(tx2)
        self.assertEqual(str(tx1), "Tx tx123 of 0.5 BTC")
        self.assertAlmostEqual(wallet.total_balance(), 1.5)

    def test_txid_generator(self):
        txs = ["tx1", "tx2"]
        gen = txid_generator(txs)
        self.assertEqual(next(gen), "tx1")
        self.assertEqual(next(gen), "tx2")
        with self.assertRaises(StopIteration):
            next(gen)

    def test_filter_txids_gen(self):
        txs = ["tx1", "abc", "tx3"]
        gen = filter_txids_gen(txs)
        self.assertEqual(list(gen), ["tx1", "tx3"])

if __name__ == "__main__":
    unittest.main()
