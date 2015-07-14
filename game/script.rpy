
define e = Character('Eileen', color="#c8ffc8")

init:
    image back = im.Scale('back.png', 100, 120)
    image slot = im.Scale('slot.png', 100, 120)
    image place = im.Scale('up.png', 50, 50)
    image wrong = im.Scale('cross.png', 50, 50)
    $ placed_card = None
    $ secret_card = None

init python:
    import random
    
    class Card:
        def __init__(self, letter, category='default'):
            self.letter = letter
            self.category = category
            self.reveal = False
            
        def __repr__(self):
            return '<Card>: {}'.format(self.letter)
            
    class CurrentSession:
        def __init__(self):
            self.placed_card = None
            self.secret_card = None
            self.word = None
            self.position = None
            self.slot = None
            
        def clear(self):
            self.placed_card = None
            self.secret_card = None
            self.word = None
            self.position = None
            self.slot = None
    
    class Letter:
        def __init__(self, alphabet):
            self.alphabet = alphabet
            
        def __repr__(self):
            return '<Letter>: {}'.format(alphabet)
            
    class Slot:
        def __init__(self, expected_letter, given_letter=None):
            self.expected_letter = expected_letter
            self.given_letter = given_letter
            self.reveal = False
            
        def __repr__(self):
            return '<Slot>: {} {}'.format(self.expected_letter, self.given_letter)
        
            
    class ArabicWord:
        def __init__(self, pic, letters=[]):
            self.pic = pic
            self.letters = letters
            self.slots = [Slot(letter) for letter in self.letters]
            
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
                
        def held_letters(self):
            return [s.letter for s in [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5] if s]
            
        def held_cards(self):
            return [s for s in [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5] if s]
            
        def clear_last_slot(self):
            last_slot = self.held_cards()[-1]
            last_slot = None
            
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
    
    for s in [enemy.slot1, enemy.slot2, enemy.slot3, enemy.slot4, enemy.slot5]:
        if s:
            add "slot" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
            text "[s.letter]" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
        else:
            add "slot" xpos (enemy_start_x + (enemy_delta_x*enemy_counter)) ypos 0.05
            
        $ enemy_counter += 1
        
    for s, slot in enumerate(word.slots):
        add "slot" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.5
        if slot.reveal:
            text "[slot.expected_letter]" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.5
    
    for s in [player.slot1, player.slot2, player.slot3, player.slot4, player.slot5]:
        if s:
            imagebutton idle "slot" hover "slot" action [SetField(current_session, "word", word), 
                                                         SetField(current_session, 'slot', s),
                                                         Show('slot_options', pos=player_counter, card=s)] xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
            text "[s.letter]" xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
        else:
            add "slot" xpos (player_start_x + (player_delta_x*player_counter)) ypos 0.75
            
        $ player_counter += 1
        
screen place(word):
    $ enemy_start_x = 0.07
    $ enemy_delta_x = 0.15
    
    for s, slot in enumerate(word.slots):
        imagebutton idle "place" hover "place" xpos (enemy_start_x + (enemy_delta_x*s)) ypos 0.5 action [SetField(current_session, "secret_card", slot), 
                                                                                                         SetField(current_session, "position", ((enemy_start_x + (enemy_delta_x*s)), 0.5)),
                                                                                                         Jump("place")]
        
screen wrong():
    add "wrong" pos current_session.position
        
screen slot_options(pos, card):
    $ slot_pos = 0.04 + (0.15 * pos)
    
    textbutton "Place" xpos slot_pos ypos 0.75 action [SetField(current_session, "placed_card", card), Hide('slot_options'), ShowTransient('place', word=current_session.word) ]#Jump('place_card')]
    textbutton "Skip" xpos slot_pos ypos 0.80 action Jump('skip_turn')
    textbutton "Trade" xpos slot_pos ypos 0.85
    
label start:
    $ player = Player()
    $ enemy = Player()
    
    $ current_session = CurrentSession()

    $ c_A = Card('A')
    $ c_B = Card('B')
    $ c_C = Card('C')
    $ c_D = Card('D')
    $ c_E = Card('E')
    $ c_F = Card('F')
    
    $ ALL_CARDS = [c_A, c_B, c_C, c_D, c_E, c_F]
    
    $ a_this = ArabicWord('This', ['A', 'E', 'C', 'F'])
    
    jump main_loop

label main_loop:
    
    call screen field(a_this)
    #show back at left
    #show slot at right

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
    
label draw_card:
    
    #"I draw a card"
    hide wrong
    $ player.draw_card(ALL_CARDS)
    
    jump main_loop
    
label place_card:
    hide wrong
    call screen place
    
label place:
    if current_session.secret_card.expected_letter == current_session.placed_card.letter:
        $ current_session.secret_card.reveal = True
        $ current_session.slot = None
    else:
        $ position = Position(pos=current_session.position)
        show wrong at position
        
        
    $ current_session.clear()
    jump enemy_move
    
label skip_turn:
    jump enemy_move
    
label enemy_move:
    $ enemy.draw_card(ALL_CARDS)
    
    #for letter in current_session.word.letters:
    $ enemy_held_letters = enemy.held_letters()
    
    python:
        for letter in enemy_held_letters:
            if letter in current_session.word.letters:
                word_slot = [s for s in current_session.word.slots if s.expected_letter == letter][0]
                word_slot.reveal = True
                enemy.clear_last_slot()
            
    jump main_loop
            
    
