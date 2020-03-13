from collections import Counter, defaultdict


class SingletonStore:
    def __new__(cls):
        if not hasattr(cls, 'store'):
            cls.store = super().__new__(cls)
        return cls.store

    def set_list(self, words):
        store_words = defaultdict(lambda: [])
        for w in words:
            word = Words(w)
            store_words[word.hash].append(word.word)
        setattr(self, 'hash_map_words', store_words)

    def get_anagrams(self, word):
        obj = Words(word)
        return getattr(self, 'hash_map_words', {}).get(obj.hash, [])


class Words:
    def __init__(self, word):
        self.word = word
        self.hash = self._calc_hash()

    def __str__(self):
        return self.word

    def _calc_hash(self):
        word = self.word
        chars = dict(Counter(word))
        sorted_chars = sorted(chars.items(), key=lambda x: x[0])
        return ''.join([f'{char.lower()}{count}'
                        for char, count in sorted_chars])
