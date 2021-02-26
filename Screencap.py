import cv2
import random

def main():
    # Start by randomly selecting starting state
    haruhi_parts = [1,2,3,4]
    weights = [4/62,27/62,26/62,5/62]
    shot_part = random.choices(haruhi_parts,weights)[0]
    for i in range(10):
        # Randomly select a frame included in the current state, and then determines the next state
        if (shot_part == 1):
            frame = random.randint(0,25800)
            shot_part = next_shot(1)
        elif (shot_part == 2):
            frame = random.randint(25801,100700)
            shot_part = next_shot(2)
        elif (shot_part == 3):
            frame = random.randint(100701,196280)
            shot_part = next_shot(3)
        else:
            frame = random.randint(196281,232752)
            shot_part = next_shot(4)
        vid_capture(frame,i)

# This function uses a Markov Chain probability to determine which part of the film to take the
# next shot from. 
def next_shot(shot_part):
    haruhi_parts = [1,2,3,4]
    if (shot_part == 1):
        weights = [0,0.75,0.25,0]
    elif (shot_part == 2):
        weights = [3/26,14/26,8/26,1/26]
    elif (shot_part == 3):
        weights = [1/25,7/25,13/25,4/25]
    else:
        weights = [0,0.4,0.6,0]
    return random.choices(haruhi_parts,weights)[0]

# Captures the specified frame and saves it as an image in the appropriate location
def vid_capture(frame, count):
    cap = cv2.VideoCapture('Suzumiya Haruhi no Shoushitsu (not burned).m4v')
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
    total_frames = cap.get(7)

    cap.set(1, frame)
    ret, frame = cap.read()
    cv2.imwrite("assets/H{num}.png".format(num = count), frame)

main()
