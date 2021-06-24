primary = int(input('What is your Primary Weapons attack stat? '))
secondary = int(input('What is your Secondary Weapons attack stat? '))
heavy = int(input('What is your Heavy Weapons attack stat? '))
ghost = int(input('What is the defense of your Ghost? '))
helmet = int(input('What is the defense of your Helmet? '))
gauntlets = int(input('What is the defense of your Gauntlets? '))
chest = int(input('What is the defense of your Chest Armor? '))
legs = int(input('What is the defense stat of your Leg Armor? '))
class_item = int(input('What is the defense stat of your Guardians Class Item? '))
artifact = input('What is the defense stat of your Artifact? If guardian is below level 40, input NA. ')
if (artifact) == str:
    ttl = primary + secondary + heavy + ghost + helmet + gauntlets + chest + legs + class_item
    light_lvl = ttl / 9
    print('Because your guradian is below level 40, it cannot have a light level. However, its theoretical light level is %d.' % light_lvl)
else:
    ttl = primary + secondary + heavy + ghost + helmet + gauntlets + chest + legs + class_item + int(artifact)
    light_lvl = ttl / 10
    print('Congratulations! You have a guardian above level 40. Your guardians light level is %d.' % light_lvl)

