print "This script assumes all tiles in your tileset block are the same height, will be centered horizontally, offset up by half a tile, and the tile block is left justified."
tile = int(raw_input("Starting tile number: "))
gridx = 32
gridy = 32
tilex = 32
tiley = int(raw_input("Height of a tile in this tileset block: "))
imagex = int(raw_input("Width of the tile block: "))
y = int(raw_input("Top edge of the tile block: "))
imagey = int(raw_input("Bottom edge of the tile block: "))
tilesetname = raw_input("Tileset: ")
filepath = "../mods/core/tilesetdefs/" + tilesetname
x=0
tileline=""
imagex = imagex - (imagex % gridx)
while y < imagey:
    while x < imagex:
        tileline = "".join(("tile=",str(tile),",",str(x),",",str(y),",",str(tilex),",",str(tiley),",",str(tilex-(gridx/2)),",",str(tiley-(gridy/2)),"\n"))
        with open(filepath, "a") as tileset:
            tileset.write(tileline)
        x += tilex
        tile +=1
    y += tiley
    x = 0
