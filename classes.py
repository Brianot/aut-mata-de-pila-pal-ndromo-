from time import sleep


class Pile():
    def __init__(self):
        self.__top = ''
        self.__list = []

    def insert(self, char):
        if (len(char) > 1):
            for i in char:
                self.__list.append(i)

            self.__top = self.__list[-1]
        elif(char != 'λ'):
            self.__list.append(char)
            self.__top = char

    def remove(self):
        self.__list.pop()

        if(len(self.__list) > 1):
            self.__top = self.__list[-1]
        elif(len(self.__list)==1):
            self.__top =self.__list[0]
        else:
            self.__top=''

    def gettop(self):
        return self.__top

    def getelements(self):
        return self.__list

##########################################################################################################


class Transition():
    def __init__(self, final, char, out, into):
        self.__final = final
        self.__char = char
        self.__out = out
        self.__into = into

    def __str__(self):
        return ("{},{}/{}".format(self.__char, self.__out, self.__into))

    def getfinal(self):
        return self.__final

    def getchar(self):
        return self.__char

    def getout(self):
        return self.__out

    def getinto(self):
        return self.__into

##########################################################################################################


class State():
    def __init__(self, name, kind):
        self.__name = name
        self.__kind = kind
        self.__transitions = []

    def addtransition(self, final, char, out, into):
        self.__transitions.append(Transition(final, char, out, into))

    def showtransitions(self):
        for transition in self.__transitions:
            print(transition)

    def __str__(self):
        return ("Name: {} Kind: {} ".format(self.__name, self.__kind))

    def getname(self):
        return self.__name

    def getkind(self):
        return self.__kind

    def gettransitions(self):
        return self.__transitions
##########################################################################################################


class Automaton():
    def __init__(self, word):
        self.__word = word
        self.__states = []
        self.__actualstate = ''
        self.pile = Pile()
        self.__usedtransitions = []
        self.__result=False

    def addstate(self, name, kind):
        self.__states.append(State(name, kind))

    def getstate(self, name):
        for state in self.__states:
            if (state.getname() == name):
                return state

    def showstates(self):
        for state in self.__states:
            print(state)

    def getstateinitial(self):
        for state in self.__states:
            if (state.getkind() == 'initial'):
                return state

    def start(self):
        self.__actualstate = self.getstateinitial()
        self.__word = self.__word+'λ'
        self.pile.insert('#')

        for char in self.__word:
            #print('Caracter actual', char)
            actualtransition = self.gettransition(char)
            if (actualtransition is not None):
                self.__usedtransitions.append(actualtransition)
               # print('Transición actual', actualtransition)
               # final = self.getstate(actualtransition.getfinal())
                #print("Voy de {} a {} ".format(
                   # self.__actualstate.getname(), final.getname()))
                self.__actualstate = self.getstate(actualtransition.getfinal())
                self.pile.remove()
                self.pile.insert(actualtransition.getinto())
                #print(self.pile.getelements())
               #sleep(5)
            else:
                break

        if (self.__actualstate.getkind() == 'final'):
            self.__result=True
            print('Es palíndromo')
        else:
            print('No es palíndromo')

    def gettransition(self, char):
        for transition in self.__actualstate.gettransitions():
            if (transition.getchar() == char and self.pile.gettop() == transition.getout()):
                return transition

    def getusedtransitions(self):
        return self.__usedtransitions

    def getresult(self):
        return self.__result