print('\n\n\n')
tiles = 1456
row = 53 # 3 tiles per row

total_row = tiles // row
remain_tiles = tiles % row

print(total_row, remain_tiles)

buy_more = row - remain_tiles

print(f'Total tiles: {tiles} pcs.')
print(f'Tiles per row: {row} pcs.')
print(f'-------Calculation--------')
print('10 tiles can make {} row'.format(total_row))
print('Remaining tile {} pcs.'.format(remain_tiles))
print('additional tile have to buy more {} pcs.'.format(buy_more))


# How many additional tiles do you have to buy?


print('\n\n\n')
print('Program tile calculation by Ama')

tilecolor ={'red':100, 'gold':200, 'white':90}
try:
    tiles = int(input('How many tiles do you want to use: '))
    row = int(input('How many tiles per row: ')) # xx tiles per row
    print(tilecolor)
    color = input('What color of tile do you select: ')
except:
    print('\nPlese fill information in number format!')
    tiles = int(input('How many tiles do you want to use: '))
    row = int(input('How many tiles per row: ')) # xx tiles per row
    print('\nPlease type color same the name in catalog!')
    print(tilecolor)
    color = input('What color of tile do you select: ')  
    
total_row = tiles // row
remain_tiles = tiles % row

#print(total_row, remain_tiles)

if remain_tiles == 0:
    buy_more = 0
else:
    buy_more = row - remain_tiles
total_tiles = tiles + buy_more


print(f'Total tiles: {tiles} pcs.')
print(f'Tiles per row: {row} pcs.')
print(f'-------Calculation--------')
print('10 tiles can make {} row'.format(total_row))
print('Remaining tile {} pcs.'.format(remain_tiles))
print('additional tile have to buy more {} pcs.'.format(buy_more))
print('Selected tile color: {}'.format(color))
print('Price of selected tile: {} THB/pcs.'.format(tilecolor[color]))
print('Total price for additional tiles: {} THB'.format(buy_more * tilecolor[color]))
print('Total price for all tiles: {} THB'.format(total_tiles * tilecolor[color]))

# How many additional tiles do you have to buy?
