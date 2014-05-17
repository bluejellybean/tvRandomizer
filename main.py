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
        self.showDirectory = r"Z:\\Public\\AWESOME DOPE MOVIE FOLDER\\Dope TV Shows\\"
        self.saveDirectory = self.showDirectory + "__randomSaves\\"
        self.saveFile = ""
        self.fullEpisodeList = []               #
        self.nextEpisodeToPlay = ""
    
    def __getFilesInTvShow(self):

        for root, dirs, files in os.walk(self.showDirectory + self.showTitle):
            for name in dirs:
                try:
                   
                    seasons = os.listdir(self.showDirectory + self.showTitle+ '/' + name)
                    
                    for episode in seasons:
                         
                        if episode != "Thumbs.db":
                            eiposdePath = name + '\\' + episode 
                            self.fullEpisodeList.append(eiposdePath)

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
            self.nextEpisodeToPlay = self.fullEpisodeList[0]
            print self.nextEpisodeToPlay
            f.close()

        except:
            print('unable to read from save file...')
            sys.exit()

    def __randomizeShowOrder(self):

        self.__getFilesInTvShow()
        random.shuffle(self.fullEpisodeList)

        self.__saveShowListToFile()

    #this should maybe allow the user to change dir, hardcoded to my own dir atm
    def setShowDirectory(self):

        print self.showDirectory

    def handleUserArguents(self):

        if self.userArgument == "-randomize":
            self.__randomizeShowOrder()
        #"switch" here?

    def __setUserArgument(self):

        dashIndex = self.userInput.index("-")
        userArg = self.userInput[dashIndex:]
        self.userArgument = userArg

    #TODO: change this to work with next episode
    def playSingleEpsiode(self):

        episodePath =self.showDirectory + self.showTitle + '\\' + self.nextEpisodeToPlay
       
        p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",episodePath, '--play-and-exit', '--fullscreen'])

    def startShow(self):

        if self.userArgument == "":
            print('read file, play newest file, appendpop to end')
            self.__openShowListFromFile()
            self.fullEpisodeList.append(self.fullEpisodeList.pop(0))
            self.__saveShowListToFile()

            self.playSingleEpsiode()

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
        self.userInput = "Family Guy"
        self.__setUserInputs()



tv = TvShows()
tv.getAndSetUserInput()

tv.startShow()

    
