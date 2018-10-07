import simpleaudio as sa
import time
import random

"""
An example project in which a rhythmical sequence (one measure, 1 sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4
Instead of using steps to iterate through a sequence, we are checking the time.
We will trigger events based on a timestamp.
------ HANDS-ON TIPS ------
- Run the code, read the code and answer the following question:
  - This script transforms a list of 'sixteenth notes timestamps' into a list of
    regular timestamps.
    In the playback loop, the time difference (currentTime minus startTime)
    is compared to the upcomming timestamp.
    Why is this a more accurate method then the methods used in the examples
    "04_randomNoteDuration.py" and "05_oneSampleSequenceSteps.py"?
    Notate your answer below this line (Dutch is allowed)!

Its better to use the time difference because its a more steady and reliable way of triggering
events at a certain time, the program analyses time that had passed and wil trigger or ignore
events on basis of time calculations. In the past examples that we worked with time.sleep we could
get into the issues of loading the cpu to a point where timing is not accurate anymore
because of the division in calculations.


- Alter the code:
  Currently one sample is played. Add another sample to the script.
  When a sample needs to be played, choose one of the two samples
  randomly.
  (See the hint about the random package in script "02_timedPlayback".)
- Alter the code:
  Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The timestamps list is emptied using the pop() function.
  (multiple possible solutions)
"""

# load 1 audioFile and store it into a list
# note: using a list taking the next step into account: using multiple samples
samples = [ sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/hihat1.wav"),
            sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/kick1.wav"),
            sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/clap1.wav")]



# set bpm
print("Fill in the bpm and press Enter")
bpm = int(input())
# calculate the duration of a quarter note
quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

#Define random sample seleccion for looping
"""    samplepick = []
        for i in range(4):
            samplepick.append(random.randint(0,2))
            samplepick = samplepick.pop(0)
            print("list van samplepick:", samplepick)

"""

#Let the user pick rhythm
print("Insert 4 notelenghts and press enter after eachone")
listusertimestamps = []
for i in range(0, 4):
    i = int(input())
    listusertimestamps.append(i)

print(listusertimestamps)
    #return(listusertimestamps)


notelenght = []
timestamps16th = []

def durationToTimestamps16th(notelenght):
    y = 0
    for note in notelenght:
        x = note * 4
        timestamps16th.append(x + y)
        y = timestamps16th[0]

#how many times is the sequence going to loop
print("Insert times to repeat sample")
aantalplays = int(input())
print("Sequence will be repeated", aantalplays, "times")


for i in range(0, aantalplays):
    timestamps = []
    timestamps16th = [0, 2, 4, 6, 8, 10, 12]



    durationToTimestamps16th(notelenght)





    for timestamp in timestamps16th:
      timestamps.append(timestamp * sixteenthNoteDuration)


    # NOTE: pop(0) returns and removes the element at index 0
    if len(timestamps) > 0:
        timestamp = timestamps.pop(0)
    # retrieve the startime: current time
    startTime = time.time()

    keepPlaying = True
    # play the sequence


    while keepPlaying:
      # retrieve current time
      currentTime = time.time()
      # check if the timestamp's time is passed
      if(currentTime - startTime >= timestamp):
        # play sample
        samples[random.randint(0,2)].play()


        # if there are timestamps left in the timestamps list
        if timestamps:
          # retrieve the next timestamp
          timestamp = timestamps.pop(0)
        else:
          # list is empty, stop loop
          keepPlaying = False
      else:
        # wait for a very short moment
        time.sleep(0.01)
