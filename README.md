#🧙 Battle of Wizards 🧙
<p align="center"> <em>A magical duel of wits and strength between two iconic characters: <strong>Gandalf</strong> and <strong>Sauron</strong>!</em> </p>
🌟 Project Overview
Battle of Wizards is a Python-based game featuring a turn-based duel between Gandalf, the White Wizard, and Sauron, the Dark Sorcerer. Each character has unique abilities, and the game continues until one character’s health reaches zero.

<h2>⚔️ Features</h2>
Dynamic Characters: Each character has their own set of powerful attacks and unique attributes.
Turn-Based Gameplay: Watch Gandalf and Sauron battle it out in an automated, turn-by-turn combat sequence.
Experience Gain: Characters gain experience points from each attack, bringing them closer to victory.
Command Line Interface: Simple and interactive, playable directly from the terminal.
<h2>🏆 Gameplay Classes</h2>
🧝‍♂️ Personnage
<p>The base class that defines core attributes and methods for characters:</p>
Attributes:
nom: Character name
vie: Health points (HP)
experience: Experience points
degats: Accumulated damage
attacks: List of attacks
Methods:
frappe(): Abstract method to handle attacks, implemented in subclasses.
recevoir_degats(): Processes incoming damage and updates health points.
esquive(): Adds a chance to dodge an attack, adding depth to gameplay.
🧙 MagicienBlanc (Gandalf)
<p>A subclass of `Personnage` representing Gandalf, featuring specific magical abilities:</p>
Attacks:
"Boule de Feu" (Fireball)
"Sort de Glace" (Ice Spell)
Special Method: Gandalf’s frappe() method selects and applies an attack randomly to the opponent.
👿 RoiSorcier (Sauron)
<p>A subclass representing Sauron, who uses dark magic to overpower opponents:</p>
Attacks:
"Maudit" (Curse)
"Explosion Noire" (Black Explosion)
Special Method: Sauron’s frappe() method selects an attack to inflict heavy damage on Gandalf.
<h2>🧩 Project Structure</h2>
<pre> 📂 Battle-of-Wizards/ ├── personnage.py # Base class defining the main character structure. ├── magicien.py # Gandalf's class with unique abilities. ├── roisorcier.py # Sauron's class with unique abilities. └── main.py # Main game loop and logic to start the duel. </pre>
<h2>🚀 Getting Started</h2>
Prerequisites
To enjoy Battle of Wizards, ensure that Python 3.x is installed.

Installation and Running the Game
Clone the repository or download the project files.
Open the terminal and navigate to the project folder.
Start the game by running:
bash
Copier le code
python main.py
Sample Gameplay
plaintext
Copier le code
Tour 1: Gandalf 100 PV, Sauron 100 PV
Gandalf utilise Boule de Feu, infligeant 25 de dégâts.
Sauron riposte avec Maudit, infligeant 20 de dégâts.
...
💡 Future Enhancements
Additional Characters: Add more characters with unique spells.
Player Control: Allow the player to choose attacks.
Advanced Mechanics: Introduce mana, stamina, and more dynamic combat attributes.
📊 Stats and Technologies
<p>Developed with Python, using Object-Oriented Programming principles.</p>
