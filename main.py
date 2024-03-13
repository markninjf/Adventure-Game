print("Choose a story: 1-Defender 2-Stranger 3-Warrior 4-Wizard\n")
answer = input("Take a number or write class: ")

#DEFENDER CHARACTER
from defender import *
if answer in ['1', 'Defender', 'defender']:
    print(defend1)
    
    print("\nChoose the biom: \n1-Forest \n2-Desert \n3-Town \n4-Mountains \n\n")
    location = input("Take a number or write biom: ")
    
    
    #Defender in the forest
    if location in ['1', 'Forest', 'forest']:
        print(defendforest)
        
        #Choice the user for defender character
        print("\nChoose a story: \n1-Stay in the forest and continue to study the clan structure in this land.\n2-Not stay in the forest and continue on your way.\n \n")
        choice_forest = int(input("Take a number: "))
        
        #First story defender
        if choice_forest == 1:
            print(defendforest1)
            
            print("\nChoose a story: \n1-Stay in this land \n2-Return to the Kingdom\n")
            choice1 = int(input("Take a number: "))
            
            #First ending
            if choice1 == 1:
                print(defendland)
            
            #Second ending
            if choice1 == 2:
                print(defendreturn)


        #Second story defender
        if choice_forest == 2:
            print(defendforest2)

            print("\nChoose story:\n1-Unity through Diplomacy \n2-The Wanderer's Legacy \n\n")
            choice2 = int(input("Take a Number: "))
            
            #First ending in the second choice
            if choice2 == 1:
                print(defendfEnd1)
            
            #Second ending in the second choice
            if choice2 == 2:
                print(defendfEnd2)

    
    #Defender in the desert
    if location in ['2', 'Desert', 'desert']:
        print(defendDesert)
        
        print("\nChoose your ending: \n1-Alliance of the Sands \n2-The Guardian of the Sands \n3-The Desert Sovereign \n4-The Nomad's Journey\n\n")
        choice_desert = int(input("Take a number: "))

        #First ending 
        if choice_desert == 1:
            print(defendDesEnd1)
        
        #Second ending
        if choice_desert == 2:
            print(defendDesEnd2)
        
        #Third ending 
        if choice_desert == 3:
            print(defendDesEnd3)
        
        #Fourth ending
        if choice_desert == 4:
            print(defendDesEnd4)
    
    
    #Defender in the Town
    if location in ['3', 'Town', 'town']:
        print(defendTown)
        
        print("\nChoose your ending: \n1-The Guardian of Everwood \n2-The Peacemaker \n3-The Wanderer's Path \n\n")
        choice_town = int(input("Take a number: "))

        #First ending
        if choice_town == 1:
            print(defendTEnd1)
        
        #Second ending
        if choice_town == 2:
            print(defendTEnd2)
        
        #Third ending
        if choice_town == 3:
            print(defendTEnd3)
        
    
    #Defend in the Mountains
    if location in ['4', 'Mountains', 'mountains']:
        print(defendMount)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Summit's Gurdian \n2-The Wayfarer's Path \n3-The Forgotten Depths \n4-The Wanderer's Legacy \n\n")
        choice_mountains = int(input("Take a number: "))

        #First ending
        if choice_mountains == 1:
            print(defendMountEnd1)

        #Second ending
        if choice_mountains == 2:
            print(defendMountEnd2)

        #Third ending
        if choice_mountains == 3:
            print(defendMountEnd3)

        #Fourth ending
        if choice_mountains == 4:
            print(defendMountEnd4)
        
        

