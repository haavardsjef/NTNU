import random



class Spiller:
    """Docstring"""

    def __init__(self):
        self.score = 0
        self.act = None
        self.navn = None
        self.MestVanlig = None

    def velg_aksjon(self):
        """Velger mellom rock/paper/scissor og returnerer dette"""
        return self.act

    def motta_resultat(self):
        """Får vite hva resultatet ble"""
        pass

    def oppgi_navn(self, navn):
        """Oppgir navnet til klassen"""
        self.navn = navn

class Historiker(Spiller):
    """Docstring"""
    pass

class Sekvensiell(Spiller):
    """Går sekvensielt gjennom de forskjellig aksjonene, rock, saks, papir"""

    def __init__(self):
        Spiller.__init__(self)
        self.previous = None


    def velg_aksjon(self):
        if self.previous is None or self.previous == 'p':
            self.previous = 'r'
            return 'r'
        elif self.previous == 'r':
            self.previous = 's'
            return 's'
        self.previous = 'p'
        return 'p'


class Tilfeldig(Spiller):
    """En spiller som velger tilfeldig mellom stein, saks og papir"""

    def __init__(self):
        Spiller.__init__(self)


    @staticmethod
    def velg_aksjon():
        temp = random.randint(0, 2)
        if temp == 0:
            return 'r'
        elif temp == 1:
            return 'p'
        return 's'

class MestVanlig(Spiller):
    """Velger basert på hvilket av motstanderens valg som er mest vanlig"""

    def __init__(self):
        Spiller.__init__(self)
        self.MestVanlig = [0, 0, 0]

class EnkeltSpill:
    """Et enkelt spill"""
    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2

    def gjennomfoer_spill(self):
        """Gjennomfører et enkelt spill"""
        act1 = Aksjon(self.spiller1.act)
        act2 = Aksjon(self.spiller2.act)
        if act1 == act2:
            self.spiller1.score += 0.5
            self.spiller2.score += 0.5
            return act1, act2, 0
        elif act1 > act2:
            self.spiller1.score += 1
            return act1, act2, 1
        self.spiller2.score += 1
        return act1, act2, 2

    def __str__(self):
        return "Spiller 1 valgte: " + self.spiller1.act + ". Spiller 2 valgte: " \
        + self.spiller2.act + ". Vinneren var "

class Aksjon:
    """Comperator for actions"""
    def __init__(self, act):
        self.act = act

    def __eq__(self, other):
        return self.act == other.act

    def __gt__(self, other):
        if (self.act == "r" and other.act == "s") or \
        (self.act == "p" and other.act == "r") or (self.act == "s" and other.act == "p"):
            return True
        return False
