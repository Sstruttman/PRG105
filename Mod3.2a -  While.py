# This program is meant to repeat the song 99 bottles of beer on the wall
beer = 99
while beer != 0:
    print(f'{beer} bottles of beer on the wall')
    print(f'{beer} bottles of beer')
    print(f'Take one down pass it around')
    beer = beer - 1
    print(f'{beer} bottles of beer on the wall!')

    if beer == 2:
        print(f'{beer} bottles of beer on the wall')
        print(f'{beer} bottles of beer')
        print(f'Take one down pass it around')
        beer = beer - 1
        print(f'{beer} bottle of beer on the wall!')

    if beer == 1:
        print(f'{beer} bottle of beer on the wall')
        print(f'{beer} bottle of beer')
        print(f'Take it down pass it around')
        exit(f'No more bottles of beer on the wall!')
