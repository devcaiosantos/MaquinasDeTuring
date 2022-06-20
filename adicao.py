from automata.tm.dtm import DTM

dtm = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'ha'},
    input_symbols={'1', '0'},
    tape_symbols={"0","1","E","#","+"},
    transitions={
        'q0': {
            '#': ('q1', '#', 'R'),
        },
        'q1': {
            'E': ('q1', 'E', 'R'),
            "+": ("q2", "E", "R")
        },
        'q2': {
            'E': ("q2","E","R"),
            "#": ("q3","#","L")
        },
        'q3': {
            'E': ('ha', '#', 'N'),
        }
    },
    initial_state='q0',
    blank_symbol='#',
    final_states={'ha'}
)

if dtm.accepts_input("#EEEEE-EE#"):
    print('accepted')
else:
    print('rejected')