heatmap = [[],[]]
#gives weights for color
for i in tiles:
    for j in tiles[i]:
        tileSum = 0
        for k in range(5):
            for l in range(5):
                tileSum += tiles[k][l].fertilizer
        heatmap[i/5][j/5] = tileSum/25
        j += 5
        i += 5