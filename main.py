import random
from tkinter import *

import pygame

potion = 0
mrwebbcured = 0
bed = 0
bucket = 0
woodenpick = 0
ironpick = 0
diamondpick = 0
waterbucket = 0
blazepowder = 0
enderpearls = 0
location_dict = {1: 'Cobbled Cliffs', 2: 'Snowy Snowland', 3: 'Village', 4: 'Vengeful Desert', 5: 'Intense Inferno'}
pygame.mixer.init()


def explain():
    logo.destroy()
    text1.config(text="Objective: defeat the Ender Dragon by choosing your way to victory.")
    text1.place(relx=0.5, rely=0.5, anchor=CENTER)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Continue", command=gamestart)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    pygame.mixer.music.load("minecraft.wav")
    pygame.mixer.music.play(-1)


def gamestart():
    global woodenpick
    global ironpick
    global diamondpick
    global menubar1
    global wwultd
    spawn = random.randint(1, 5)
    location_string = location_dict[spawn]
    text1.config(text="You have spawned in the " + location_string + ".")
    if spawn == 1:
        image = Label(image=cobbledcliffsimage)
        image.place(x=110, y=0, anchor=NW)
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Climb", command=climb)
        filemenu1.add_command(label="Mine", command=mine)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either climb the mountain or mine cobblestone.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif spawn == 2:
        image = Label(image=snowysnowland)
        image.place(x=110, y=0, anchor=NW)
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Snow Hut", command=snowhut)
        filemenu1.add_command(label="Igloo", command=igloo)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either make a snow hut or find a igloo.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif spawn == 3:
        image = Label(image=villages)
        image.place(x=110, y=0, anchor=NW)
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Iron Golem", command=golem)
        filemenu1.add_command(label="Loot", command=loot)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either fight the Iron Golem or loot the village.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif spawn == 4:
        image = Label(image=vengefuldesert)
        image.place(x=110, y=0, anchor=NW)
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Cactus", command=cactus)
        filemenu1.add_command(label="Oasis", command=oasis)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either destroy cactus or go to the Oasis.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif spawn == 5:
        image = Label(image=intenseinferno)
        image.place(x=110, y=0, anchor=NW)
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Investigate", command=investigatelava)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You went to the Intense Inferno ")
        wwultd.config(text="You can only investigate the lava.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def climb():
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Keep Looking", command=search)
    filemenu1.add_command(label="Go Down", command=godown)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You decided to climb the mountain just to find nothing...")
    wwultd.config(text="You can either keep looking around or go down\nthe mountain.")
    wwultd.place(relx=0.5, rely=0.61, anchor=S)


def mine():
    global woodenpick
    global ironpick
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Chasm", command=chasm)
    filemenu1.add_command(label="Oasis", command=oasis)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You decided to mine in the mountain until you upgraded to a iron pickaxe.")
    wwultd.config(text="You can either go to the chasm or to the oasis.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)
    woodenpick += 1
    ironpick += 1


def search():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    menubar1.destroy()
    text1.config(text="You died of the low temperature.")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def godown():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    menubar1.destroy()
    text1.config(text="You decided to go down the mountain but you died of low temperature.")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def snowhut():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You couldn't finish making it so you died of the cold temperature...")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def igloo():
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Cobbled Cliffs", command=cobbledcliffs)
    filemenu1.add_command(label="Basement", command=basement)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You found a igloo in the Snowy Snowland.")
    wwultd.config(text="You can either run to cobbled cliffs or loot the basement.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def cobbledcliffs():
    global wwultd
    global menubar1
    global image
    image = Label(image=cobbledcliffsimage)
    image.config(image=cobbledcliffsimage)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Climb", command=climb)
    filemenu1.add_command(label="Mine", command=mine)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You ran to the Cobbled Cliffs to mine some stone.")
    wwultd.config(text="You can either climb the mountain or mine cobblestone.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def basement():
    global potion
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Cobbled Cliffs", command=cobbledcliffs)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You looted the basement and found a potion which you saved for later.")
    potion += 1
    wwultd.config(text="You can only go to the Cobbled Cliffs.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def golem():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You decided to fight the Iron Golem but it was too strong and you died...")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def loot():
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Chasm", command=chasm)
    filemenu1.add_command(label="Beds", command=beds)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You looted the village and found some food and Emeralds.")
    wwultd.config(text="You can either go into the chasm or take the Villager's beds.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def beds():
    global bed
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Chasm", command=chasm)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You took the Villager's beds for later.")
    bed += 1
    wwultd.config(text="You can only go into the chasm.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def chasm():
    global mrwebbcured
    global wwultd
    global menubar1
    image = Label(image=chasmimage)
    image.config(image=chasmimage)
    image.place(x=110, y=0, anchor=NW)
    if mrwebbcured == 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Mine", command=minechasm)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You climbed down into the deep chasm.")
        wwultd.config(text="You can only mine.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif mrwebbcured == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Mine", command=minechasm)
        filemenu1.add_command(label="Investigate", command=investigate)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You climbed down into the deep chasm.")
        wwultd.config(text="You can either mine or investigate a pair of red lights in the dark.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def investigate():
    global potion
    global wwultd
    global menubar1
    global image
    image = Label(image=zbmrwebb)
    image.config(image=zbmrwebb)
    image.place(x=110, y=0, anchor=NW)
    pygame.mixer.music.load("cave.wav")
    pygame.mixer.music.play(0)
    if potion == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Ignore", command=ignore)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You investigated the pair of red lights and found MR. WEBB?!\nAs a Zombie Villager?!")
        wwultd.config(text="You can only ignore him.")
        wwultd.place(relx=0.5, rely=0.585, anchor=S)
    elif potion == 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Ignore", command=ignore)
        filemenu1.add_command(label="Cure", command=cure)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You investigated the pair of red lights and found MR. WEBB?!\nAs a Zombie Villager?!")
        wwultd.config(text="You can either ignore him or cure him with your potion.")
        wwultd.place(relx=0.5, rely=0.585, anchor=S)


def ignore():
    global ironpick
    global diamondpick
    global wwultd
    global menubar1
    global image
    image = Label(image=chasmimage)
    image.config(image=chasmimage)
    image.place(x=110, y=0, anchor=NW)
    pygame.mixer.music.load("minecraft.wav")
    pygame.mixer.music.play(-1)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Enter Portal", command=portal)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You decided to mine until you got a Diamond Pickaxe and a Nether Portal.")
    wwultd.config(text="You can only enter the portal.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)
    ironpick += 1
    diamondpick += 1


def minechasm():
    global ironpick
    global diamondpick
    global wwultd
    global menubar1
    global image
    pygame.mixer.music.load("minecraft.wav")
    pygame.mixer.music.play(-1)
    image = Label(image=chasmimage)
    image.config(image=chasmimage)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Enter Portal", command=portal)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You decided to mine until you got a Diamond Pickaxe and a Nether Portal.")
    wwultd.config(text="You can only enter the portal.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)
    ironpick += 1
    diamondpick += 1


def cure():
    global mrwebbcured
    global potion
    global wwultd
    global menubar1
    global image
    image = Label(image=chasmimage)
    image.config(image=chasmimage)
    image.place(x=110, y=0, anchor=NW)
    pygame.mixer.music.load("villager.wav")
    pygame.mixer.music.play(0)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Mine", command=minechasm)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(
        text="You decided to cure Mr. Webb.\nWhen he turned back into a Villager he thanked you for your efforts.")
    wwultd.config(text="You can only mine in the chasm.")
    wwultd.place(relx=0.5, rely=0.585, anchor=S)
    potion -= 0
    mrwebbcured += 1


def cactus():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You decided to destroy cactus for no reason.\nBefore you knew it, it was nighttime and you died...")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def oasis():
    global wwultd
    global menubar1
    global image
    image = Label(image=vengefuldesert)
    image.config(image=vengefuldesert)
    image.place(x=110, y=0, anchor=NW)
    if bucket == 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Water", command=water)
        filemenu1.add_command(label="Craft", command=craft)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You found a oasis with water!")
        wwultd.config(text="You can either grab some water or craft a wooden pickaxe")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif bucket == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Craft", command=craft)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You found a oasis with water!")
        wwultd.config(text="You can only craft a wooden pickaxe.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def craft():
    global wwultd
    global menubar1
    global woodenpick
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Loot Pyramid", command=pyramid)
    filemenu1.add_command(label="Cobbled Cliffs", command=cobbledcliffs)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You crafted a wooden pickaxe!")
    wwultd.config(text="You can either loot the pyramid or go to the Cobbled Cliffs")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)
    woodenpick += 1


def water():
    global wwultd
    global menubar1
    global bucket
    global waterbucket
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Intense Inferno", command=intenseinferno)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You collected some water with your bucket!")
    wwultd.config(text="You can only go to the Intense Inferno")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)
    bucket -= 1
    waterbucket += 1


