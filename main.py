def citire_fisier(nume_fisier):
    global start_state
    dfa = {}
    with open(nume_fisier, 'r') as f:
        transitions = {}
        accept_states = set()
        linii = f.readlines()
        for linie in linii:
            parti = linie.strip().split()
            if linie != linii[-1]:
                if len(linie) == 6:
                    stare, stare_urmatoare = parti
                    transitions[(stare, "")] = stare_urmatoare
                else:
                    stare, simbol, stare_urmatoare = parti
                    transitions[(stare, simbol)] = stare_urmatoare
            elif linie == linii[-1]:
                for parte in parti:
                    accept_states.add(parte)
            else:
                print(f"Linii ignorate: {linie.strip()}")

        alfabet = set()
        states = set()
        for (stare, simbol) in transitions:
            alfabet.add(simbol)
            states.add(stare)
            states.add(transitions[(stare, simbol)])
        start_state = "q" + min([x[1] for x in states])
        dfa['alphabet'] = alfabet
        dfa['states'] = states

        dfa['start_state'] = start_state
        dfa['accept_states'] = accept_states
        dfa['transitions'] = transitions
    return dfa


global x
x = 0


def generate_words_dfa(dfa, length):
    def backtrack(state, word, cur_length):
        global x
        if cur_length > length:
            return
        if cur_length <= length and state in dfa['accept_states']:
            print(word)
            x += 1
        for edge_label, next_state in dfa['transitions'].items():
            if state == edge_label[0]:
                new_word = word + edge_label[1]
                backtrack(next_state, new_word, cur_length + 1)
            elif state == edge_label[0] and edge_label[1] == '':
                backtrack(next_state, word, cur_length)

    start = dfa['start_state']
    backtrack(start, '', 0)


if __name__ == "__main__":
    dfa = citire_fisier('Test2.txt')
    print(dfa)
    generate_words_dfa(dfa, 3)
    print(x)
