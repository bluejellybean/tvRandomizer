import time
import os
import signal
import sys
import random
import subprocess

#better name for this? it will end up being the main class holding
#data for dirs, tv names, user args and such
class TvShows:
    def __init__(self):
        self.userInput = ""
        self.showTitle = ""
        self.userArgument = ""
        self.showDirectory = "//AWESOMEPCV2/Users/Public/AWESOME DOPE MOVIE FOLDER/Dope tv shows/"
        self.saveDirectory = self.showDirectory + "__randomSaves/"
        self.saveFile = ""
        self.fullEpisodeList = []
    
    def __getFilesInTvShow(self):
        print('here')
        for root, dirs, files in os.walk(self.showDirectory + self.showTitle):
            for name in dirs:
                try:
                    seasons = os.listdir(self.showDirectory + self.showTitle+ '/' + name)
                    for episode in seasons:
                        if episode != "Thumbs.db":
                            self.fullEpisodeList.append(episode)

                except WindowsError:
                    print 'Skipping', os.path.join(root, name)

    def __saveShowListToFile(self):
        f = open(self.saveFile, 'w')
        for episode in self.fullEpisodeList:
            f.write(episode+'\n')
        f.close()

    def __openShowListFromFile(self):
        try:
            f = open(self.saveFile, 'r')         ####a###########create text file, change path. 
            self.fullEpisodeList = f.read().splitlines()
            f.close()
            print self.fullEpisodeList

        except:
            print('unable to read from file')
            sys.exit()

    def __randomizeShowOrder(self):
        self.__getFilesInTvShow()
        random.shuffle(self.fullEpisodeList)

        self.__saveShowListToFile()

    #this should maybe allow the user to change dir, hardcoded to my own dir atm
    def setShowDirectory(self):
        print self.showDirectory
        #print('love')

    def handleUserArguents(self):
        print self.userArgument
        if self.userArgument == "-randomize":
            self.__randomizeShowOrder()
        #"switch" here?

    def __setUserArgument(self):
        dashIndex = self.userInput.index("-")
        userArg = self.userInput[dashIndex:]
        self.userArgument = userArg

    #TODO: change this to work with next episode
    def playSingleEpsiode(self):
        p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","C:\\\Users\Alex\Desktop\Anchorman2.mp4", '--play-and-exit', '--fullscreen'], shell=True)


    def startShow(self):
        if self.userArgument == "":
            print('read file, play newest file, appendpop to end')
            self.__openShowListFromFile()
        else:
            self.handleUserArguents()

    def __setShowTitle(self):
        if "-" in self.userInput:
            dashIndex = self.userInput.index("-")
            if (self.userInput[dashIndex - 1]) == " ":
                self.showTitle = self.userInput[0:dashIndex - 1]
            else:
                self.showTitle = self.userInput[0:dashIndex]
        else:
            self.showTitle = self.userInput

    def __setUserInputs(self):
        if "-" in self.userInput:
            self.__setUserArgument()
        self.__setShowTitle()
        self.__setSaveFile()

    def __setSaveFile(self):
        self.saveFile = self.saveDirectory + self.showTitle + ".txt"
      

    def getAndSetUserInput(self):
        #self.userInput = raw_input("Enter movie title: ")
        #temp hardcoded because sublimes compiler can't handle input
        self.userInput = "Star trek"
        self.__setUserInputs()



tv = TvShows()
tv.getAndSetUserInput()

tv.startShow()





    
