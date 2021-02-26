# The Haruhi Stack

### Liam Juskevice
### Computational Creativity Spring 2021
This code is very simple to use, but I do not have the main source for it saved on github. This code uses a video file containing the entirety of *The Disappearance of Haruhi Suzumiya*. If you have that file and the filename matches in **Screencap.py** you need only run markov.py on the command line and the program works by itself. Feel free to test it out with a different video file instead, but you'll have to tweak the frame numbers and such in **Screencap.py** to make it work. Also the Markov chain I used would no longer be meaningful for any different video. 

The Markov Chain used in this program is based on how I edited my audiovisual essay on the movie, which you can view [here](https://bowdoin-my.sharepoint.com/:v:/g/personal/ljuskevi_bowdoin_edu/EXv5CIlmelBFqbFmBf4xvdwBlQqGVFu4F_5vbeMTxCl8_w?e=44zStA).

Essentially, I divided the story's narrative into four different parts, and analyzed which parts of the movies I took clips from. I looked at every clip from the movie I used in my AV essay (ignoring clips from media besides the movie) and determined which part of the movie they came from and the sequence of which I used them for the AV Essay. I then used that sequence to model a Markov Chain to then randomly select 10 frames from the movie. These 10 frames are then stacked together, creating the rather strange final results you can see in the example folder. 

For the record I divided the parts of the movie as follows:
**Pre-Disappearance:** Frames 0-25800  
**The Disappearance:** Frames 25801-100700  
**Finding Haruhi and the Climax:** 100701-196280  
**After Story:** 196281-232752  


