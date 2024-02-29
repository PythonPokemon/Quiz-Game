print("Willkommen zu unserem Computer Quiz!") 

playing = input("möchtest du spielen?") 

if playing != "ja": 
    quit()

print("Okay, lass uns spielen:-) ")
score = 0

answer = input("Achte auf groß -und kleinschrift, wenn du bereit bist schreibe -->OK<-- ")
if answer == "OK":
    print('Los gehts')
    score += 1 
else:
    print("falsch!___Trinke_Ayran_werde_Hayvan___#Spoiler___Jobcenter") 

answer = input("Wie heißt die Beste Programmiersprache der Welt? ") 
if answer == "Python": 
    print('Richtig')
    score += 1
else:
    print("falsch!___Trinke_Ayran_werde_Hayvan___#Spoiler___Python") 

answer = input("Wie lautet die Abkürzung unseres Bildunsträgers? ") 
if answer == "GFN": 
    print('Richtig')
    score += 1
else:
    print("falsch!___Trinke_Ayran_werde_Hayvan___#Spoiler___GFN") 

answer = input("Wer bezahlt diese Umschulung? ")
if answer == "Jobcenter":
    print('Richtig')
    score += 1
else:
    print("falsch!___Trinke_Ayran_werde_Hayvan___#Spoiler___Jobcenter") 

answer = input("Wie lange dauert die Umschulung in Jahren? ") 
if answer == "2": 
    print('Richtig')
    score += 1
else:
    print("falsch!___Trinke_Ayran_werde_Hayvan___#Spoiler___2") 

print("Du hast " + str(score) + "/5 Bismillah____Allhamdullilah____du wurdest erleuchtet:-)")
print("Du hast " + str((score / 5) * 100) + " %.") 