def pyramid():
    global wwultd
    global menubar1
    global ironpick
    ironpick += 1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Village", command=village)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You looted the Pyramid and got a Iron Pickaxe!")
    wwultd.config(text="You can only go to the village")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def village():
    global wwultd
    global menubar1
    global image
    image = Label(image=villages)
    image.config(image=villages)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Iron Golem", command=golem)
    filemenu1.add_command(label="Loot", command=loot)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You went to the Village!")
    wwultd.config(text="You can either fight the Iron Golem or loot the village.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def intenseinferno():
    global woodenpick
    global ironpick
    global diamondpick
    global wwultd
    global menubar1
    global image
    image = Label(image=intenseinferno)
    image.config(image=intenseinferno)
    image.place(x=110, y=0, anchor=NW)
    if woodenpick >= 1 or ironpick >= 1 or diamondpick >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Mine", command=mineunderground)
        filemenu1.add_command(label="Investigate", command=investigatelava)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You went to the Intense Inferno ")
        wwultd.config(text="You can either mine underground or go investigate the lava.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    else:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Investigate", command=investigatelava)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You went to the Intense Inferno ")
        wwultd.config(text="You can only investigate the lava.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def mineunderground():
    global ironpick
    global diamondpick
    global wwultd
    global menubar1
    text1.config(text="You mined underground but lava started to pour out of a hole close to you!")
    if ironpick >= 1 or diamondpick >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Mine Away", command=live)
        filemenu1.add_command(label="Accept Fate", command=die)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either mine away or accept your fate.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    else:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Accept Fate", command=die)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can only accept your fate.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def investigatelava():
    global wwultd
    global menubar1
    global image
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You investigated the lava but you fell in and got boiled to a pulp.")
    wwultd.destroy()


def live():
    global waterbucket
    global bucket
    global wwultd
    global menubar1
    if waterbucket >= 1 and bucket == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
        waterbucket -= 1
        bucket += 1
    elif bucket >= 1 and waterbucket == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif bucket > waterbucket > 0 and bucket > 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif waterbucket > bucket > 0 and waterbucket > 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
        waterbucket -= 1
        bucket += 1
    elif bucket >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif waterbucket >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Make Portal", command=portal)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You mined away just in time!")
        wwultd.config(text="You can collect lava and make a portal.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
        waterbucket -= 1
        bucket += 1
    elif bucket == 0 and waterbucket == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Vengeful Desert", command=vengefuldesert)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You don't have anything to make a portal with...")
        wwultd.config(text="You can only go to the Vengeful Desert.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def vengefuldesert():
    global menubar1
    global wwultd
    global image
    image = Label(image=vengefuldesert)
    image.config(image=vengefuldesert)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Cactus", command=cactus)
    filemenu1.add_command(label="Oasis", command=oasis)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You have gone to the Vengeful Desert")
    wwultd.config(text="You can either destroy cactus or go to the Oasis.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def die():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You tried to mine away but the lava caught up\nto you and you burned into a crisp.")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def portal():
    global wwultd
    global menubar1
    global image
    image = Label(image=nether)
    image.config(image=nether)
    image.place(x=110, y=0, anchor=NW)
    portalspawn = random.randint(1, 10)
    pygame.mixer.music.load("concretehalls.wav")
    pygame.mixer.music.play(-1)
    if portalspawn == 5:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Nether Fortress", command=fortress)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(
            text="You stepped into the portal entered the Nether.\nWhen you entered you were lucky and spawned next "
                 "to a Nether fortress!")
        wwultd.config(text="You can only go into the Nether fortress")
        wwultd.place(relx=0.5, rely=0.585, anchor=S)
    elif portalspawn != 5:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Cheat", command=cheat)
        filemenu1.add_command(label="Trade", command=trade)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You stepped into the portal entered the Nether")
        wwultd.config(text="You can either cheat using Chunkbase or trade with Piglins for ender pearls.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def cheat():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You were caught cheating so you canceled the speedrun...")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def fortress():
    global blazepowder
    global enderpearls
    global menubar1
    global wwultd
    text1.config(text="You went into the Nether fortress and demolished some blazes.")
    blazepowder = 1
    if enderpearls == 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Craft", command=craftpearls)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can only craft eyes of ender.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif enderpearls == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Trade", command=trade)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can only trade with Piglins.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def trade():
    global enderpearls
    global blazepowder
    global menubar1
    global wwultd
    text1.config(text="You have traded with Piglins for ender pearls.")
    enderpearls = 1
    if blazepowder == 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Craft", command=craftpearls)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can craft eyes of ender.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    elif blazepowder == 0:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Nether Fortress", command=fortress)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can only go find a Nether fortress.")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)


