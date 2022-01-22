## consider solow axis as X-axis, and fast axis as Y-axis. 
## The class extractor can extract all the variables, and plot horizontal linecuts, and 
# vertical lincuts, from a 2D map at any setpoint value. 
## 
## slow axis changes for each slow_axis[n,:]
## fast-axis changes for each fast-axis[:,m]
import numpy as np

class mplot_DC:
    def __init__(self, data, rows, columns, setpoint=None , degree=None):
#         super().__init__(name = "Plot 3D or 2D from .dat file")
        self._data = data
        self._rows= rows 
        self._columns= columns 
        self._setpoint = setpoint 
        self._degree= degree 
    
    def colorplot (data, rows, columns ):
        slow_axis = np.reshape(data[:,0], ( columns , rows )) 
        fast_axis= np.reshape(data[:,1], (columns , rows)) 
        R = np.reshape(data[:,7], ( columns , rows ))
        G = np.reshape(data[:,8], ( columns , rows )) 
        I = np.reshape(data[:,9], ( columns , rows )) 
        return(slow_axis, fast_axis , G, R , I )
    
    #### vertical cross section. along slow axis @ each fast axis datapoint.   
    def vmean ( data, rows, columns , setpoint, degree): 
        slow_axis = np.reshape(data[:,0], ( columns , rows )) 
        fast_axis= np.reshape(data[:,1], (columns , rows)) 
        R= np.reshape(data[:,2], ( columns , rows ))
        G = np.reshape(data[:,3], ( columns , rows )) 

        bkg_map_R = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_G = np.zeros_like(slow_axis)    # an empty image for background fits
        for col in np.arange(slow_axis.shape[0]):  # for the length of the column (i.e. each column ...)
#             mean_R = np.mean(R[col , :]) # Fit poly over bkg rows for col
            bkg_map_R[col , :]=  np.mean(R[col , :])  # Eval poly at ALL row positions
#             mean_G = np.mean(G[col , :]) # Fit poly over bkg rows for col
            bkg_map_G[col , :]=  np.mean(G[col , :])  # Eval poly at ALL row positions
            
        R_sub = R-bkg_map_R
        G_sub = G-bkg_map_G          

        # check if condition to check if it is sweep up or sweep down  
#         print("slow_axis[0,0] =",slow_axis[0,0])
#         print("slow_axis[1,0] =",slow_axis[1,0])    
        if slow_axis[0,0] < slow_axis[1,0]:
            indx_x = np.where( slow_axis[:,0] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            R_vline= R[indx_x, :] # y axis of 2D graph     
            G_vline= G[indx_x, :] # y axis of 2D graph  
            
            R_sub= R_sub[indx_x, :] # y axis of 2D graph     
            G_sub= G_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , G_vline, G_sub_vline, R_vline , R_sub_vline, slow_axis, fast_axis, G, G_sub, R, R_sub  )

        else:
            indx_x = np.where( slow_axis[:,0] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            R_vline= R[indx_x, :] # y axis of 2D graph     
            G_vline= G[indx_x, :] # y axis of 2D graph 

            R_sub_vline= R_sub[indx_x, :] # y axis of 2D graph     
            G_sub_vline= G_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , G_vline, G_sub_vline, R_vline , R_sub_vline, slow_axis, fast_axis, G, G_sub, R, R_sub )
        
