xle = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
def focus(xle):
    for i in xle:
        print(i)

def globe(xle):
    for i in xle:
        for j in range(len(i)):
            xle[j] = 9

globe(xle)
focus(xle)






