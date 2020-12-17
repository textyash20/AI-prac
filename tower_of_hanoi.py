def moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print("Moving disk from",fp,"to",tp)
n=int(input("Enter the no. of disks :\t"))
moveTower(5,"A","B","C")