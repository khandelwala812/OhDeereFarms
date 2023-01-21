generation[100][100]= [[]]
def generate():
    for i in generation:
        for j in generation:
            randVal = random.randint(0, 8)
            generation[i][j] = randVal