def craftpearls():
    global menubar1
    global wwultd
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Enter Portal", command=endportal)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(
        text="You crafted eyes of ender and went into the Overworld.\nAfter you went into the Overworld you searched "
             "for a\nEnd Portal and you activated it.")
    text1.place(relx=0.5, rely=0.58, anchor=S)
    wwultd.config(text="You can only enter the End Portal.")
    wwultd.place(relx=0.5, rely=0.62, anchor=S)


def endportal():
    global menubar1
    global wwultd
    global image
    image = Label(image=end)
    image.config(image=end)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Shoot", command=shoot)
    filemenu1.add_command(label="Destroy", command=destroy)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You jumped into the End Portal.\nThe final fight, this is what you have been waiting for!.")
    text1.place(relx=0.5, rely=0.5, anchor=CENTER)
    wwultd.config(text="You can either shoot down the ender crystals\nor just destroy the Dragon while it's perched.")
    wwultd.place(relx=0.5, rely=0.585, anchor=S)
    pygame.mixer.music.load("calm4.wav")
    pygame.mixer.music.play(-1)


def shoot():
    global menubar1
    global wwultd
    global bed
    text1.config(text="You shot down the end crystals with your bow.\nThere are now 2 left but they are in cages.")
    if bed >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Pillar Up", command=pillar)
        filemenu1.add_command(label="Bed Camp", command=bedcamp)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can either pillar up to the last 2 or bed camp.")
        wwultd.place(relx=0.5, rely=0.585, anchor=S)
    else:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Pillar Up", command=pillar)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        wwultd.config(text="You can only pillar up to the last 2.")
        wwultd.place(relx=0.5, rely=0.585, anchor=S)


