from classes import *

automaton = Automaton('c')

automaton.addstate('p', 'initial')
automaton.addstate('q', 'normal')
automaton.addstate('r', 'final')

automaton.getstate('p').addtransition('p', 'a', '#', '#a')
automaton.getstate('p').addtransition('p', 'b', '#', '#b')
automaton.getstate('p').addtransition('p', 'a', 'a', 'aa')
automaton.getstate('p').addtransition('p', 'b', 'a', 'ab')
automaton.getstate('p').addtransition('p', 'a', 'b', 'ba')
automaton.getstate('p').addtransition('p', 'b', 'b', 'bb')
automaton.getstate('p').addtransition('q', 'c', 'a', 'a')
automaton.getstate('p').addtransition('q', 'c', 'b', 'b')
automaton.getstate('p').addtransition('q', 'c', '#', '#')
# automaton.getstate('p').showtransitions()

automaton.getstate('q').addtransition('q', 'a', 'a', 'λ')
automaton.getstate('q').addtransition('q', 'b', 'b', 'λ')
automaton.getstate('q').addtransition('r', 'λ', '#', '#')
# automaton.getstate('q').showtransitions()

automaton.start()
