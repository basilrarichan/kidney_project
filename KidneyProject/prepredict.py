def prepredict(data):
    cnt=0
    if((float(data[0])>=1.005) and (float(data[0])<=1.030)):
        cnt=cnt+1
    if((float(data[1])<=30)):
        cnt=cnt+1
    if((float(data[2])>=0.7) and (float(data[2])<=1.3)):
        cnt=cnt+1
    if((float(data[3])>=11.5)):
        cnt=cnt+1
    if((float(data[4])>=38.3) and (float(data[4])<=48.6)):
        cnt=cnt+1
    if(cnt>=3):
        return 0
    else:
        return 1
