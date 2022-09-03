import matplotlib.pyplot as plt
def BL(x, y):
    # Δx, Δy
    dx = y[0] - x[0]
    dy = y[1] - x[1]
    
    # slope 
    m = dy/dx
    
    # the initial decision parameter
    p = 2*dy - dx
    
    # lists to collect points and the parameters
    next_p = [x]
    parameters = [p]
    
    # initial point
    x0 = x[0]; y0 = x[1]
    
    # loop for Δx - 1
    for i in range(dx):
        if p < 0:
            x0 += 1
            p += 2*dy
        else:
            x0 += 1; y0 +=1
            p += 2*dy - 2*dx

        parameters.append(p)
        next_p.append((x0, y0))
        
    return m, parameters, next_p
    
def main():
    pointx = (20, 10)
    pointy = (30, 18)
    m, p, points = BL(pointx, pointy)
    print("slope: "+str(m), "parameters: "+str(p), "points: "+str(points), sep='\n')
    x = [x[0] for x in points]
    y = [y[1] for y in points]
    plt.xlim(pointx[0]-1, pointy[0]+1)
    plt.ylim(pointx[1]-1, pointy[1]+1)
    plt.scatter(x ,y)
    plt.show()

main()