from statistics import mean, variance
import numpy as np

lista=[9,1,5,3,3,3,2,9,0]
def calculate(list):
   
    if len(list)!=9:       
        raise ValueError("List must contain nine numbers.")
    else:       
        a=np.array(list).reshape((3,3))
    
    # print(a)
    # ----------MEAN----------
    mean=[(a.mean(axis=0).tolist()),(a.mean(axis=1).tolist()),(a.flatten().mean())]
    # print(mean.tolist())
    
    # --------VARIANCE-------
    variance=([a.var(axis=0).tolist(),a.var(axis=1).tolist(),a.flatten().var()])
    # print(variance.tolist())
   
    # -------Standar Deviation---------
    stde=([a.std(axis=0).tolist(),a.std(axis=1).tolist(),a.flatten().std()])
    # print(stde.tolist())
    # ------MAX--------------
    max=([a.max(axis=0).tolist(),a.max(axis=1).tolist(),a.flatten().max()])
    # print(max.tolist())
    # ------MIN-------------
    min=([a.min(axis=0).tolist(),a.min(axis=1).tolist(),a.flatten().min()])
    # print(min)

    # ------SUM
    sum=([a.sum(axis=0).tolist(),a.sum(axis=1).tolist(),a.flatten().sum()])
    # print(sum)
    calculations={"mean":mean,
                "variance":variance,
                "standard deviation":stde,
                "max":max,
                "min":min,
                "sum":sum}

    print(calculations)
    
  
calculate(lista)   
        