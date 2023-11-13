import instMem as intr
import decoder as dec

pc=0
while True:
    print(intr.insts[pc/4])
    pc+=4
    if((pc>>2)>=len(intr.insts)):
        break


