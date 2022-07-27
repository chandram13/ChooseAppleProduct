# Marvish Chandra

'''This program is intended to help the user decide on what Apple application they can use to fit their needs.'''

class appleProducts:

def video():

videoPrograms = ("iMovie", "QuickTime", "Final Cut Pro X", "DVD Player")

for vp in videoPrograms:
    print(vp)
userVideo = input("What Apple video product would you like to use?")
print(userVideo)

def productivity():

productivityPrograms = ("Calculator", "FaceTime", "KeyNote", "Mail", "Messages", "Notes", "Numbers", "Pages", "Preview", "TextEdit")
for pp in productivityPrograms:
    print(pp)
userProductivity = input("What Apple productivity product would you like to use?")
print(userProductivity)

def audio():

audioPrograms = ("Garageband", "Logic Pro X", "Music", "Podcasts")
for ap in audioPrograms:
    print(ap)
userAudio = input("What Apple audio product would you like to use?")
print(userAudio)

