
define e = Character('Eileen', color="#c8ffc8")

init:
    image back = im.Scale('back.png', 100, 120)
    image slot = im.Scale('slot.png', 100, 120)

init python:
    import random
    
    class Card:
        def __init__(self, letter, category='default'):
            self.letter = letter
            self.category = category
            
        def __repr__(self):
            return '<Card>: {}'.format(self.letter)
            
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
        def __init__(self, inventory=[]):
            self.inventory = inventory
            self.slot1 = None
            self.slot2 = None
            self.slot3 = None
            self.slot4 = None
            self.slot5 = None
            self.slots = [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5]
            
        def draw_card(self, cards):
            card = random.choice(cards)
            
            if not self.slot1:
                self.slot1 = card
            elif not self.slot2:
                self.slot2 = card
            elif not self.slot3:
                self.slot3 = card
            elif not self.slot4:
                self.slot4 = card
            elif not self.slot5:
                self.slot5 = card
            
        def __repr__(self):
            return '<Player>: {} {} {} {} {}'.format(self.slot1, self.slot2, self.slot3, self.slot4, self.slot5)
    
    
screen field(word):
    $ enemy_start_x = 0.07
    $ enemy_delta_x = 0.15
    $ enemy_counter = 0
    
    $ player_start_x = 0.07
    $ player_delta_x = 0.15
    $ player_counter = 0
    
    add "back" xpos 0.80 ypos 0.4
    imagebutton idle "back" hover "back" xpos 0.8 ypos 0.4 action Jump('draw_card')
    
    for s in enemy.slots:
        if s:
            text "[s.letter]" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
            add "slot" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
        else:
            add "slot" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
            
        $ enemy_counter += 1
        
    for s in range(0, len(word.letters)):
        add "slot" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.5
    
    for s in [player.slot1, player.slot2, player.slot3, player.slot4, player.slot5]:
        if s:
            
            imagebutton idle "slot" hover "slot" hovered Show('slot_options', pos=player_counter) unhovered Hide('slot_options') action Jump('draw_card') xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
            #add "slot" xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
            text "[s.letter]" xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
        else:
            add "slot" xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
            
        $ player_counter += 1
        
screen slot_options(pos):
    $ slot_pos = 0.07 + (0.15 * pos)
    
    textbutton "Place" xpos slot_pos ypos 0.75
    textbutton "Skip" xpos slot_pos ypos 0.80
    textbutton "Trade" xpos slot_pos ypos 0.85
    
label start:
    $ player = Player()
    $ enemy = Player()

    $ c_A = Card('A')
    $ c_B = Card('B')
    $ c_C = Card('C')
    $ c_D = Card('D')
    $ c_E = Card('E')
    $ c_F = Card('F')
    
    $ ALL_CARDS = [c_A, c_B, c_C, c_D, c_E, c_F]
    
    $ a_this = ArabicWord('This', ['T', 'H', 'I', 'S'])
    
    jump main_loop

label main_loop:
    
    
    call screen field(a_this)
    #show back at left
    #show slot at right

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
    
label draw_card:
    
    "I draw a card"
    $ player.draw_card(ALL_CARDS)
    
    jump main_loop
