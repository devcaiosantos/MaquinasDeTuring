from automata.tm.dtm import DTM

dtm = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'ha'},
    input_symbols={'1', '0'},
    tape_symbols={"0","1","E","#","-"},
    transitions={
        'q0': {
            '#': ('q1', '#', 'R'),
        },
        'q1': {
            'E': ('q2', '#', 'R'),
        },
        'q2': {
            'E': ("q2","E","R"),
            "-": ("q3","-","R")
        },
        'q3': {
            'E': ('q3', 'E', 'R'),
            "#": ("q4","#","L")
        },
        'q4': {
            'E': ('q5', '#', 'L'),
        },
        'q5': {
            'E': ('q6', 'E', 'L'),
            '-': ('ha', '#', 'N')
        },
        'q6': {
            'E': ('q6', 'E', 'L'),
            '-': ('q7', '-', 'L'),
        },
        'q7':{
            '#': ('ha', '#', 'N'),
            'E': ('q8', 'E', 'L'),
        },
        'q8':{
            'E': ('q8', 'E', 'L'),
            '#': ('q1', '#', 'R'),
        }
    },
    initial_state='q0',
    blank_symbol='#',
    final_states={'ha'}
)

if dtm.accepts_input("#EE-EE#"):
    print('accepted')
else:
    print('rejected')