#returns heat map based on input of f for fertilizer, t for tillage, s for same crop
def heatmap(levelType):
    heatmap = [[],[]]
    #gives weights for color
    for i in tiles:
        for j in tiles[i]:
            tileSum = 0
            for k in range(5):
                for l in range(5):
                    if levelType == "f":
                        tileSum += tiles[k][l].fertilizer
                    elif levelType == "t":
                        tileSum += tiles[k][l].tillage
                    elif levelType == "s":
                        tileSum += tiles[k][l].sameCrop
            heatmap[i/5][j/5] = tileSum/25
            j += 5
            i += 5
    return heatmap