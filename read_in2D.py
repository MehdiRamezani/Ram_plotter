import numpy as np

def read_in2D(file):
    #read in data file
    with open(file) as f:
        lines = (line for line in f if not line.startswith('#'))
        data = np.loadtxt(lines, delimiter='\t', skiprows=0)
    f.closed
    #convert to array
    data = np.asarray(data, dtype=np.float64)
    
    #get number of rows and columns
    rows = 1
    for k in range(len(data[:,0])):
        if data[k,0] == data[k+1,0]:
            rows += 1
        else:
            break
    columns = int(len(data[:,0])/rows)
    
    return data, rows, columns
