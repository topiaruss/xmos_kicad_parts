"""XMOS XS1-128 TQFP 0.4mm pitch footprint maker
Russ Ferriday
russf@topia.com
April 2011
"""
head="""PCBNEW-LibModule-V1  Wed 13 Apr 2011 08:50:05 PM PDT
$INDEX
XMOS-TQFP-128-4.8mm-Pad
$EndINDEX
$MODULE XMOS-TQFP-128-4.8mm-Pad
Po 0 0 0 15 4DA66EBB 00000000 ~~
Li XMOS-TQFP-128-4.8mm-Pad
Cd THIN QUAD FLAT PACK
Kw THIN QUAD FLAT PACK
Sc 00000000
AR
Op 0 0 0
T0 -1791 -5364 600 600 0 120 N V 21 N">NAME"
T1 -1388 -4085 600 600 0 120 N V 21 N">VALUE"
DC 1772 -1772 1969 -1772 150 21
DS -2362 -2362 1969 -2362 150 21
DS 1969 -2362 2362 -1969 150 21
DS 2362 -1969 2362 2362 150 21
DS 2362 2362 -2362 2362 150 21
DS -2362 2362 -2362 -2362 150 21
"""
pchunk="""Dr 0 0 0
At SMD N 00888000
Ne 0 ""
"""
tail="""$EndMODULE  XMOS-TQFP-128-4.8mm-Pad
$EndLIBRARY
"""

f = open('m.mod', 'w')
f.write(head)

def convImp(mm):
    return int(round(mm * 1000.0 *10 / 25.4))

def putpad(name, x, y, xpos, ypos, shape='O'):
    #import pdb; pdb.set_trace()
    x = convImp(x)
    y = convImp(y)
    xpos = convImp(xpos)
    ypos = convImp(ypos)
    f.write('$PAD\n')
    f.write('Sh "%s" %s %s %s 0 0 0\n' % (name, shape, x, y))
    f.write(pchunk)
    f.write('Po %s %s\n' % (xpos, ypos))
    f.write('$EndPAD\n')

startx = 0.2 + 15 * 0.4 
ypos = -7.7
x,y = 0.2, 1.45
for p in range(32):
    xpos = startx - (p * 0.4)
    putpad(p+1, x, y, xpos,ypos) 

starty = -(0.2 + 15 * 0.4)
xpos = -7.7
x,y = 1.45, 0.2
for p in range(32,64):
    ypos = starty + ((p-32) * 0.4)
    putpad(p+1, x, y, xpos,ypos) 

startx = -(0.2 + 15 * 0.4)
ypos = 7.7
x,y = 0.2, 1.45
for p in range(64,96):
    xpos = startx + ((p-64) * 0.4)
    putpad(p+1, x, y, xpos,ypos) 

starty = (0.2 + 15 * 0.4)
xpos = 7.7
x,y = 1.45, 0.2
for p in range(96,128):
    ypos = starty - ((p-96) * 0.4)
    putpad(p+1, x, y, xpos,ypos) 

putpad(129, 4.8, 4.8, 0, 0, 'R') 
f.write(tail);
f.close()
