pfannkuchen = "\n 200 g Mehl\n 2 Eier\n 300 ml Milch\n 1 Prise Salz\n 1 EL Zucker\n Butter/Öl zum Braten"

waffeln = "\n 250 g Mehl\n 2 Eier\n 150 g Zucker\n 1 Päckchen Vanillezucker\n 125 g Butter\n 250 ml Milch\n 1 Prise Salz\n 1 TL Backpulver"

kaesekuchen = "\n 500 g Quark (Magerquark)\n 150 g Zucker\n 1 Päckchen Vanillezucker\n 3 Eier\n 1 Päckchen Vanillepuddingpulver\n 100 g Butter (geschmolzen)\n 1 Prise Salz\n Abrieb einer Zitrone (optional)"




print("Bitte wähle dein Rezept (1, 2 oder 3)")
print("")
for rezept in ["(1) Pfannkuchen", "(2) Waffeln", "(3) Käsekuchen"]:
    print(rezept)



auswahl = int(input("Auswahl: "))
if auswahl == 1:
    print("Dein Pfannkuchen Rezept lautet: " + pfannkuchen)
    print("Viel Spass beim nachmachen! :) ")
elif auswahl == 2:
    print("Dein Waffel Rezept lautet: " + waffeln)
    print("Viel Spass beim nachmachen! :) ")
elif auswahl == 3:
     print("Dein Käsekuchen Rezept lautet: " + kaesekuchen)
     print("Viel Spass beim nachmachen! :) ")
else:
    print("Ich habe deine Eingabe nicht verstanden")



input("Press a key to end the program...")