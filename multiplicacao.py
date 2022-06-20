from automata.tm.dtm import DTM

dtm = DTM(
    states={'qi','q0', 'q1', 'q2', 'q3', 'q5', 'q6', 'q7', 'q8','q9','q10','ha'},
    input_symbols={'1', '0'},
    tape_symbols={"0","1","E","Z","#","*"},
    transitions={
        'qi': {
            '#': ('q0', '#', 'R'),
        },
        'q0': {
            '1': ('q1', '#', 'R'),
            "#": ("q0", "#", "R")
        },
        'q1': {
            '*': ('q2', '1', 'R'),
            '1': ('q5', '1', 'R'),
        },
        'q2': {
            'Z': ("q2","1","R"),
            "1": ("q2","1","R"),
            '#': ("q3","#","L")
        },
        'q3': {
            '1': ('ha', '#', 'N')
        },
        'q5': {
            '1': ('q5', '1', 'R'),
            '*': ('q6', '*', 'R')
        },
        'q6': {
            '1': ('q7', 'E', 'R'),
            'Z': ('q9', 'Z', 'L'),
        },
        'q7':{
            '1': ('q7', '1', 'R'),
            'Z': ('q7', 'Z', 'R'),
            '#': ('q8', 'Z', 'L'),
        },
        'q8':{
            '1': ('q8', '1', 'L'),
            'Z': ('q8', 'Z', 'L'),
            'E': ('q6', 'E', 'R'),
        },
        'q9':{
            'E': ('q9', '1', 'L'),
            '*': ('q10', '*', 'L'),
        },
        'q10':{
            '1': ('q0', '1', 'L'),
            '#': ('q0', '#', 'R'),
        },
    },
    initial_state='q0',
    blank_symbol='#',
    final_states={'ha'}
)

steps = dtm.read_input_stepwise("#11*111####")
for step in steps:
    print("############# ",step)
dtm.read_input("#11*111####").print()

if dtm.accepts_input("#11*111####"):
    print('accepted')
else:
    print('rejected')