# The Haruhi Stack

### Liam Juskevice
### Computational Creativity Spring 2021
This code is very simple to use, but I do not have the main source for it saved on github. This code uses a video file containing the entirety of *The Disappearance of Haruhi Suzumiya*. If you have that file and the filename matches in **Screencap.py** you need only run markov.py on the command line and the program works by itself. Alternatively, if you don't have the movie file on hand you can just run **make_image.py** by itself to see how it works with the set of screenshots I have uploaded. Feel free to test it out with a different video file instead, but you'll have to tweak the frame numbers in **Screencap.py** to make it work. Also the Markov chain I used would no longer be meaningful for any different video. 

The Markov Chain used in this program is based on how I edited my audiovisual essay on the movie, which you can view [here](https://bowdoin-my.sharepoint.com/:v:/g/personal/ljuskevi_bowdoin_edu/EXv5CIlmelBFqbFmBf4xvdwBlQqGVFu4F_5vbeMTxCl8_w?e=44zStA).

Essentially, I divided the story's narrative into four different parts, and analyzed which parts of the movies I took clips from. I looked at every clip from the movie I used in my AV essay (ignoring clips from media besides the movie) and determined which part of the movie they came from and the sequence of which I used them for the AV Essay. I then used that sequence to model a Markov Chain to then randomly select 10 frames from the movie. These 10 frames are then stacked together, creating the rather strange final results you can see in the example folder. 

For the record I divided the parts of the movie as follows:  
**Pre-Disappearance:** Frames 0-25800  
**The Disappearance:** Frames 25801-100700  
**Finding Haruhi and the Climax:** Frames 100701-196280  
**After Story:** Frames 196281-232752  

And the Markov Chain probabilities are as follows:  

|        | Part 1 | Part 2 | Part 3 | Part 4 |
|--------|--------|--------|--------|--------|
| Part 1 | 0      | 3/4    | 1/4    | 0      |
| Part 2 | 3/26   | 14/26  | 8/26   | 1/26   |
| Part 3 | 1/25   | 7/25   | 13/25  | 4/25   |
| Part 4 | 0      | 2/5    | 3/5    | 0      |


This project works with an idea I played around with in a previous art class and applies the Markov Chain principle to it. For the art class I selected a handful of anime I'm particularly fond of, and set up a program to randomly select an episode from the show and timestamp to take a screenshot of. Unlike this program the screenshots and editing were done entirely manually. Also this program selects screenshots using a Markov Chain whereas the old one was pretty much entirely random. With this set up I have the opportunity to make more of these strange images using a movie I love and have spent plenty of time thinking about. Furthermore, with the Markov Chain reflecting my pattern of behavior in editing the AV essay, which gives the pattern an additional level of intrigue. Had I managed my time better I would have found a way to integrate the clips from other media into the Markov Chain and final image as well. Oh well. 


I have not used Python in a while, so I was not confident I could easily implement my idea into action. Fortunately the essentials came back to me relatively quickly. This project also involved working with two libraries I had absolutely no experience with beforehand. I simply put faith in my ability to figure these libraries out (with plenty of help from google) and jumped in. Fortunately for me, these libraries are quite intuitive to use, at least for the purposes I needed them for. This program was way more sophisticated than what I used for that art class, so pretty much every aspect of this program was at least somewhat new to me. Was it exceptionally difficult to figure out? Not really. But I've managed to impress myself with how quickly I could grasp all this to create something like this. If I were to build on this system I would find a way to work clips from different media into the final work as well. Beyond that, now that I have some basic knowledge of pillow and OpenCV I'm sure they could easily come to use in my later endeavors for this course. 


That being said, I am not sure I would consider this system creative in the traditional sense. It generates unique images using randomness that humans would have difficulty emulating. Is probabilistic image manipulation qualify as creativity? It certainly creates something distinctive, but I'm not sure if it truly fits the bill.

Credit goes to everyone involved in the making of *The Disappearance of Haruhi Suzumiya* for creating the imagery this system utilizes. Outside of that I needed to plenty of research into pillow and OpenCV, and the following sources were helpful to that end:  
https://pillow.readthedocs.io/en/stable/  
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html  