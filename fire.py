import board
import time
import neopixel
import random

num_pixels = 30
np = neopixel.NeoPixel(board.A2, num_pixels, brightness=1.0, auto_write=False)

def constrain(low, high, value):
    if value < low:
        return low
    if value > high:
        return high
    return value

def chase(color1, color2, loop = 20, count=3, delay=0.1):
    result = 0
    for outer in range(count*loop):
        np.fill(color1)
        for i in range(num_pixels):
            if i % count == result:
                np[i] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count


def flame(background, foreground):
    for j in range(20):

        intensity = random.random() * 0.5 + 0.5
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        '''
        for i in range(num_pixels):
            intensity = random.random() * 0.5 + 0.5
            i_background = [int(i * intensity) for i in background]
            np[i] = i_background
        '''
        for i in range(random.randint(2, int(num_pixels / 5))):
            intensity = random.random() * 0.5 + 0.5
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(0.06)

background = (255, 92, 0)
foreground = (255, 20, 0)
while True:

    #flame((255, 91, 0), (255, 20, 0))
    intensity = random.random() * 0.7 + 0.3
    i_background = [int(i * intensity) for i in background]
    np.fill(i_background)
    '''
    for i in range(num_pixels):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np[i] = i_background
    '''
    for i in range(random.randint(2, int(num_pixels / 5))):
        intensity = random.random() * 0.7 + 0.3
        i_foreground = [int(i * intensity) for i in foreground]
        np[random.randint(0, num_pixels-1)] = i_foreground
    np.show()
    time.sleep(0.06)
