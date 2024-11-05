# Python-Game-Of-Thrones-fitgh

<p>This project is a Python game featuring a magical duel between two legendary characters, <strong>Gandalf</strong> and <strong>Sauron</strong>. Each character possesses unique attacks and abilities, with the aim to battle until one character’s health is fully depleted.</p>
<h2>Project Overview</h2>
<p>This game simulates a turn-based combat where players can watch a back-and-forth magical duel between Gandalf, the White Wizard, and Sauron, the Dark Sorcerer. The game continues until one character wins by reducing the opponent's health points (HP) to zero.</p>
Features
Characters: Each character has special attacks with distinct damage points.
Turn-based Gameplay: Gandalf and Sauron take turns attacking each other, with a small chance to evade attacks.
Experience Gain: Characters gain experience based on their attack power.
Simple Command Line Interface: The game can be easily played from the command line.
Classes
Personnage
<p>The abstract base class for the characters. This class defines:</p>
Attributes: nom (name), vie (health), experience, degats (damage taken), and attacks.
Methods:
frappe(): Abstract method to be implemented by each character.
recevoir_degats(): Handles incoming damage and updates the character's HP.
esquive(): A chance-based dodge method that may prevent damage.
MagicienBlanc (Gandalf)
<p>A subclass of `Personnage` with specific attacks:</p>
Attacks: "Boule de Feu" (Fireball) and "Sort de Glace" (Ice Spell).
frappe(): Randomly selects an attack and applies its damage to the opponent.
RoiSorcier (Sauron)
<p>A subclass of `Personnage` representing a powerful dark sorcerer with unique attacks:</p>
Attacks: "Maudit" (Curse) and "Explosion Noire" (Black Explosion).
frappe(): Randomly selects an attack and applies its damage to the opponent.
Getting Started
Prerequisites
<p>To play, you’ll need Python 3.x installed on your machine.</p>
How to Run
Clone the repository or download the project files.
Navigate to the project directory in your terminal.
Run the main script using the command:
bash
Copier le code
python main.py
Follow the prompts to continue each turn or quit.
Example Gameplay
plaintext
Copier le code
Tour 1: Gandalf 100 PV, Sauron 100 PV
Gandalf utilise Boule de Feu, infligeant 25 de dégâts.
...
Project Structure
personnage.py: Defines the base Personnage class.
magicien.py: Defines MagicienBlanc, Gandalf’s character class.
roisorcier.py: Defines RoiSorcier, Sauron’s character class.
main.py: Runs the game, managing turns and determining the winner.
Future Enhancements
<p>Here are some potential features to expand the project:</p>
Add more characters and attacks.
Implement player control to choose specific attacks.
Enhance combat mechanics with more attributes (e.g., mana, stamina).
