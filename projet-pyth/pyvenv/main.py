from lib.classes.magicien import MagicienBlanc
from lib.classes.roisorcier import RoiSorcier

def main():
    gandalf = MagicienBlanc("Gandalf")
    sauron = RoiSorcier("Sauron")
    tour = 0

    while gandalf.vie - gandalf.degats > 0 and sauron.vie - sauron.degats > 0:
        print(f"\nTour {tour + 1}: Gandalf {gandalf.vie - gandalf.degats} PV, Sauron {sauron.vie - sauron.degats} PV")
        if tour % 2 == 0:
            gandalf.frappe(sauron)
        else:
            sauron.frappe(gandalf)

        if input("Tapez 'quit' pour quitter ou appuyez sur Entrée pour continuer: ").lower() == 'quit':
            print("Jeu terminé.")
            break
        tour += 1

    print("Le jeu est fini.")
    if gandalf.vie - gandalf.degats > 0:
        print("Gandalf gagne!")
    else:
        print("Sauron gagne!")

if __name__ == "__main__":
    main()