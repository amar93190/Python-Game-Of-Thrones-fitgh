from .personnage import Personnage
import random

class MagicienBlanc(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.attacks = {"Boule de Feu": 25, "Sort de Glace": 20}

    def frappe(self, cible):
        if not cible.esquive():
            attack = random.choice(list(self.attacks.items()))
            cible.recevoir_degats(attack[1])
            self.experience += attack[1] * 0.1
            print(f"{self.nom} utilise {attack[0]}, infligeant {attack[1]} de dégâts.")