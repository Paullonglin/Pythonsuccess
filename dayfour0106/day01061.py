jias=['a','b','c']
yis=['x','y','z']
for jia in range(3):
    for yi in range(3):
        if jia==0 and yi==0:
            continue
        elif jia==2 and yi==0:
            continue
        elif jia==2 and yi==2:
            continue
        else:
            print(jias[jia],yis[yi])