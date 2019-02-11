'''Package to create a wordsearch in txt, tex, pdf or png form'''

import random
from enum import Enum

alphabet = ('a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z')

class Directions(Enum):
    '''Enumeration to encode all of the possible directions'''
    NORTH_EAST = (1,1)
    EAST = (1,0)
    SOUTH_EAST = (1,-1)
    SOUTH = (0,-1)
    SOUTH_WEST = (-1,-1)
    WEST = (-1,0)
    NORTH_WEST = (-1,1)
    NORTH = (0,1)

class WordGrid():
    '''WorldGrid class to store all wordsearch data'''

    def __init__(self, N, val='.'):
        '''WorldGrid constructor'''
        values = []
        for i in range(N):
            col = []
            for j in range(N):
                col.append(val)
            values.append(col)
        self.values = values
        self.N = N

    def __str__(self):
        '''Convert WordGrid to string'''
        s = ''
        for i in range(self.N):
            for j in range(self.N):
                s += self.values[i][j] + ' '
            s += '\n'
        return s

    def __getitem__(self, indices):
        '''Get wordsearch letter at given indices'''
        try:
            assert len(indices) == 2
            return self.values[indices[1]][indices[0]]
        except AssertionError:
            print('number of indices must equal 2')

    def __setitem__(self, indices, val):
        '''Set wordsearch letter at given indices with given value'''
        try:
            assert len(indices) == 2
            self.values[indices[1]][indices[0]] = val
        except AssertionError:
            print('number of indices must equal 2')

    def add_word(self, word, empty='.', allow_backwards=True):
        '''Add given word to wordsearch with a random placement'''

        # split word into list of letters
        letters = []
        for letter in word:
            letters.append(letter)

        # keep trying a placement until a word fits
        fits = False
        tries = 0
        while fits==False:
            direction = random.choice(self._allowed_directions(allow_backwards))
            x = random.randint(0, self.N-1)
            y = random.randint(0, self.N-1)
            fits = self._isvalid(direction, x, y, empty, len(letters))
            tries += 1
            if tries > 100000:
                raise ValueError('It seems the wordsearch is too small to hold all these words!')

        # add in word along direction
        for i in range(len(letters)):
            self.__setitem__((x,y), letters[i])
            x += direction.value[0]
            y -= direction.value[1]

    def fill_rest(self, replace='.'):
        '''Fill blank spaces (indicated with replace character) with random letters'''
        for i in range(self.N):
            for j in range(self.N):
                if self.values[i][j] == replace:
                    r = random.randint(0,len(alphabet) - 1)
                    self.values[i][j] = alphabet[r]

    def show(self):
        '''Print WordGrid object to screen'''
        for i in range(self.N):
            for j in range(self.N):
                print(self.values[i][j], end=' ')
            print()

    def _isvalid(self, direction, x, y, empty, length):
        '''Return bool to indicate if given word fits into the wordsearch'''

        # make sure word does not go over the edge
        end_x = x + direction.value[0]*length
        end_y = y - direction.value[1]*length
        if(end_x < 0 or end_x >=self.N or end_y < 0 or end_y >= self.N):
            return False

        # make sure word does not overwite another
        for i in range(length):
            if self.__getitem__((x,y)) != empty:
                return False
            x += direction.value[0]
            y -= direction.value[1]

        # this placement is is valid
        return True

    def _allowed_directions(self, allow_backwards):
        '''Return a list of allowed directions for placement'''
        if allow_backwards == True:
            return list(Directions.__members__.values())[:]
        if allow_backwards == False:
            return list(Directions.__members__.values())[0:4]

def make_wordsearch(N, words, allow_backwards):
    '''Make a wordsearch from specification file (specification.py)'''
    wg = WordGrid(N)
    for word in words:
        wg.add_word(word, allow_backwards=allow_backwards)
    wg.fill_rest()
    return wg

if(__name__ == '__main__'):

    # will be in specification file
    N = 16
    words = ['HERE', 'ARE', 'SOME', 'EXAMPLE', 'WORDS']
    allow_backwards = False
    # TODO

    # make wordsearch
    ws = make_wordsearch(N, words, allow_backwards)

    # save wordsearch to desired format
    print(ws)
    # TODO
