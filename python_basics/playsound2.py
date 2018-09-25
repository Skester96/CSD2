#Alleen 16bit files

import simpleaudio as sa
import time

#ImportFiles
wave_obj = sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/hihat2.wav")

#Define Bpm
print("Welcome to the sandersampler")
print("Insert bpm and 1 file will be played")
bpm = int(input())
bpmsec = 60 / bpm
print("Bpm is ", bpmsec, "sec")

#Make list array / Defineer list van 4 noot lengtes
print("Insert 4 notelenghts and press enter after eachone")
list1 = []
for maatnoot in range(0, 4):
    maatnoot = float(input())
    list1.append(maatnoot)

#print(len(list1))

#Defineer aantal van afspelen
print("Insert times to repeat sample")
aantalplays = int(input())
print("Sample will be repeated", aantalplays, "times")

#amountofplays = aantalplays

#Loop play and read func as many times as user chooses to be played (> 4)
for i in range(0, aantalplays):
    #play and read sample x times
    for x in range(0, 4):
        play_obj = wave_obj.play()
        #   play_obj.wait_done()
        time.sleep(bpmsec*list1[x])
