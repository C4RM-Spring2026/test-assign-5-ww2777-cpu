import numpy as np


def getBondDuration(y, face, couponRate, m, ppy=1):
    periods=m*ppy
    cf=face*couponRate/ppy
    i=np.arange(1,periods+1)
    discount=(1+y/ppy)**(-i)
    pvsum=(cf*discount).sum()+face*(1+y/ppy)**(-periods)
    wtsum=(i*cf*discount).sum()+periods*face*(1+y/ppy)**(-periods)
    return((wtsum/pvsum)/ppy)


