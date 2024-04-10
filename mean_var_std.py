import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list)
    matrix.resize((3,3))

    calculations = {
        'mean': [[*matrix.mean(axis=0)],[*matrix.mean(axis=1)], matrix.mean()],
        'variance': [[*matrix.var(axis=0)],[*matrix.var(axis=1)], matrix.var()],
        'standard deviation': [[*matrix.std(axis=0)],[*matrix.std(axis=1)], matrix.std()],
        'max': [[*matrix.max(axis=0)],[*matrix.max(axis=1)], matrix.max()],
        'min':[[*matrix.min(axis=0)],[*matrix.min(axis=1)], matrix.min()],
        'sum': [[*matrix.sum(axis=0)],[*matrix.sum(axis=1)], matrix.sum()]
    }

    return calculations