#STRANGER CHARACTER
from stranger import *
if answer in ['2', 'Stranger', 'stranger']:
    print(stran2)

    #Choice the biom
    print("\nChoose the biom: \n1-Forest \n2-Desert \n3-Town \n4-Mountains \n\n")
    locationStran = input("Take a number or write biom: ")

    #Stranger in the forest
    if locationStran in ['1', 'Forest', 'forest']:
        print(stranFor)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Guardian's Path \n2-The Wanderer's Journey \n3-The Seeker of Truth \n4-The Keeper of Balance \n\n")
        choice_forestStran = int(input("Take a number: "))

        #First Ending
        if choice_forestStran == 1:
            print(stranForEnd1)
        
        #Second Ending
        if choice_forestStran == 2:
            print(stranForEnd2)
        
        #Third Ending
        if choice_forestStran == 3:
            print(stranForEnd3)
        
        #Fourth Ending
        if choice_forestStran == 4:
            print(stranForEnd4)
    
    
    
    #Stranger in the Desert
    if locationStran in ['2', 'Desert', 'desert']:
        print(stranDes)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Nomad's Embrace \n2-The Oasis's Guardian \n3-The Explorer's Quest \n4-The Sage's Retreat \n\n")
        choice_desertStran = int(input("Take a number: "))

        #First Ending
        if choice_desertStran == 1:
            print(stranDesEnd1)
        
        #Second Ending
        if choice_desertStran == 2:
            print(stranDesEnd2)
        
        #Third Ending
        if choice_desertStran == 3:
            print(stranDesEnd3)
        
        #Fourth Ending
        if choice_desertStran == 4:
            print(stranDesEnd4)
    
    
    
    #Stranger in the Town
    if locationStran in ['3', 'Town', 'town']:
        print(stranTown)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Hero's Call \n2-The Artisan's Craft \n3-The Wanderer's Path \n4-The Enigmatic Departure \n\n")
        choice_townStran = int(input("Take a number: "))

        #First Ending
        if choice_townStran == 1:
            print(stranTownEnd1)
        
        #Second Ending
        if choice_townStran == 2:
            print(stranTownEnd2)
        
        #Third Ending
        if choice_townStran == 3:
            print(stranTownEnd3)
        
        #Fourth Ending
        if choice_townStran == 4:
            print(stranTownEnd4)
    
    
    #Stranger in the Mountains
    if locationStran in ['4', 'Mountains', 'mountains']:
        print(stranMoun)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Summit's Triumph \n2-The Hermit's Solitude \n3-The Wanderer's Redemption \n4-The Timeless Wanderer \n\n")
        choice_mounStran = int(input("Take a number: "))

        #First Ending
        if choice_mounStran == 1:
            print(stranMounEnd1)
        
        #Second Ending
        if choice_mounStran == 2:
            print(stranMounEnd2)
        
        #Third Ending
        if choice_mounStran == 3:
            print(stranMounEnd3)
        
        #Fourth Ending
        if choice_mounStran == 4:
            print(stranMounEnd4)


#WARRIOR CHARACTER
from warrior import *
if answer in ['3', 'Warrior', 'warrior']:
    print(warr3)


    #Choice the biom
    print("\nChoose the biom: \n1-Forest \n2-Desert \n3-Town \n4-Mountains \n\n")
    locationWarr = input("Take a number or write biom: ")

    #Warrior in the forest
    if locationWarr in ['1', 'Forest', 'forest']:
        print(warrFor)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Hermit's Haven \n2-The Seeker's Quest \n3-The Shamma's Wisdom \n4-The Beasmaster's Bond \n\n")
        choice_forestWarr = int(input("Take a number: "))

        #First Ending
        if choice_forestWarr == 1:
            print(warrForEnd1)
        
        #Second Ending
        if choice_forestWarr == 2:
            print(warrForEnd2)
        
        #Third Ending
        if choice_forestWarr == 3:
            print(warrForEnd3)
        
        #Fourth Ending
        if choice_forestWarr == 4:
            print(warrForEnd4)


    #Warrior in the desert
    if locationWarr in ['2', 'Desert', 'desert']:
        print(warrDes)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Guardian of the Dunes \n2-The Seeker of Lost Treasures \n3-The Mystic's Revelation \n4-The Desert King \n5-The Wanderer's Odyssey \n\n")
        choice_desertWarr = int(input("Take a number: "))


        #First Ending
        if choice_desertWarr == 1:
            print(warrDesEnd1)
        
        #Second Ending
        if choice_desertWarr == 2:
            print(warrDesEnd2)    
        
        #Third Ending
        if choice_desertWarr == 3:
            print(warrDesEnd3)    
        
        #Fourth Ending
        if choice_desertWarr == 4:
            print(warrDesEnd4)    
        
        #Fifth Ending
        if choice_desertWarr == 5:
            print(warrDesEnd5)


    #Warrior in the town
    if locationWarr in ['3', 'Town', 'town']:
        print(warrTown)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Artisan's Calling \n2-The Merchant's Fortune \n3-The Scholar's Quest \n4-The Wanderer's Rest \n\n")
        choice_townWarr = int(input("Take a number: "))

        #First Ending
        if choice_townWarr == 1:
            print(warrTownEnd1)

        #Second Ending
        if choice_townWarr == 2:
            print(warrTownEnd2)

        #Third Ending
        if choice_townWarr == 3:
            print(warrTownEnd3)

        #Fourth Ending
        if choice_townWarr == 4:
            print(warrTownEnd4)



    #Warrior in the mountains
    if locationWarr in ['4', 'Mountains', 'mountains']:
        print(warrMoun)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Seeker's Quest \n2-The Elemental Harmony \n3-The Ascension \n4-The Mountain King \n\n")
        choice_mounWarr = int(input("Take a number: "))

        #First Ending
        if choice_mounWarr == 1:
            print(warrMounEnd1)
        
        #Second Ending
        if choice_mounWarr == 2:
            print(warrMounEnd2)
        
        #Third Ending
        if choice_mounWarr == 3:
            print(warrMounEnd3)
        
        #Fourth Ending
        if choice_mounWarr == 4:
            print(warrMounEnd4)



