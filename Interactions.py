from Tile import *

# function that returns new instance of a class
def tileIDs(num):
    
    IDs = {
        1: Grass(),
        2: Tree(),
        3: Border(),
        4: Stone(),
        5: Dirt(),
        6: Hole(),
        7: ShallowWater(),
        8: DeepWater(),
        9: Sand(),
        10: Clay(),
        11: Wood(),
        12: WoodSpade(),
        13: WoodPick(),
        14: WoodAxe(),
        15: StoneSpade(),
        16: StonePick(),
        17: StoneAxe()
    }
    
    return IDs[num]
    

# First Tuple:
# (tile to break, held item)
# Second Tuple:
# (replace with, receive, damage)

breaks = {
    
    # Grass turns into a hole, receive dirt. DEFAULT INTERACTION
    (1, 0): (6, 5, (0, 5)),
    (1, 12): (6, 1, (5, 10)), # With wood shovel
    (1, 15): (6, 1, (10, 15)), # With stone shovel
    
    # Tree turns to grass, receive tree. DEFAULT INTERACTION
    (2, 0): (1, 2, (5, 10)),
    (2, 14): (1, 2, (10, 15)), # With wood axe
    (2, 17): (1, 2, (15, 20)), # With stone axe
    
    # Stone turns to dirt, receive stone. DEFAULT INTERACTION
    (4, 0): (5, None, (0, 1)),
    (4, 13): (5, 4, (10, 20)), # With wood pick
    (4, 16): (5, 4, (20, 30)), # With stone pick
    
    # Dirt turns into a hole, receive dirt. DEFAULT INTERACTION
    (5, 0): (6, 5, (0, 5)),
    (5, 12): (6, 5, (5, 10)), # With wood shovel
    (5, 15): (6, 5, (10, 15)), # With stone shovel
    
    # Sand turns to dirt, receive sand. DEFAULT INTERACTION
    (9, 0): (5, 9, (0, 5)),
    (9, 12): (5, 9, (5, 10)), # With wood shovel
    (9, 15): (5, 9, (10, 15)),
    
    # Clay turns to dirt, receive clay. DEFAULT INTERACTION
    (10, 0): (5, 10, (0, 5)),
    (10, 12): (5, 10, (5, 10)), # With wood shovel
    (10, 15): (5, 10, (10, 15)), # With stone shovel
    
    # Break underneath shallow water for clay, only works with shovel. Turns into deep water. # DEFAULT INTERACTION
    (7, 0): (8, None, (0, 1)),
    (7, 12): (8, 10, (2, 5)), # With wood shovel
    (7, 15): (8, 10, (5, 10)), # With stone shovel
    
    # Break placed wood for wood, only works with axe. Turns into dirt. # DEFAULT INTERACTION
    (11, 0): (5, None, (1, 2)),
    (11, 14): (5, 11, (25, 35)),
    
}


# First Tuple:
# (held item, tile to place on)
# Value:
# replace with
places = {
    
    # PLACING DIRT/GRASS
    # Place grass in a hole
    (1, 6): 1,
    
    # Place dirt in a hole
    (5, 6): 5,
    
    
    # PLACING TREES
    # Place a tree on dirt
    (2, 5): 2,
    
    # Place a tree on grass
    (2, 1): 2,
    
    
    # PLACING STONE
    # Place stone on grass
    (4, 1): 4,
    
    # Place stone on dirt
    (4, 5): 4,
    
    
    # PLACING SAND
    # Place sand on dirt
    (9, 5): 9,
    
    # Place sand on grass
    (9, 1): 9,
    
    
    # PLACING CLAY
    # Place clay on grass
    (10, 1): 10,
    
    # Place clay on dirt
    (10, 5): 10,
    
    # Place clay in deep water
    (10, 8): 7,
    
    
    # PLACING WOOD
    # Place wood on grass
    (11, 1): 11,
    
    # Place wood on dirt
    (11, 5): 11
    
}

