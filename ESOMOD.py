import os
####################################################
#basestats
health = 1200
stamina = 1150
magic = 1150

magicDam = 1100
spellCrit = (magicDam % 25) + magicDam

magicRegen = 175
stamRegen = 175
healthRegen = 125

weaponDam = 1100
weaponCrit = (weaponDam * .15) + weaponDam

#resistance
fireResisx = .01
fireResis = magicDam - (magicDam * fireResisx)
coldResisx = .01
coldResis = magicDam - (magicDam * coldResisx)

#Basic Attribute
characterSpeed = 100 #100 is normal
sneakSpeed = (characterSpeed - 75)
swimSpeed = (characterSpeed - 65)


#list of races in faction
EP = ['Dunmer', 'Nord', 'Argonian']
AD = ['Altmer', 'Bosmer', 'Khajiit']
DC = ['Redguard', 'Orc', 'Breton']
Imp = ['Imperial']
#Classes
Templar = 'temp'
Dragonknight = 'dk'
Nightblade = 'nb'
Sorcercer = 'sorc'
classes = ""
while classes == "":
    classes = raw_input("Please chose your class: Templar, Dragonknight, Nightblade, Sorcerer\n")
    classes = classes.title()
    

    if classes == 'Templar' or classes == 'temp':
        print "\t\t\tRecommended races:", "\n\t\t\tBreton", "\n\t\t\tNord", "\n\t\t\tBosmer","\n\t\t\tImperial", "\n\t\t\tRedguard", "\n\t\t\tAltmer"
    elif classes == 'Dragonknight' or classes == 'Dk':
        print "\t\t\tRecommended race:","\n\t\t\tImperial","\n\t\t\tDunmer","\n\t\t\tNord","\n\t\t\tOrc","\n\t\t\tRedguard"
    elif classes == 'Nightblade' or classes == 'Nb':
        print "\t\t\tRecommended race:", '\n\t\t\tKhajiit', '\n\t\t\tImperial', '\n\t\t\tBosmer', '\n\t\t\tOrc, \n\t\t\tBreton'
    elif classes == "Sorcerer" or classes == 'Sorc':
        print "\t\t\tRecommended race:", '\n\t\t\tImperial', '\n\t\t\tAltmer', '\n\t\t\tBreton', '\n\t\t\tDunmer'
    else:
        classes = ""
        print "Invalid class, please select again."
faction = ""
while faction == "":
    faction = raw_input("Please chose your faction: EP, AD, DC or Imp \n" )
    
    

    if faction == "EP":
        for race in EP:
            print race
        print "Choose your race" "(Note this will tell you your unattributed bonus at end-game)"
        raceChosen = raw_input("")
        if raceChosen == "Dunmer" or raceChosen == "dunmer":
            print "\tMax Magicka:", int(magic + (magic * .06)), "\n\tMax Stamina:", int(stamina + (stamina * .06)), "\n\tFlame Damage Bonus:", int(magicDam + (magicDam * .07))
        if raceChosen == 'Nord' or raceChosen == "nord":
            print "\tMax Health:", int(health + (health * .03)), "\n\tCold Resistance:", int(coldResis +(coldResisx * 3)), "\n\tHealth Regeneration:", int(healthRegen + (healthRegen * .30)), "\n\tDamage Reduction 6%" 
        if raceChosen == "Argonian" or raceChosen == "argonian":
            print "\tSwim Speed Bonus:", int(swimSpeed + (swimSpeed * .50)), "\n\tMax Health:", int(health + (health * .03))
    elif faction == "AD":
        for race in AD:
            print race
        print "Choose your race" "(Note this will tell you your unattributed bonus at end-game)"
        raceChosen = raw_input("")
        if raceChosen == 'Altmer' or raceChosen == 'altmer':
            print "\tMagicka Recovery:", int(magicRegen + (magicRegen * .09)), "\n\tMax Magicka:", int(magic + (magic * .1)), "\n\tMagic Damage:", int(magicDam + (magicDam * .04))
        if raceChosen == "Bosmer" or raceChosen == 'bosmer':
            print "\tStamina Regeneration:", int(stamRegen + (stamRegen * .21)), "\n\tMax Stamina:", int(stamina + (stamina*.03))
        if raceChosen == "Khajiit" or raceChosen == "khajiit":
            print "\tHealth Regeneration:", int(healthRegen + (healthRegen * .3)), "\n\tWeapon Critical % increase:", int(weaponCrit - (weaponCrit * .6))
    elif faction == "DC":
        for race in DC:
            print race
        print "Choose your race" "(Note this will tell you your unattributed bonus at end-game)"
        raceChosen = raw_input("")
        if raceChosen == "Redguard" or raceChosen == 'redguard':
             print "\tStamina Regeneration:", int(stamRegen + (stamRegen * .09)), "\n\tMax Stamina:", int(stamina + (stamina * .1)), "\n\tYou also restore 3[x] Stamina when damaging an enemy with a melee attack."
        if raceChosen == "Orc" or raceChosen == 'orc':
            print "\tMax Health:", int(health + (health * .06)), "\n\tMax Stamina:", int(stamina + (stamina * .06)), "\n\tHealth Regen:", int(healthRegen + (healthRegen * .3))
        if raceChosen == "Breton" or raceChosen == 'breton':
            print "\tMax Magicka:", int(magic + (magic * .1)), "\n\tMagic Resistance increased by 3[x]", "\n\tReduction: Reduces the magicka cost of spells by 3%."
    elif faction == "Imp":
        for race in Imp:
            print race
        print "Choose your race" "(Note this will tell you your unattributed bonus at end-game)"
        raceChosen = raw_input("")
        if raceChosen == 'Imperial' or raceChosen == 'imperial':
            print "\tMax health:",  int(health + (health * .12)), "\n\tMax Stamina:", int(stamina + (stamina*.10)), "\n\tMelee Attacks have a chance to restore 3[x] Healh"
    else:
        faction = ""
        print "Invalid faction, please select again."


print classes
print faction
print raceChosen
if classes == 'nightblade' and raceChosen == 'Khajiit' or raceChosen == 'Bosmer' or raceChosen == 'Orc':
    print "\tWe recommend you play a stamina-based cannon build."
elif classes == 'nightblade' and raceChosen == 'Imperial' or raceChosen == 'Breton':
    print "\tWe recommend you play a sustain-DPS build"
elif classes == 'nightblade' and raceChosen == 'Breton':
    print "\tWe recommend you try/play a Magicka build"
elif classes == 'dragonknight' and raceChosen == 'Redguard' or raceChosen =='Nord' or raceChosen =='Orc':
    print "\tWe recommend you try/play a stamina-based cannon build."
elif classes == 'dragonknight' and raceChosen == 'Imperial' or raceChosen == 'Dunmer':
    print "\tWe recommend you play a tank or magicka-based build."
elif classes == "sorcerer" and raceChosen == 'Altmer' or raceChosen == 'Breton' or raceChosen == 'Imperial':
    print "\tWe recommend you play a magicka-sustain/cannon build."
elif classes == 'Templar' and raceChosen == 'Breton' or raceChosen == 'Altmer' or raceChosen ==  'Imperial':
    print "\tWe recommend a magicka-based build, or a tank or a cannon build."
elif classes == 'Templar' and raceChosen == 'Nord' or raceChosen == 'Bosmer' or raceChosen == 'Redguard' or raceChosen == 'Imperial':
    print "\tWe recommend you play a stamina-based build, or cannon build."

print "\t\tHappy hunting!"
print "\t\tFor builds/addons please see Tamrielfoundry/ESOui online"

os.system("pause")    
    


    
