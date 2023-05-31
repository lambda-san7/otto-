import pygame
import os
import sounddevice as sd
import numpy as np

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Otter")

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

running = True

class otter:
    default = pygame.transform.scale(pygame.image.load(f"{dir_path}/otter.png"),(480,270))
    quiet = pygame.transform.scale(pygame.image.load(f"{dir_path}/otter O.png"),(480,270))
    loud = pygame.transform.scale(pygame.image.load(f"{dir_path}/otter AEI.png"),(480,270))
    sprite = default

fs = 44100

def calculate_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm <= 20 and volume_norm > 1:
        print("mid")
        otter.sprite = otter.quiet
        return
    if volume_norm > 20:
        print("loud")
        otter.sprite = otter.loud
        return
    else:
        otter.sprite = otter.default
        
stream = sd.InputStream(callback=calculate_volume, channels=1, samplerate=fs)
stream.start()

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            stream.stop()
            stream.close()
    window.fill((50,50,50))
    window.blit(otter.sprite, (0,140))
    pygame.display.update()

pygame.quit