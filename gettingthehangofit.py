Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def Main():
	print("Select a number between 1-100")
	randomnumber = ("42")
	userGuess = input("Your Guess: ")
	if userGuess == randomnumer:
		print("You got it homeslice!")
	else:
		print("That is incorrect padawan")

		
>>> Main()
Select a number between 1-100
Your Guess: 12
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Main()
  File "<pyshell#9>", line 5, in Main
    if userGuess == randomnumer:
NameError: name 'randomnumer' is not defined
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
                print("+1 to any attribute")
        elif userRace == Elf:
                print("+2 dex, immune to sleep magic, resistant to charm")
        elif userRace == Dwarf:
                print("+2 con, immune to poison, advantage on stone knowledge")
        else:
                print("Remember to spell correctly")
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
                print("+1 to any attribute")
                
        elif userRace == Elf:
                print("+2 dex, immune to sleep magic, resistant to charm")
                
        elif userRace == Dwarf:
                print("+2 con, immune to poison, advantage on stone knowledge")
                
        else:
                print("Remember to spell correctly")
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
                print("+1 to any attribute")
                
        elif userRace == Elf:
                print("+2 dex, immune to sleep magic, resistant to charm")
        elif userRace == Dwarf:
                print("+2 con, immune to poison, advantage on stone knowledge")
        else:
                print("Remember to spell correctly")
                
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
		if userRace == Human:
			print("+1 to any attribute")
		elif userRace == Elf:
			print("+2 dex, immune to sleep magic, resistant to charm")
		elif userRace == Dwarf:
			print("+2 con, immune to poison, advantage on stone knowledge")
		else:
			print("Remember to spell correctly")
			
SyntaxError: unexpected indent
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
			print("+1 to any attribute")
		elif userRace == Elf:
			print("+2 dex, immune to sleep magic, resistant to charm")
		elif userRace == Dwarf:
			print("+2 con, immune to poison, advantage on stone knowledge")
	else:
			print("Remember to spell correctly")
			
SyntaxError: unindent does not match any outer indentation level
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
		print("+1 to any attribute")
		elif userRace == Elf:
			print("+2 dex, immune to sleep magic, resistant to charm")
		elif userRace == Dwarf:
			print("+2 con, immune to poison, advantage on stone knowledge")
	else:
		print("Remember to spell correctly")
		
SyntaxError: invalid syntax
>>> def Main():
	print("Choose a race from Elf, Dwarf, Human")
	Human = ("Human")
	Elf = ("Elf")
	Dwarf = ("Dwarf")
	userRace = input("Your Race: ")
	if userRace == Human:
		print("+1 to any attribute")
	elif userRace == Elf:
		print("+2 dex, immune to sleep magic, resistant to charm")
	elif userRace == Dwarf:
		print("+2 con, immune to poison, advantage on stone knowledge")
	else:
		print("Remember to spell correctly")

		
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: Human
+1 to any attribute
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: Elf
+2 dex, immune to sleep magic, resistant to charm
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: Dwarf
+2 con, immune to poison, advantage on stone knowledge
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: elf
Remember to spell correctly
>>> def NextStep():
	print("Select a class from Fighter, Cleric, Thief")
	Fighter = ("Fighter")
	Cleric = ("Cleric")
	Thief = ("Thief")
	userClass = input("Your Class: ")
	if userClass == Fighter:
		print("Proficient in hand-to-hand combat", "Built to be powerhouses",
		      "Knowledgeable in use of almost all weapon types",
		      "Is capaable of using most types of armor efficiently",)
	elif userClass == Cleric:
		print("Calls upon invokation of Gods to cast magic",
		      "Wields maces and hammers efficiently",
		      "Is capable of using mosts types of armor efficiently",)
	elif userClass == Thief:
		print("Relys on stealth and agility to dispatch enemies",
		      "can use thieves tools, daggers, bows, short swords efficiently",
		      "Is capable of using leather while still being able to sneak efficiently")

	
>>> NextStep()
Select a class from Fighter, Cleric, Thief
Your Class: Fighter
Proficient in hand-to-hand combat Built to be powerhouses Knowledgeable in use of almost all weapon types Is capaable of using most types of armor efficiently
>>> NextStep()
Select a class from Fighter, Cleric, Thief
Your Class: Cleric
Calls upon invokation of Gods to cast magic Wields maces and hammers efficiently Is capable of using mosts types of armor efficiently
>>> NextStep()
Select a class from Fighter, Cleric, Thief
Your Class: Thief
Relys on stealth and agility to dispatch enemies can use thieves tools, daggers, bows, short swords efficiently Is capable of using leather while still being able to sneak efficiently
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: Elf
+2 dex, immune to sleep magic, resistant to charm
>>> NextStep()
Select a class from Fighter, Cleric, Thief
Your Class: Thief
Relys on stealth and agility to dispatch enemies can use thieves tools, daggers, bows, short swords efficiently Is capable of using leather while still being able to sneak efficiently
>>> Main()
Choose a race from Elf, Dwarf, Human
Your Race: Elf
+2 dex, immune to sleep magic, resistant to charm
>>> NextStep()
Select a class from Fighter, Cleric, Thief
Your Class: Thief
Relys on stealth and agility to dispatch enemies can use thieves tools, daggers, bows, short swords efficiently Is capable of using leather while still being able to sneak efficiently
>>> 
