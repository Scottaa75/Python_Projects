import time

beer = 99
while beer > 0:
    print(f'{beer} bottles of beer on the wall, {beer}, bottles of beer!!, Take one down, pass it around, ...')
    beer -= 1
    time.sleep(2)
    print(f'{beer} bottles of beer on the wall')
    time.sleep(5)