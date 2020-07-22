import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
        
    y = np.array(list)
    y = y.reshape(3,3)
    y
    z = np.array([[y.mean(axis=0).tolist(), y.mean(axis=1).tolist(), y.mean()], [y.var(axis=0).tolist(), y.var(axis=1).tolist(), y.var()], [y.std(axis=0).tolist(), y.std(axis=1).tolist(), y.std()], [y.max(axis=0).tolist(), y.max(axis=1).tolist(), y.max()], [y.min(axis=0).tolist(), y.min(axis=1).tolist(), y.min()], [y.sum(axis=0).tolist(), y.sum(axis=1).tolist(), y.sum()]])
    z = z.reshape(6,3)
    z = z.tolist()
    calculations = {}
    calculations['mean'] = z[0]
    calculations['variance'] = z[1]
    calculations['standard deviation'] = z[2]
    calculations['max'] = z[3]
    calculations['min'] = z[4]
    calculations['sum'] = z[5]
    
    return calculations