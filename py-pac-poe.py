print("""
  ----------------------
  Let's play Py-Pac-Poe!
  ----------------------
      """)

state = {}

def play_game():
    init_game()
    while not state['winner']:
        print_board()

def init_game():
    state['board'] = {
    'a1': 'X', 'b1': None, 'c1': None,
    'a2': None, 'b2': None, 'c2': None,
    'a3': None, 'b3': None, 'c3': None
    }
    state['winner'] = None
    state['turn'] = 'X'

def print_board():
    b = state['board']
    print(
        """
            A   B   C
        1)  {} | {} | {} 
            ----------
        2)  {} | {} | {}
            ----------
        3)  {} | {} | {}
        """.format(
        str(b['a1'] or ' '), str(b['b1'] or ' '), str(b['c1'] or ' '),
        str(b['a2'] or ' '), str(b['b2'] or ' '), str(b['c2'] or ' '),
        str(b['a3'] or ' '), str(b['b3'] or ' '), str(b['c3'] or ' ')
        )
    )




play_game()