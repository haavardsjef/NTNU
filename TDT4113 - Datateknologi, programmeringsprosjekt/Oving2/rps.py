import random
import matplotlib.pyplot as plt

# 0 = Rock, 1 = Paper, 2 = scissor
class Spiller:
    """Spiller klasse, en generell spiller"""

    def __init__(self):
        self.score = 0
        self.action = None
        self.navn = None
        self.motstanders_valg = []

    def velg_aksjon(self):
        """Velger mellom rock/paper/scissor og returnerer dette"""
        return random.randint(0, 2)

    def motta_resultat(self, opp_action, winner):
        """Får vite hva resultatet ble"""
        self.motstanders_valg.append(opp_action)

    def oppgi_navn(self, navn):
        """Oppgir navnet til klassen"""
        self.navn = navn








class Tilfeldig(Spiller):
    """En spiller som velger tilfeldig mellom stein, saks og papir"""
    def __init__(self):
        Spiller.__init__(self)

    def velg_aksjon(self):
        return random.randint(0, 2)






class Sekvensiell(Spiller):
    """Går sekvensielt gjennom de forskjellig aksjonene, rock, saks, papir"""

    def __init__(self):
        Spiller.__init__(self)
        self.action = 2

    def velg_aksjon(self):
        """Sjekker hva forrige aksjon var, og velger basert på det"""
        if self.action == 2:
            self.action = 0
            return 0
        if self.action == 0:
            self.action = 1
            return 1
        self.action = 2
        return 2






class MestVanlig(Spiller):
    """Velger basert på hvilket av motstanderens valg som er mest vanlig"""

    def __init__(self):
        Spiller.__init__(self)

    def velg_aksjon(self):
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for element in self.motstanders_valg:
            if element == 0:
                count_0 += 1
            elif element == 1:
                count_1 += 1
            else:
                count_2 += 1

        if (count_0 >= count_1) and (count_0 >= count_2):
            return 1
        if (count_1 >= count_0) and (count_1 >= count_2):
            return 2
        return 0






class Historiker(Spiller):
    """Sjekker om motstanderen har en tendens til å spille noe spesielt,
    etter en sekvens av spesifisert lengde"""
    def __init__(self, husk):
        Spiller.__init__(self)
        self.husk = husk
        self.sequence = []

    def find_sequence(self):
        """Finds the last sequence"""
        self.sequence = []
        if self.husk <= len(self.motstanders_valg):
            for i in range(self.husk, 0, -1):
                self.sequence.append(self.motstanders_valg[-1*i])
        else:
            for i in range(len(self.motstanders_valg), 0, -1):
                self.sequence.append(self.motstanders_valg[-1*i])

    def velg_aksjon(self):
        self.find_sequence()
        temp = []
        # Starter fra 1 fordi hvis sekvensen starter på index 0 så er det ingen valg før uansett..
        for i in range(1, len(self.motstanders_valg)):
            if self.motstanders_valg[i:i+self.husk] == self.sequence:
                temp.append(self.motstanders_valg[i-1])

        if not temp: #Sjekker om listen er tom
            return random.randint(0, 2)

        # Koden under er bare kopiert fra MestVanlig klassen,
        # med unntak av at listen er byttet ut med temp listen.
        # Dette kan ganske enkelt gjøres om til en statisk funksjon
        # som tar en liste som input, meen ork...
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for element in temp:
            if element == 0:
                count_0 += 1
            elif element == 1:
                count_1 += 1
            else:
                count_2 += 1

        if (count_0 >= count_1) and (count_0 >= count_2):
            return 1
        if (count_1 >= count_0) and (count_1 >= count_2):
            return 2
        return 0







class EnkeltSpill:
    """Et enkelt spill"""
    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.act1 = None
        self.act2 = None
        self.winner = None

    def gjennomfoer_spill(self):
        """Gjennomfører et enkelt spill"""
        self.act1 = Aksjon(self.spiller1.velg_aksjon())
        self.act2 = Aksjon(self.spiller2.velg_aksjon())
        if self.act1 == self.act2:
            self.spiller1.score += 0.5
            self.spiller2.score += 0.5
            self.winner = None
        elif self.act1 > self.act2:
            self.spiller1.score += 1
            self.winner = 1
        else:
            self.spiller2.score += 1
            self.winner = 2
        self.spiller1.motta_resultat(self.act2.action, self.winner)
        self.spiller2.motta_resultat(self.act1.action, self.winner)

    def __str__(self):
        return "Spiller 1 valgte: " + to_action(self.act1.action) + ". Spiller 2 valgte: " \
        + to_action(self.act2.action) + ". Vinneren var spiller " + str(self.winner)





class Aksjon:
    """Comperator for actions"""
    def __init__(self, action):
        self.action = action

    def __eq__(self, other):
        return self.action == other.action

    def __gt__(self, other):
        if (self.action == 0 and other.action == 2) or \
        (self.action == 1 and other.action == 0) or (self.action == 2 and other.action == 1):
            return True
        return False







class MangeSpill:
    """Når man vil ha mange spill"""
    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill

    def arranger_enkeltspill(self):
        """Arrangerer enkeltspill"""
        spill = EnkeltSpill(self.spiller1, self.spiller2)
        spill.gjennomfoer_spill()
        print(spill)

    def arranger_turnering(self):
        """Arrangerer en turnering"""
        p1_score = []
        for i in range(1, self.antall_spill+1):
            self.arranger_enkeltspill()
            p1_score.append(self.spiller1.score / i)
        print(self.spiller1.score)
        print(self.spiller2.score)
        plt.plot(p1_score)
        plt.ylabel('Gjennomsnittlig poeng')
        axes = plt.gca()
        axes.set_ylim([0, 1])
        plt.show()


def to_action(num):
    """Konverterer tallet til tilsvarende streng"""
    if num == 0:
        return "stein"
    if num == 1:
        return "papir"
    return "saks"




def grensesnitt():
    """Tekst basert grensenitt med 2 spillere"""
    name = input("Navn på spiller: ")
    print("Type spiller?" + "\n" + "0 = Tilfeldig" + "\n" + \
     "1 = Sekvensiell" + "\n" + "2 = MestVanlig" + "\n" + "3 = Historiker")
    type_spiller = int(input())
    if type_spiller == 0:
        PLAYER1 = Tilfeldig()
    elif type_spiller == 1:
        PLAYER1 = Sekvensiell()
    elif type_spiller == 2:
        PLAYER1 = MestVanlig()
    elif type_spiller == 3:
        husk = int(input("Hvor lange sekvenser skal jeg huske: "))
        PLAYER1 = Historiker(husk)
    PLAYER1.oppgi_navn(name)

    print("----------")

    name = input("Navn på spiller: ")
    print("Type spiller?" + "\n" + "0 = Tilfeldig" + "\n" + \
     "1 = Sekvensiell" + "\n" + "2 = MestVanlig" + "\n" + "3 = Historiker")
    type_spiller = int(input())
    if type_spiller == 0:
        PLAYER2 = Tilfeldig()
    elif type_spiller == 1:
        PLAYER2 = Sekvensiell()
    elif type_spiller == 2:
        PLAYER2 = MestVanlig()
    elif type_spiller == 3:
        husk = int(input("Hvor lange sekvenser skal jeg huske: "))
        PLAYER2 = Historiker(husk)
    PLAYER2.oppgi_navn(name)

    print("----------")

    games = int(input("Hvor mange spill skal vi spille: "))

    print("----------")

    TURNERING = MangeSpill(PLAYER1, PLAYER2, games)
    TURNERING.arranger_turnering()

grensesnitt()