###########################        
    
    #### vertical cross section. along slow axis @ each fast axis datapoint.   
    def vline ( data, rows, columns , setpoint, degree): 

        slow_axis = np.reshape(data[:,0], ( columns , rows )) 
        fast_axis= np.reshape(data[:,1], (columns , rows)) 
        R= np.reshape(data[:,7], ( columns , rows ))
        G = np.reshape(data[:,8], ( columns , rows )) 
        I = np.reshape(data[:,9], ( columns , rows ))      

        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_R = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_G = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_I = np.zeros_like(slow_axis)    # an empty image for background fits        
        # function to to fitting
        for col in np.arange(slow_axis.shape[0]):  # for the length of the column (i.e. each column ...)
            fit_id_R = np.polyfit(fast_axis[col , :] , R[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_R[col , :]= np.polyval(fit_id_R , fast_axis[col , :])   # Eval poly at ALL row positions
            fit_id_G = np.polyfit(fast_axis[col , :] , G[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_G[col , :]= np.polyval(fit_id_G , fast_axis[col , :])   # Eval poly at ALL row positions
            fit_id_I = np.polyfit(fast_axis[col , :] , I[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_I[col , :]= np.polyval(fit_id_I , fast_axis[col , :])   # Eval poly at ALL row positions

        R_sub = R-bkg_map_R
        G_sub = G-bkg_map_G    
        I_sub = I-bkg_map_I    
                           
            
        # check if condition to check if it is sweep up or sweep down  
#         print("slow_axis[0,0] =",slow_axis[0,0])
#         print("slow_axis[1,0] =",slow_axis[1,0])    
        if slow_axis[0,0] < slow_axis[1,0]:
            indx_x = np.where( slow_axis[:,0] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            R_vline= R[indx_x, :] # y axis of 2D graph     
            G_vline= G[indx_x, :] # y axis of 2D graph  
            I_vline= I[indx_x, :] # y axis of 2D graph  
            
            R_sub_vline= R_sub[indx_x, :] # y axis of 2D graph     
            G_sub_vline= G_sub[indx_x, :] # y axis of 2D graph 
            I_sub_vline= I_sub[indx_x, :] # y axis of 2D graph 

            
            return (fast_axis_vline , G_vline, G_sub_vline, R_vline , R_sub_vline, I_vline, I_sub_vline, slow_axis, fast_axis, G, G_sub, R, R_sub , I, I_sub )
        else:
            indx_x = np.where( slow_axis[:,0] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            R_vline= R[indx_x, :] # y axis of 2D graph     
            G_vline= G[indx_x, :] # y axis of 2D graph 
            I_vline= I[indx_x, :] # y axis of 2D graph 

            R_sub_vline= R_sub[indx_x, :] # y axis of 2D graph     
            G_sub_vline= G_sub[indx_x, :] # y axis of 2D graph 
            I_sub_vline= I_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , G_vline, G_sub_vline, R_vline , R_sub_vline, I_vline, I_sub_vline, slow_axis, fast_axis, G, G_sub, R, R_sub , I, I_sub )
    
    #### horizontal cross section. along fast axis @ each slow axis datapoint.
    def hline( data, rows, columns , setpoint, degree): 

        slow_axis = np.reshape(data[:,0], ( columns , rows )) 
        fast_axis= np.reshape(data[:,1], (columns , rows)) 
        R= np.reshape(data[:,7], ( columns , rows ))
        G = np.reshape(data[:,8], ( columns , rows )) 
        I = np.reshape(data[:,9], ( columns , rows )) 

        
        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_R = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_G = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_I = np.zeros_like(slow_axis)    # an empty image for background fits        
        # function to to fitting
        for col in np.arange(slow_axis.shape[1]):  # for the length of the column (i.e. each column ...)
            fit_id_R = np.polyfit(slow_axis[: , col] , R[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_R[: , col]= np.polyval(fit_id_R , slow_axis[: , col])   # Eval poly at ALL row positions
            fit_id_G = np.polyfit(slow_axis[: , col] , G[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_G[: , col]= np.polyval(fit_id_G , slow_axis[: , col])   # Eval poly at ALL row positions
            fit_id_I = np.polyfit(slow_axis[: , col] , I[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_I[: , col]= np.polyval(fit_id_I , slow_axis[: , col])   # Eval poly at ALL row positions

        R_sub = R-bkg_map_R
        G_sub = G-bkg_map_G         
        I_sub = G-bkg_map_G         
        
        
        # check if condition to check if it is sweep up or sweep down          
        if fast_axis[0,0] < fast_axis[0,1]:
            indx_x = np.where( fast_axis[0,:] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            slow_axis_hline= slow_axis[:, indx_x] # x axis of 2D graph 
            # To return data linecut
            R_hline= R[:, indx_x] # y axis of 2D graph     
            G_hline= G[:, indx_x] # y axis of 2D graph   
            I_hline= I[:, indx_x] # y axis of 2D graph   

            R_sub_hline= R_sub[:, indx_x] # y axis of 2D graph     
            G_sub_hline= G_sub[:, indx_x] # y axis of 2D graph             
            I_sub_hline= I_sub[:, indx_x] # y axis of 2D graph             
            
            return (slow_axis_hline , G_hline, G_sub_hline, R_hline , R_sub_hline, I_hline, I_sub_hline, slow_axis, fast_axis, G, G_sub, R,  R_sub , I, I_sub   )
        else:
            indx_x = np.where( fast_axis[0,:] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            slow_axis_hline= slow_axis[: , indx_x] # x axis of 2D graph 
            # To return data linecut
            R_hline= R[:, indx_x] # y axis of 2D graph     
            G_hline= G[:, indx_x] # y axis of 2D graph        
            I_hline= I[:, indx_x] # y axis of 2D graph        

            R_sub_hline= R_sub[:, indx_x] # y axis of 2D graph     
            G_sub_hline= G_sub[:, indx_x] # y axis of 2D graph               
            I_sub_hline= I_sub[:, indx_x] # y axis of 2D graph     
            
            return (slow_axis_hline , G_hline, G_sub_hline, R_hline , R_sub_hline, I_hline, I_sub_hline, slow_axis, fast_axis, G, G_sub, R,  R_sub , I, I_sub   )
