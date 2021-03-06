import random
import time

# World Variables ------------------
_5Stars = [
    "Keqing",
    "Mona",
    "Qiqi",
    "Jean",
    "Diluc",
    "Amos Bow",
    "Skyward Harp",
    "Lost Prayer To The Sacred Winds",
    "Skyward Atlas",
    "Primordial Jade Winged-Spear",
    "Skyward Spine",
    "Wolf's Gravestone",
    "Skyward Pride",
    "Skyward Blade",
    "Aquila Favonia",
]
_4Stars = [
    "Sucrose",
    "Chongyun",
    "Noelle",
    "Bennett",
    "Fischl",
    "Ningguang",
    "Xingqiu",
    "Beidou",
    "Xiangling",
    "Amber",
    "Razor",
    "Kaeya",
    "Barbara",
    "Lisa",
    "Rust",
    "Sacrificial Bow",
    "The Stringless",
    "Favonius Warbow",
    "Eye Of Perception",
    "Sacrificial Fragments",
    "The Widsithv",
    "Favonius Codex",
    "Favonius Lance",
    "Dragon's Bane",
    "Rainslasher",
    "Sacrificial Greatsword",
    "The Bell",
    "Favonius Greatsword",
    "Lions Roar",
    "Sacrificial Sword",
    "The Flute",
    "Favonius Sword",
]
_3Stars = [
    "Slingshot",
    "Sharpshooter's Oath",
    "Raven Bow",
    "Emerald Orb",
    "Thrilling Tales Of Dragon Slayers",
    "Magic Guide",
    "Black Tassel",
    "Debate Club",
    "Bloodtainted Greatsword",
    "Ferrous Shadow",
    "Skyrider Sword",
    "Harbinger Of Dawn",
    "Cool Steel",
]

inventory = {
    "5Stars": ["MC"],
    "4Stars": [],
    "3Stars": [],
}

global pulls_since_5 
pulls_since_5 = 0
global pulls_since_4
pulls_since_4 = 0

# Functions -------------------------
def starAnimation(stuffGot):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.25)
    print("`")
    time.sleep(0.25)
    print('  `')
    time.sleep(0.25)
    print('    `')
    time.sleep(0.25)
    print('      `')
    time.sleep(0.25)
    print('       `   *  ')
    time.sleep(0.25)
    print('     * (    #    ) *         ')
    time.sleep(0.25)
    print('      *(   #***#   )*      ')
    time.sleep(0.25)
    print('        * (  # ) *        ')
    time.sleep(0.25)
    print('            *           ')
    time.sleep(0.25)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    
    print("---- Pulled ----")
    for stuff in stuffGot:
        print(stuff)
    
def getPull(rarity):
    if rarity == 5:
        l = len(_5Stars) -1
        num = random.randint(0,l)
        pull = _5Stars[num]
        inventory["5Stars"].append(pull)
        return pull +" **"
    elif rarity == 4:
        l = len(_4Stars) -1
        num = random.randint(0,l) 
        pull = _4Stars[num]
        inventory["4Stars"].append(pull)
        return pull + " *"
    else:
        l = len(_3Stars) -1 
        num = random.randint(0,l)
        pull = _3Stars[num]
        inventory["3Stars"].append(pull)
        return pull

def makeWish(ammount):
    stuffGot = [];
    animation = False
    global pulls_since_5
    global pulls_since_4
    
    for val in range(0,ammount):
        if pulls_since_5 >= 89:
            stuffGot.append(getPull(5))
            animation = True
            pulls_since_5  = 0
            pulls_since_4  = 0
        elif pulls_since_4 >= 9:
            stuffGot.append(getPull(4))
            animation = True
            pulls_since_5 += 1
            pulls_since_4  = 0
        else:
            num = random.randint(0,1000)
            if num >= 994:
                stuffGot.append(getPull(5))
                animation = True
                pulls_since_5  = 0
            elif num < 994 and num >= 943:
                stuffGot.append(getPull(4))
                animation = True
                pulls_since_5 += 1
                pulls_since_4  = 0
            else :
                stuffGot.append(getPull(3))
                pulls_since_4 += 1
                pulls_since_5 += 1
                
    if animation:
        starAnimation(stuffGot)
    else:
        print("---- Pulled ----")
        for stuff in stuffGot:
            print(stuff)
    start()

def start():
    print("--------------------------------------------")
    userInput = input()
    try:
        if int(userInput) >0:#<= 10:
            makeWish(int(userInput))
    except:
        if userInput.lower() == 'inventory':
            print("~~ 5 Stars ~~\n")
            for x in inventory['5Stars']:
                print(x)
            print("~~ 4 Stars ~~\n")
            for x in inventory['4Stars']:
                print(x)
            #print("~~ Junk ~~\n")
            #for x in inventory['3Stars']:
            #    print(x)
            start()
        elif userInput.lower() == 'q':
            quit()
        else:
            print("Dumbbutt do it right")
            start()
    

# Start -----------------------------
print()
print("Welcome let me explain how to use this program :)")
print("Simply type the number of pulls you wish to make (10 max) \nor type 'Inventory' to see your inventory")
print("Thats all there is to know! Have Fun!! ")
print()
start()