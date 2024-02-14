# programa que faz um som quando interagido
from pygame import mixer, event

mixer.init()
mixer.music.load('./mp3/ica.mp3')
mixer.music.play()
input('Digite algo para parar...')
event.wait()