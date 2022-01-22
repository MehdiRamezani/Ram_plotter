# define function to draw line, given 2 points, and extends in y dircetion
# points give in form of p_1=(x_1,y_1) , p_2=(x_2,y_2)
def plot_arb_lines(p_1,p_2, height=4.8):
    # meV it is the extend of the lines in Y direction
    slope = (p_2[1]-p_1[1])/(p_2[0]-p_1[0]) #define slope
    intercept= p_1[1] - (slope * p_1[0])#intercept
    p_start_x , p_start_y = (-height - intercept)/slope , -height #the first point on positive slope.
    p_start = ([p_start_x , p_start_y])
    p_stop_x ,  p_stop_y  =  (height - intercept) /slope,  height #the last point on positive slpe
    p_stop = ([p_stop_x , p_stop_y])
    print( "p_start= ", p_start)
    print( "p_stop= ", p_stop)
    return(p_start , p_stop)