#WIZARD CHARACTER
from wizard import *
if answer in ['4', 'Wizard', 'wizard']:
    print(wiza4)

    #Choice the biom
    print("\nChoose the biom: \n1-Forest \n2-Desert \n3-Town \n4-Mountains \n\n")
    locationWiza = input("Take a number or write biom: ")

    #Wizard in the forest
    if locationWiza in ['1', 'Forest', 'forest']:
        print(wizaFor)


        #Choice the Ending
        print("\nChoose your ending: \n1-The Guardian of Arcane Secrets \n2-The Mystic's Revelation \n3-The Alchemist's Discovery \n4-The Enigma Unsolved \n\n")
        choice_forestWiza = int(input("Take a number: "))

        #First Ending
        if choice_forestWiza == 1:
            print(wizaForEnd1)

        #Second Ending
        if choice_forestWiza == 2:
            print(wizaForEnd2)

        #Third Ending
        if choice_forestWiza == 3:
            print(wizaForEnd3)

        #Fourth Ending    
        if choice_forestWiza == 4:
            print(wizaForEnd4)
    

    #Wizard in the Desert
    if locationWiza in ['2', 'Desert' 'desert']:
        print(wizaDes)


        #Choice the Ending
        print("\nChoose your ending: \n1-The Mirage of Illusion \n2-The Elemental Convergence \n3-The Nomad's Fortune \n4-The Cryptic Ruins \n\n")
        choice_desertWiza = int(input("Take a number: "))

        #First Ending
        if choice_desertWiza == 1:
            print(wizaDesEnd1)

        #Second Ending
        if choice_desertWiza == 2:
            print(wizaDesEnd2)

        #Third Ending
        if choice_desertWiza == 3:
            print(wizaDesEnd3)

        #Fourth Ending    
        if choice_desertWiza == 4:
            print(wizaDesEnd4)



    #Wizard in the Town
    if locationWiza in ['3', 'Town' 'town']:
        print(wizaTown)


        #Choice the Ending
        print("\nChoose your ending: \n1-The Alchemist's \n2-The Defender's Resolve \n3-The Scholar's Pursuit \n4-The Illusionist's Legacy \n\n")
        choice_townWiza = int(input("Take a number: "))

        #First Ending
        if choice_townWiza == 1:
            print(wizaTownEnd1)

        #Second Ending
        if choice_townWiza == 2:
            print(wizaTownEnd2)

        #Third Ending
        if choice_townWiza == 3:
            print(wizaTownEnd3)

        #Fourth Ending    
        if choice_townWiza == 4:
            print(wizaTownEnd4)


    #Wizard in the Mountains
    if locationWiza in ['4', 'Mountains' 'mountains']:
        print(wizaMoun)

        #Choice the Ending
        print("\nChoose your ending: \n1-The Guardian of the Pass \n2-The Elemental Convergence \n3-The Sage's Enligtenment \n4-The Mystic's Curse \n\n")
        choice_mounWiza = int(input("Take a number: "))


        #First Ending
        if choice_mounWiza == 1:
            print(wizaMounEnd1)

        #Second Ending
        if choice_mounWiza == 2:
            print(wizaMounEnd2)

        #Third Ending
        if choice_mounWiza == 3:
            print(wizaMounEnd3)

        #Fourth Ending    
        if choice_mounWiza == 4:
            print(wizaMounEnd4)
    