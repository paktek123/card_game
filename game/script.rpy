
define e = Character('Eileen', color="#c8ffc8")

init:
    image back = im.Scale('back.png', 100, 120)
    image slot = im.Scale('slot.png', 100, 120)

init python:
    class Card:
        def __init__(self, letter, category='default'):
            self.letter = letter
            self.category = category
            
        def __repr__(self):
            return '<Card>: {}'.format(letter)
            
    class Letter:
        def __init__(self, alphabet):
            self.alphabet = alphabet
            
        def __repr__(self):
            return '<Letter>: {}'.format(alphabet)
            
    class ArabicWord:
        def __init__(self, pic, letters=[]):
            self.pic = pic
            self.letters = letters
            
        def __repr__(self):
            return '<ArabicWord>: {}'.format(letters.join(' '))
            
    class Player:
        def __init__(self, inventory):
            self.inventory = inventory
            self.slot1 = None
            self.slot2 = None
            self.slot3 = None
            self.slot4 = None
            self.slot5 = None
            
        def __repr__(self):
            return '<Player>: {}'.format(alphabet)
    
    
screen field(word):
    $ enemy_start_x = 0.07
    $ enemy_delta_x = 0.15
    
    $ player_start_x = 0.07
    $ player_delta_x = 0.15
    
    add "back" xpos 0.80 ypos 0.4
    
    for s in range(0,5):
        add "slot" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.05
        
    for s in range(0, len(word.letters)):
        add "slot" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.5
    
    for s in range(0,5):
        add "slot" xpos (player_start_x + (player_delta_x*s)) ypos 0.75

label start:

    $ c_A = Card('A')
    $ c_B = Card('B')
    $ c_C = Card('C')
    $ c_D = Card('D')
    $ c_E = Card('E')
    $ c_F = Card('F')
    
    $ a_this = ArabicWord('This', ['T', 'H', 'I', 'S'])
    
    call screen field(a_this)
    #show back at left
    #show slot at right

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
