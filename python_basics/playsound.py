import simpleaudio as sa
'''values = [1, 2, 3, 4, 5]
numValues = len(values)

print len (values)


for value in values: '''
wave_obj = sa.WaveObject.from_wave_file("/home/sander/documentos/Samples/hihat2.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
