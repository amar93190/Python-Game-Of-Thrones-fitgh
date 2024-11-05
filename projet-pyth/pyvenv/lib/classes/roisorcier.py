from .personnage import Personnage
import random

class RoiSorcier(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.attacks = {"Maudit": 30, "Explosion Noire": 35}

    def frappe(self, cible):
        if not cible.esquive():
            attack = random.choice(list(self.attacks.items()))
            cible.recevoir_degats(attack[1])
            self.experience += attack[1] * 0.1
            print(f"{self.nom} lance {attack[0]}, causant {attack[1]} de dégâts.")