#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import sys

def seasonsCombination():
    seaNums = list(range(1,5))
    seaNames = ['s', 'S', 's0', 'S0', 'season', 'season0', 'Season', 'Season0', 's ', 'S ', 's 0', 'S 0', 'season ', 'season 0', 'Season ', 'Season 0']

    seasonsCombined = []
    for seaName in seaNames:
        for seaNum in seaNums:
            seasonsCombined.append(seaName+str(seaNum))
    return seasonsCombined

def getSeasonNumber(showFolder, seasonsCombined):
    for s in seasonsCombined:
        search = showFolder.find(s)
        if search != (-1):
            seaNumber = s.split()[-1].strip()
            sName = "Season "+seaNumber.zfill(2)
            if "s" in seaNumber or "S" in seaNumber:
                seaNumber = seaNumber[-1]
                sName = "Season "+seaNumber.zfill(2)
            break

    if search == -1:
        seaNumber = "01"
        sName = "Season 01"
        s = ""
        
    showFolderFin = showFolder.replace(s, "").strip()
    # Pad with a 0 for seaNumber
    return [sName, str(seaNumber).zfill(2), showFolderFin]

# MAIN CODE - integrate other pieces or use function (def)
if __name__ == '__main__':
    RootDir = sys.argv[1]
    SeasonsCombine = seasonsCombination()
    ShowFolderPath_ORG = []
    ShowFolderPath_NEW = []
    for folder in os.listdir(RootDir):
        print(folder)
        # We want the show directory and need to parse it if contains a season
        getSeasonNumber(folder,SeasonsCombine)
        seasonName, seasonNumber, showName = getSeasonNumber(folder, SeasonsCombine)
        print("sName: " + seasonName + "\tsNum: " + seasonNumber + "\tShow: " + showName)
        
        # Make Season # Directory - check if does not exist and if empty
        show = os.path.join(RootDir,folder)
        # We can later rename our shows with Season Suffix
        ShowFolderPath_ORG.append(show)
        ShowFolderPath_NEW.append(os.path.join(RootDir,showName))
        os.rename(show, os.path.join(RootDir,showName))
        show = os.path.join(RootDir,showName)
        showSeason = os.path.join(show,seasonName)
        if not os.path.isdir(showSeason):
            os.mkdir(showSeason)
            
        if not os.listdir(showSeason):
            # Empty -  move episodes
            os.chdir(show)
            increm = 1
            epiNum = 1
            for file in os.listdir():
                # Plex Naming Format ShowName - sxxexx
                # Commented out the increment was to skip trying to move the season folder, but the if file_ext handles that...
                # if increm == 1:
                    # increm = increm+1
                    # continue
                filename, file_ext = os.path.splitext(file)
                if file_ext is not "":
                    epiNumStr = str(epiNum).zfill(2)
                    shutil.move(os.path.join(show,file), os.path.join(showSeason, showName + " - " + "s"+seasonNumber+"e"+epiNumStr+file_ext))
                    epiNum = epiNum+1
                increm = increm+1
        
        else:
            print(showName + " " + seasonName + " The season folder was non-empty, no files were moved and renamed")