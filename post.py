import re

with open("pre.gcode",'r') as f:
    lines = f.readlines()

def setAccel(x):
    return "SET_VELOCITY_LIMIT ACCEL=%i ACCEL_TO_DECEL=%i SQUARE_CORNER_VELOCITY=5" % (x,x)

primePillarAcc = 3000
loopAcc = 2000
stackedSparseInfillAcc = 3000
destringWipeJumpAcc = 3000
perimeterAcc = 2000
crownAcc = 3000
solidAcc = 3000
sparseInfillAcc = 3000

for l in lines:
    m= re.findall("(?smi)(.*?) Path\'",l)
    
    a = []
    
    if m != []:
        assert(len(m) == 1)
        path = m[0][3:]
        
        if path == 'Prime Pillar':
            a.append(setAccel(primePillarAcc))
            pass
        elif path == 'Loop':
            a.append(setAccel(loopAcc))
            pass
        elif path == 'Stacked Sparse Infill':
            a.append(setAccel(stackedSparseInfillAcc))
            pass
        elif path == 'Destring/Wipe/Jump':
            a.append(setAccel(destringWipeJumpAcc))
            pass
        elif path == 'Perimeter':
            a.append(setAccel(perimeterAcc))
            pass
        elif path == 'Crown':
            a.append(setAccel(crownAcc))
            pass
        elif path == 'Solid':
            a.append(setAccel(solidAcc))
            pass
        elif path == 'Sparse Infill':
            a.append(setAccel(sparseInfillAcc))
            pass
        else:
            print(path)
            break
            
    print(l.rstrip())
    if len(a) > 0:
        print("\n".join(a))
