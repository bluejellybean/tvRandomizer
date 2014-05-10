import time
import os
import signal
import sys
import random
import subprocess

#########################
#gets file names from specified dir
#x = os.listdir("\\AWESOMEPCV2\Users\Public\AWESOME DOPE MOVIE FOLDER")
#x =  os.getcwd()
#print x


def getFileStuff():
    x = os.getcwd()
    y = x + "/star trek/ranMovie.txt"
    try:
        f = open(y, 'r')          ####a###########create text file, change path. 
        currentAccounts = f.read().splitlines()
        f.close()
        return currentAccounts

    except:
        fileErrorMessage = ''.join(['[',str(currentTime()),']',' Unable to open currentAccounts.txt, terminating program...' ])
        print (fileErrorMessage)

        sys.exit()    


def makeSickDataforWriteFileStuff(showTitle, showEpisodes):
    data = {}
    swag=['blah', 'notblah']
    data[showTitle] = showEpisodes
    data["key"] = "value"
   # data[showTitle] = "fuckSpok.bl"
       
    print data



name = "star trek"
shows = ["spoklove.avi", "cobainletu-s.jpg"]
makeSickDataforWriteFileStuff(name, shows)
def writeFileStuff():
    x = os.getcwd()
    y = x + "/star trek/ranMovie.txt"
    print y
    try:
        f = open(y, 'w')
        for x in range(0, 10):
            string = str("blah" + str(x))
            newLine = ''.join([string,'\n'])
            f.write(newLine)
          #  

    except:
        print('some file shit broke')
        sys.exit()
    f.close()

    
#print os.path.abspath(os.curdir)
#os.chdir(os.curdir + "/Star Trek/")
#print os.path.abspath(os.curdir)


#play an single file, hardcoded currently
def playFile(filePath):
#   p = subprocess.Popen([filePath])
    p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","C:\\\Users\Alex\Desktop\Anchorman2.mp4"])

def showAvailable(showName):
    showAvailable = False
    tvShowNamesFolder = (os.listdir(os.getcwd()))

    for showTitleFolder in tvShowNamesFolder:
        if showTitleFolder.lower() == showName.lower():
            showAvailable = True

    return showAvailable

def main():
    tv = TvShow()
    
    tv.getUserInput()
    
    

    handleUserInput(showNameInput)


    tvShowNamesFolder = (os.listdir(os.getcwd()))

    for showTitleFolder in tvShowNamesFolder:
        if showTitleFolder.lower() == showNameInput.lower():
                print (showTitleFolder.lower()+ " is an available show!")

                #os.chdir(os.curdir + "/" + myInput)
                
                pathTousersShowInputFolder = os.path.abspath(os.curdir)
                print pathTousersShowInputFolder
                writeFileStuff()
                usersShowInputFolder = (os.listdir(pathTousersShowInputFolder))

    #walking scrip area######
                for root, dirs, files in os.walk(pathTousersShowInputFolder):
                    for name in dirs:
                        try:
                            pathToSeason = (pathTousersShowInputFolder+ "/" +name)
                          #  print pathToSeason
                            x = os.listdir(pathToSeason)
                            for y in x:
                                if y != "Thumbs.db":
                                    fullPath = (pathToSeason + "/" + y)
                                   # print y
                                    #print fullPath
                                
                            #os.rmdir(os.path.join(root, name))
                        except WindowsError:
                            print 'Skipping', os.path.join(root, name)

#doStuff()


#main()
#better name for this? it will end up being the main class holding
#data for dirs, tv names, user args and such
class TvShows:
    def __init__(self):
        self.userInput = ""
        self.showTitle = ""
        self.userArgument = ""
        self.showDirectory = ""
    
    def randomizeShowOrder(self):
        print self.showTitle

    def setShowDirectory(self):
        print self.showDirectory

    def handleUserArguents(self):
        print self.userArgument
        #"switch" here?

    def __setUserArgument(self):
        dashIndex = self.userInput.index("-")
        userArg = self.userInput[dashIndex:]
        self.userArgument = userArg

    def __setShowTitle(self):
        if "-" in self.userInput:
            dashIndex = self.userInput.index("-")
            if (self.userInput[dashIndex - 1]) == " ":
                self.showTitle = self.userInput[0:dashIndex - 1]
            else:
                self.showTitle = self.userInput[0:dashIndex]
        else:
            self.showTitle = self.userInput

    def __handleUserInput(self):
        if "-" in self.userInput:
            self.__setUserArgument()
        self.__setShowTitle()
      

    def getUserInput(self):
        self.userInput = raw_input("Enter movie title: ")
        self.__handleUserInput()

#x = TvShows("test", "-randomize")

tv = TvShows()
tv.getUserInput()











    