def destroy():
    global wwultd
    global menubar1
    global image
    image = Label(image=dead)
    image.config(image=dead)
    image.place(x=110, y=0, anchor=NW)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(text="You accidentally looked at a Enderman, it got mad and attacked you.")
    wwultd.destroy()
    pygame.mixer.music.load("oof.wav")
    pygame.mixer.music.play(0)


def pillar():
    global menubar1
    global wwultd
    global waterbucket
    global image
    if waterbucket >= 1:
        menubar1 = Menu(window1)
        filemenu1 = Menu(menubar1, tearoff=0)
        filemenu1.add_command(label="Attack Dragon", command=attack)
        menubar1.add_cascade(label="Options", menu=filemenu1)
        window1.config(menu=menubar1)
        text1.config(text="You destroyed the End Crystals and water clutched down!")
        wwultd.config(text="You can only attack the Ender Dragon")
        wwultd.place(relx=0.5, rely=0.565, anchor=S)
    else:
        image = Label(image=dead)
        image.config(image=dead)
        image.place(x=110, y=0, anchor=NW)
        filemenu1 = Menu(menubar1, tearoff=0)
        window1.config(menu=menubar1)
        menubar1.destroy()
        text1.config(text="You destroyed the End Crystals and\n jumped off hoping for the best and well,\n you died...")
        wwultd.destroy()
        pygame.mixer.music.load("oof.wav")
        pygame.mixer.music.play(0)


def bedcamp():
    global wwultd
    global menubar1
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Grab Egg", command=grabegg)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You took out your beds and you tried to sleep in it\ncausing a explosion destroying the Dragon!")
    wwultd.config(text="You can only grab the egg and win.")
    wwultd.place(relx=0.5, rely=0.585, anchor=S)


def attack():
    global wwultd
    global menubar1
    image = Label(image=end)
    image.config(image=end)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Grab Egg", command=grabegg)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(text="You pulled out your sword and destroyed the Dragon!")
    wwultd.config(text="You can only grab the egg and win.")
    wwultd.place(relx=0.5, rely=0.565, anchor=S)


