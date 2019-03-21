import pygame

# import random

file = "/Users/md/learn_code/stopdanse/4.mp3"
# BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
# FREQ, SIZE, CHAN = getmixerargs()
# pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER
# random.seed(1)
# set = 0
# hi = random.randint(100, 100000)
num = 0
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
# pygame.mixer.music.load()
# for x in range(0, 1000000):
# 	print("hi")
pygame.mixer.music.play()
# for x in range(0, 1000000):
# 	print("hi")
# while pygame.mixer.music.get_busy():
# 	continue
while pygame.mixer.music.get_busy():
	pygame.time.Clock().tick(10)
	num += 1
	if num %150 == 50:
		pygame.mixer.music.pause()
	if num % 150 == 80:
		pygame.mixer.music.unpause()


	# 	set =1


	# pygame.mixer.music.stop()
# print("hi")
