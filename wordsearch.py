### Tool used to create a NxN wordsearch given a list of words to include

import random

alphabet = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z']

class WordGrid():

    def __init__(self, N, val='.'):
        values = []
        for i in range(N):
            col = []
            for j in range(N):
                col.append(val)
            values.append(col)
        self.values = values
        self.N = N

    def __str__(self):
        s = ''
        for i in range(self.N):
            for j in range(self.N):
                s += self.values[i][j] + ' '
            s += '\n'
        return s

    def __getitem__(self, indices):
        try:
            assert len(indices) == 2
            return self.values[indices[0]][indices[1]]
        except AssertionError:
            print('number of indices must equal 2')

    def __setitem__(self, indices, val):
        try:
            assert len(indices) == 2
            self.values[indices[0]][indices[1]] = val
        except AssertionError:
            print('number of indices must equal 2')

    def add_word(self, word, direction):
        letters = []
        for letter in word:
            letters.append(letter)
        print(letters)
        # TODO

    def fill_rest(self, replace='.'):
        for i in range(self.N):
            for j in range(self.N):
                if self.values[i][j] == replace:
                    r = random.randint(0,len(alphabet) - 1)
                    self.values[i][j] = alphabet[r]

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.values[i][j], end=' ')
            print()

wg = WordGrid(8)
wg.fill_rest()
print(wg)
