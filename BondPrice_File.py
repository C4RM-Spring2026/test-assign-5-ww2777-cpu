import numpy as np
    


def getBondPrice(y, face, couponRate, m, ppy=1):
    periods=m*ppy
    cf=face*couponRate/ppy
    i=np.arange(1,periods+1)
    discount=(1+y/ppy)**(-i)
    pv_coupon=(cf*discount).sum()
    pv_face=face*(1+y/ppy)**(-periods)
    return(pv_coupon+pv_face)
    




