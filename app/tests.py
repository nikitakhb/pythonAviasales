import unittest

from store import SingletonStore


class TestStore(unittest.TestCase):
    def setUp(self) -> None:
        self.test_words = [
            'aabb',
            'abab',
            'baab',
            'baba',
        ]
        self.worlds = [
            'bbbaaa',
            'вижу',
            'живу',
        ] + self.test_words

    def test_singleton(self):
        store1 = SingletonStore()
        store2 = SingletonStore()
        self.assertEqual(store1, store2)

    def test_load_and_get_word(self):
        store = SingletonStore()
        store.set_list(self.worlds)
        self.assertEqual(
            store.get_anagrams('bbaa'),
            self.test_words
        )

    def test_load_and_get_word_not_from_words(self):
        store = SingletonStore()
        store.set_list(self.worlds)
        self.assertEqual(
            store.get_anagrams('Nikita'),
            []
        )
