import simpleaudio as sa
import time

#Define Bpm
print("Insert bpm")
bpm = int(input())
bpmsec = 60 / bpm
print("Bpm is ", bpmsec, "sec")

#Make list array
#Defineer list van 4 noot lengtes
print("Insert 4 notelenghts")
list1 = []
for maatnoot in range(0, 4):
    maatnoot = float(input())
    list1.append(maatnoot)
#Kies welke getal in de lijst
#print(list1[0])

#Defineer aantal van afspelen
print("Insert times to repeat sample")
aantalplays = int(input())
print("Sample will be repeated", aantalplays, "times")


amountofplays = int(input())
amountofplays = aantalplays

for x in range(0, amountofplays):
    for x in range(0, aantalplays):
        wave_obj = sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/hihat2.wav")
        play_obj = wave_obj.play()
 #   play_obj.wait_done()
        time.sleep(bpmsec*list1[x])
        print(x)
