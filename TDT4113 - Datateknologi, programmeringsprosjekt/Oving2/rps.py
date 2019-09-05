import random



class Spiller:
    """Docstring"""

    def __init__(self):
        self.score = 0
        self.act = None
        self.navn = None

    def velg_aksjon(self):
        """Velger mellom rock/paper/scissor og returnerer dette"""
        self.act = input("r/p/s: ")
        return self.act

    def motta_resultat(self):
        """Får vite hva resultatet ble"""
        pass

    def oppgi_navn(self, navn):
        """Oppgir navnet til klassen"""
        self.navn = navn

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
