import time
import os
import signal
import sys
import random


#########################
#gets file names from specified dir
#x = os.listdir("\\AWESOMEPCV2\Users\Public\AWESOME DOPE MOVIE FOLDER")
#x =  os.getcwd()
#print x
def doStuff():
    myInput = raw_input("pleaseEnterShit ")

    tvShowNamesFolder = (os.listdir(os.getcwd()))

    for showTitleFolder in tvShowNamesFolder:
        if showTitleFolder.lower() == myInput.lower():
                print (showTitleFolder.lower()+ " is an available show!")

                os.chdir(os.curdir + "/" + myInput)
                
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
################

            
     #       for firstDirDown in usersShowInputFolder:
     #           print firstDirDown
   # else:
       # print ("sorry, that is not an available show.")



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
        
#doStuff()
writeFileStuff()
#myArr=[0,1,2,3]
#random.shuffle(myArr)
#print myArr
#arr = getFileStuff()
#print arr
##random.shuffle(arr)
#print arr
    
#print os.path.abspath(os.curdir)
#os.chdir(os.curdir + "/Star Trek/")
#print os.path.abspath(os.curdir)
        
#works for opening a single file..NOT playlist yet..should be able to do this
#p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","C:\\\Users\Alex\Desktop\Anchorman2.mp4"])
#time.sleep(10)
#p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","C:\\\Users\Alex\Desktop\Anchorman2.mp4"])
#time.sleep(10)
#p.kill()