def grabegg():
    global wwultd
    global menubar1
    global image
    image = Label(image=villages)
    image.config(image=villages)
    image.place(x=110, y=0, anchor=NW)
    menubar1 = Menu(window1)
    filemenu1 = Menu(menubar1, tearoff=0)
    filemenu1.add_command(label="Credits", command=creditsscene)
    menubar1.add_cascade(label="Options", menu=filemenu1)
    window1.config(menu=menubar1)
    text1.config(
        text="With you taking the Egg and going into the portal\nyou have just saved the world.\nThe Villagers at the "
             "village congratulate you for your deeds!")
    text1.place(relx=0.5, rely=0.58, anchor=S)
    wwultd.config(text="You can only read the end credits.")
    wwultd.place(relx=0.5, rely=0.62, anchor=S)


def creditsscene():
    global wwultd
    global menubar1
    global image
    image = Label(image=smurf)
    image.config(image=smurf)
    image.place(x=110, y=0, anchor=NW)
    pygame.mixer.music.load("thespectre.wav")
    pygame.mixer.music.play(-1)
    filemenu1 = Menu(menubar1, tearoff=0)
    window1.config(menu=menubar1)
    menubar1.destroy()
    text1.config(
        text="Thank you for playing my choose your adventure game!\nMusic by C418, Markus Persson and Alan Walker.\nMinecraft font and cobblestone "
             "texture by Mojang.\nMinecraft dirt block icon by Mojang\nAll rights by Mojang and the Python "
             "modules.\nIdea and code by Landon Perkins.")
    text1.place(relx=0.5, rely=0.7, anchor=S)
    wwultd.destroy()


def creditsinfo():
    creditswindow = Toplevel(window1)
    creditswindow.minsize(301, 96)
    creditswindow.maxsize(301, 96)
    creditswindow.resizable(0, 0)
    creditswindow.title("Credits")
    creditslabel = Label(creditswindow,
                         text="Thank you for playing my choose your adventure game!\nMusic by C418, Markus Persson and Alan Walker.\nMinecraft font and cobblestone texture by Mojang.\nMinecraft dirt block icon by Mojang\nAll rights by Mojang and the Python modules.\nIdea and code by Landon Perkins")
    creditslabel.pack()


window1 = Tk()
window1.geometry("400x400")
window1.title("Minestory")
window1.minsize(400, 400)
window1.maxsize(400, 400)
window1.resizable(0, 0)
wwultd = Label(window1, text="")
wwultd.place(relx=0.5, rely=0.565, anchor=S)
icon = PhotoImage(file='logo.png')
window1.iconphoto(True, icon)
menubar1 = Menu(window1)
filemenu1 = Menu(menubar1, tearoff=0)
filemenu1.add_command(label="Yes", command=explain)
filemenu1.add_command(label="No")
menubar1.add_cascade(label="Options", menu=filemenu1)
window1.config(menu=menubar1)
filemenu2 = Menu(menubar1, tearoff=0)
filemenu2.add_command(label="Credits", command=creditsinfo)
menubar1.add_cascade(label="Help", menu=filemenu2)
window1.config(menu=menubar1)
minestorylogo = PhotoImage(file='minestorylogo.png')
cobbledcliffsimage = PhotoImage(file='cobbledcliffs.png')
snowysnowland = PhotoImage(file='snowysnowland.png')
villages = PhotoImage(file='village.png')
chasmimage = PhotoImage(file='chasm.png')
vengefuldesert = PhotoImage(file='vengefuldesert.png')
intenseinferno = PhotoImage(file='intenseinferno.png')
nether = PhotoImage(file='nether.png')
end = PhotoImage(file='end.png')
smurf = PhotoImage(file='smurf.png')
zbmrwebb = PhotoImage(file='zbmrwebb.png')
dead = PhotoImage(file='dead.png')
logo = Label(window1, image=minestorylogo)
logo.pack()
text1 = Label(window1,
              text="Welcome to Minestory,\n a Minecraft inspired choose your own adventure game!\nPick what you want "
                   "to do in the options tab during your story\n to choose what happens.\nDo you want to start the "
                   "game?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAll assets not made by me are by Microsoft and Mojang")
text1.place(relx=0.5, rely=1, anchor=S)
pygame.mixer.music.load("wethands.wav")
pygame.mixer.music.play(-1)
window1.mainloop()
