from abc import ABC, abstractmethod
import random

class Personnage(ABC):
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.experience = 0
        self.degats = 0
        self.attacks = {}

    @abstractmethod
    def frappe(self, cible):
        pass

    def recevoir_degats(self, degats):
        self.degats += degats
        print(f"{self.nom} reçoit {degats} de dégâts, total: {self.degats}. Santé restante: {self.vie - self.degats}")

    def esquive(self):
        if random.random() < 0.2:
            print(f"{self.nom} esquive l'attaque!")
            return True
        return False
