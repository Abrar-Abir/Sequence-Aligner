scoreMatrix =  [[0, 1],\
                [0, -1, 1],\
                [0, -1, -1, 1],\
                [0, -1, -1, -1, 1]]
sq1 = "ACGGTTGC"
sq2 = "AGCGTC"

def scoreParams(scoreMatrix):
    match, misMatch, gap = 0, 0, 0
    
    for i in range(4):
        for j in range(i+1):
            if j == 0:
                gap += scoreMatrix[i][j]
            elif i + 1 == j:
                match += scoreMatrix[i][j]
            else:
                misMatch += scoreMatrix[i][j]
    
    return 0.1*(match/4)//0.1, 0.1*(misMatch/6)//0.1, 0.1*(gap/4)//0.1

def score(b1, b2):
    if int(b1) < int(b2):
        b1, b2 = b2, b1
    return scoreMatrix[int(b1)-1][int(b2)]

def select(branches):
    branches.sort(key=lambda  row: (row[2], row[3]))
    return branches[-1]

def getNode(sq1, sq2, al1, al2, sMax, sMin, match, misMatch):
    if sq1[0] == sq2[0]:
        brnch0 = (al1 + sq1[0], al2 + sq2[0],\
            sMax, sMin + score(sq1[0], sq2[0]) - misMatch)
    else:
        brnch0 = (al1 + sq1[0], al2 + sq2[0],\
            sMax + score(sq1[0], sq2[0]) - match, sMin)
    brnch1 = (al1 + '0', al2 + sq2[0],\
        sMax + 2*score(sq1[0], sq2[0]) - match,\
        sMin + 2*score(sq1[0], sq2[0]) - misMatch)
    brnch2 = (al1 + sq1[0], al2 + '0', sMax, sMin)
    return brnch0, brnch1, brnch2

def align(sq1, sq2):
    base = 'AGCT'
    match, misMatch, gap = scoreParams(scoreMatrix)
    print(match, misMatch, gap)
    if len(sq1) < len(sq2):
        sq1, sq2 = sq2, sq1

    for i in range(4):
        sq1 = sq1.replace(base[i], str(i + 1))
        sq2 = sq2.replace(base[i], str(i + 1))
    
    al1, al2 = '', ''
    sMax, sMin = 0, 0

    while sq1 != '' or sq2 != '':
        print(sq1, sq2, al1, al2, sMax, sMin)
        brnch0, brnch1, brnch2 = getNode(sq1, sq2, al1, al2, sMax, sMin, match, misMatch)
        brnch = select([brnch0, brnch1, brnch2])
        al1, al2, sMax, sMin = brnch[0], brnch[1], brnch[2], brnch[3]

        if al1[-1] != '0':
            sq1 = sq1[1:]
        if al2[-1] != '0':
            sq2 = sq2[1:]
    
        if sq1 == '' or sq2 == '':
            if sq1 == '':
                al1 += '0'*len(sq2)
                al2 += sq2
                sq2 = ''
            else:
                al2 += '0'*len(sq1)
                al1 += sq1
                sq1 = ''

    for i in range(4):
        al1 = al1.replace(str(i + 1), base[i])
        al1 = al1.replace('0', '_')
        al2 = al2.replace(str(i + 1), base[i])
        al2 = al2.replace('0', '_')
    return al1, al2

print(align(sq1, sq2))