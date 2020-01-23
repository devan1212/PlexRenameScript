# Plex Rename Show and Episodes
This python script is pretty simple, and it's major purpose is to rename episodes and move them into appropriate Season folders within a show.

## Who this is for?
This script is not for power users of Plex, it is not 100% automated and some manual work needs to be done, I will go into depth of the scope of this simple script. 

## Usage, Limitations, and Notes
### How it works?
The main idea behind this was to rename episodes and shows when they have been downloaded so that they would be Plex friendly.

Orginally Folder Structure Could look something like this (Nonsense can be information that we really don't care about such as Torrent Creator, Encoding Level, etc) (XX stands for number)
```
ShowName_<nonsense>
  - EpisodeXX_<nonsense>
 ```
 
 Post Script Structure (A lot more Plex Friendly)
 ```
 ShowName sXX
  - Season XX
    - ShowName SXXEXX
```

### Manual Steps Needed
As stated before, this is not fully automated and there are some manual steps required that should be performed before running the script.

For each show in your main TV Show Directory, you need to remove "nonsense" and rename them in the following format:

```ShowName_SXX``` 

If you look at the code, SXX can be either SeasonXX, seasonXX, or sXX. This is the only manual change you have to do for the script to move and rename the episodes within the folder.

If there is only one season for the show, then you can leave out the SXX - the script will just assume that this is the first season of the show.

### Set Up
All that is needed to run this script is Python. If you are using Anaconda, you can just open up Anaconda Prompt and type the following:

```python <location of Python Script> <Main Directory of Shows>```

### Limitations & Notes
The biggest limitation is that some manual work is required. On the bright side, you won't have to rename each episode :)

If you have multiple seasons to a show I would recommend just have separate folders initially
```ShowName_S01``` and ```ShowName_S02``` after the script is run you can move the subfolders ```Season01``` and ```Season02``` into just ```ShowName``` folder

