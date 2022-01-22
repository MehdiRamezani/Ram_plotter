## consider solow axis as X-axis, and fast axis as Y-axis. 
## The class extractor can extract all the variables, and plot horizontal linecuts, and 
# vertical lincuts, from a 2D map at any setpoint value. 
## 
## slow axis changes for each slow_axis[n,:]
## fast-axis changes for each fast-axis[:,m]
import numpy as np

class mplot_handle:
    def __init__(self, data, rows, columns, setpoint=None , degree=None, handle0=0,  handle1=1, handle2=2 , handle3=3, handle4=4, handle5=5, handle6=6):
#         super().__init__(name = "Plot 3D or 2D from .dat file")
        self._data = data
        self._rows= rows 
        self._columns= columns 
        self._setpoint = setpoint 
        self._degree= degree 
        self._handle0= handle0 
        self._handle1= handle1 
        self._handle2= handle2 
        self._handle3= handle3 
        self._handle4= handle4 
        self._handle5= handle5 
        self._handle6= handle6 
    
    def colorplot (data, rows, columns , handle0,  handle1, handle2 , handle3, handle4, handle5, handle6):
        handle0 = np.reshape(data[:,handle0], ( columns , rows )) 
        handle1 = np.reshape(data[:,handle1], (columns , rows)) 
        handle2 = np.reshape(data[:,handle2], ( columns , rows )) 
        handle3 = np.reshape(data[:,handle3], ( columns , rows )) 
        handle4 = np.reshape(data[:,handle4], ( columns , rows )) 
        handle5 = np.reshape(data[:,handle5], ( columns , rows )) 
        handle6 = np.reshape(data[:,handle6], ( columns , rows )) 
        return(handle0, handle1 , handle2 , handle3 , handle4, handle5, handle6 )
    
    #### vertical cross section. along slow axis @ each fast axis datapoint.   
    def vmean ( data, rows, columns , setpoint, degree, handle0,  handle1, handle2 , handle3, handle4, handle5, handle6): 
        handle0 = np.reshape(data[:,handle0], ( columns , rows )) 
        handle1 = np.reshape(data[:,handle1], (columns , rows)) 
        handle2 = np.reshape(data[:,handle2], ( columns , rows )) 
        handle3 = np.reshape(data[:,handle3], ( columns , rows )) 
        handle4 = np.reshape(data[:,handle4], ( columns , rows )) 
        handle5 = np.reshape(data[:,handle5], ( columns , rows )) 
        handle6 = np.reshape(data[:,handle6], ( columns , rows )) 

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
            
            R_sub_vline= R_sub[indx_x, :] # y axis of 2D graph     
            G_sub_vline= G_sub[indx_x, :] # y axis of 2D graph 
            
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
        
        
    def vline ( data, rows, columns , setpoint, degree, handle0,  handle1, handle2 , handle3, handle4, handle5, handle6): 
        handle0 = np.reshape(data[:,handle0], ( columns , rows )) 
        handle1 = np.reshape(data[:,handle1], (columns , rows)) 
        handle2 = np.reshape(data[:,handle2], ( columns , rows )) 
        handle3 = np.reshape(data[:,handle3], ( columns , rows )) 
        handle4 = np.reshape(data[:,handle4], ( columns , rows )) 
        handle5 = np.reshape(data[:,handle5], ( columns , rows )) 
        handle6 = np.reshape(data[:,handle6], ( columns , rows )) 
     

        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_handle2 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle3 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle4 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle5 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle6 = np.zeros_like(handle0)    # an empty image for background fits
        # function to to fitting
        for col in np.arange(handle0.shape[0]):  # for the length of the column (i.e. each column ...)
            fit_id_handle2 = np.polyfit(handle1[col , :] , handle2[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle2[col , :]= np.polyval(fit_id_handle2 , handle1[col , :])   # Eval poly at ALL row positions

            fit_id_handle3 = np.polyfit(handle1[col , :] , handle3[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle3[col , :]= np.polyval(fit_id_handle3 , handle1[col , :])   # Eval poly at ALL row positions

            fit_id_handle4 = np.polyfit(handle1[col , :] , handle4[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle4[col , :]= np.polyval(fit_id_handle4 , handle1[col , :])   # Eval poly at ALL row positions

            fit_id_handle5 = np.polyfit(handle1[col , :] , handle5[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle5[col , :]= np.polyval(fit_id_handle5 , handle1[col , :])   # Eval poly at ALL row positions

            fit_id_handle6 = np.polyfit(handle1[col , :] , handle6[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle6[col , :]= np.polyval(fit_id_handle6 , handle1[col , :])   # Eval poly at ALL row positions

        # now lets fill in the empty matrixes for the subtracted data
        handle2_sub = handle2-bkg_map_handle2
        handle3_sub = handle3-bkg_map_handle3
        handle4_sub = handle4-bkg_map_handle4
        handle5_sub = handle5-bkg_map_handle5
        handle6_sub = handle6-bkg_map_handle6
            
        # check if condition to check if it is sweep up or sweep down  
#         print("handle0[0,0] =",handle0[0,0])
#         print("handle0[1,0] =",handle0[1,0])    
        if handle0[0,0] < handle0[1,0]:
            indx_x = np.where( handle0[:,0] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            handle1_vline= handle1[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            handle2_vline= handle2[indx_x, :] # y axis of 2D graph     
            handle3_vline= handle3[indx_x, :] # y axis of 2D graph  
            handle4_vline= handle4[indx_x, :] # y axis of 2D graph  
            handle5_vline= handle5[indx_x, :] # y axis of 2D graph  
            handle6_vline= handle6[indx_x, :] # y axis of 2D graph  
            
            handle2_sub_vline= handle2_sub[indx_x, :] # y axis of 2D graph     
            handle3_sub_vline= handle3_sub[indx_x, :] # y axis of 2D graph 
            handle4_sub_vline= handle4_sub[indx_x, :] # y axis of 2D graph 
            handle5_sub_vline= handle5_sub[indx_x, :] # y axis of 2D graph 
            handle6_sub_vline= handle6_sub[indx_x, :] # y axis of 2D graph 

            return (handle1_vline , handle2_vline, handle2_sub_vline, handle3_vline , handle3_sub_vline, handle4_vline, handle4_sub_vline , handle5_vline, handle5_sub_vline , handle6_vline, handle6_sub_vline , handle0, handle1, handle2, handle2_sub, handle3, handle3_sub,  handle4, handle4_sub ,  handle5, handle5_sub ,  handle6, handle6_sub )
        else:
            indx_x = np.where( handle0[:,0] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            handle1_vline= handle1[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            handle2_vline= handle2[indx_x, :] # y axis of 2D graph     
            handle3_vline= handle3[indx_x, :] # y axis of 2D graph  
            handle4_vline= handle4[indx_x, :] # y axis of 2D graph  
            handle5_vline= handle5[indx_x, :] # y axis of 2D graph  
            handle6_vline= handle6[indx_x, :] # y axis of 2D graph  
            
            handle2_sub_vline= handle2_sub[indx_x, :] # y axis of 2D graph     
            handle3_sub_vline= handle3_sub[indx_x, :] # y axis of 2D graph 
            handle4_sub_vline= handle4_sub[indx_x, :] # y axis of 2D graph 
            handle5_sub_vline= handle5_sub[indx_x, :] # y axis of 2D graph 
            handle6_sub_vline= handle6_sub[indx_x, :] # y axis of 2D graph 
            
            return (handle1_vline , handle2_vline, handle2_sub_vline, handle3_vline , handle3_sub_vline, handle4_vline, handle4_sub_vline , handle5_vline, handle5_sub_vline , handle6_vline, handle6_sub_vline , handle0, handle1, handle2, handle2_sub, handle3, handle3_sub,  handle4, handle4_sub ,  handle5, handle5_sub ,  handle6, handle6_sub )

    #### horizontal cross section. along fast axis @ each slow axis datapoint.
    def hline( data, rows, columns , setpoint, degree, handle0,  handle1, handle2 , handle3, handle4, handle5, handle6): 

        handle0 = np.reshape(data[:,handle0], ( columns , rows )) 
        handle1 = np.reshape(data[:,handle1], (columns , rows)) 
        handle2 = np.reshape(data[:,handle2], ( columns , rows )) 
        handle3 = np.reshape(data[:,handle3], ( columns , rows )) 
        handle4 = np.reshape(data[:,handle4], ( columns , rows )) 
        handle5 = np.reshape(data[:,handle5], ( columns , rows )) 
        handle6 = np.reshape(data[:,handle6], ( columns , rows )) 

        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_handle2 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle3 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle4 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle5 = np.zeros_like(handle0)    # an empty image for background fits
        bkg_map_handle6 = np.zeros_like(handle0)    # an empty image for background fits
        # function to to fitting
        for col in np.arange(handle0.shape[1]):  # for the length of the column (i.e. each column ...)
            fit_id_handle2 = np.polyfit(handle0[: , col] , handle2[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle2[: , col]= np.polyval(fit_id_handle2 , handle0[: , col])   # Eval poly at ALL row positions
            fit_id_handle3 = np.polyfit(handle0[: , col] , handle3[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle3[: , col]= np.polyval(fit_id_handle3 , handle0[: , col])   # Eval poly at ALL row positions
            fit_id_handle4 = np.polyfit(handle0[: , col] , handle4[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle4[: , col]= np.polyval(fit_id_handle4 , handle0[: , col])   # Eval poly at ALL row positions
            fit_id_handle5 = np.polyfit(handle0[: , col] , handle5[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle5[: , col]= np.polyval(fit_id_handle5 , handle0[: , col])   # Eval poly at ALL row positions
            fit_id_handle6 = np.polyfit(handle0[: , col] , handle6[: , col] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_handle6[: , col]= np.polyval(fit_id_handle6 , handle0[: , col])   # Eval poly at ALL row positions

        # now lets fill in the empty matrixes for the subtracted data
        handle2_sub = handle2-bkg_map_handle2
        handle3_sub = handle3-bkg_map_handle3
        handle4_sub = handle4-bkg_map_handle4
        handle5_sub = handle5-bkg_map_handle5
        handle6_sub = handle6-bkg_map_handle6
        
        # check if condition to check if it is sweep up or sweep down          
        if handle1[0,0] < handle1[0,1]:
            indx_x = np.where( handle1[0,:] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            handle0_hline= handle0[:, indx_x] # x axis of 2D graph 

            # To return data linecut
            # now calculate the line cuts for the unmodified values
            handle2_hline= handle2[:, indx_x] # y axis of 2D graph     
            handle3_hline= handle3[:, indx_x] # y axis of 2D graph   
            handle4_hline= handle4[:, indx_x] # y axis of 2D graph     
            handle5_hline= handle5[:, indx_x] # y axis of 2D graph   
            handle6_hline= handle6[:, indx_x] # y axis of 2D graph     

            # now calculate the line cuts for the subtracted values
            handle2_sub_hline= handle2_sub[:, indx_x] # y axis of 2D graph     
            handle3_sub_hline= handle3_sub[:, indx_x] # y axis of 2D graph 
            handle4_sub_hline= handle4_sub[:, indx_x] # y axis of 2D graph 
            handle5_sub_hline= handle5_sub[:, indx_x] # y axis of 2D graph 
            handle6_sub_hline= handle6_sub[:, indx_x] # y axis of 2D graph 
            return (handle0_hline , handle2_hline, handle2_sub_hline, handle3_hline , handle3_sub_hline, handle4_hline, handle4_sub_hline , handle5_hline, handle5_sub_hline , handle6_hline, handle6_sub_hline , handle0, handle1, handle2, handle2_sub, handle3, handle3_sub,  handle4, handle4_sub ,  handle5, handle5_sub ,  handle6, handle6_sub )

        else:
            indx_x = np.where( handle1[0,:] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            handle0_hline= handle0[:, indx_x] # x axis of 2D graph 

            # To return data linecut
            # now calculate the line cuts for the unmodified values
            handle2_hline= handle2[:, indx_x] # y axis of 2D graph     
            handle3_hline= handle3[:, indx_x] # y axis of 2D graph   
            handle4_hline= handle4[:, indx_x] # y axis of 2D graph     
            handle5_hline= handle5[:, indx_x] # y axis of 2D graph   
            handle6_hline= handle6[:, indx_x] # y axis of 2D graph     

            # now calculate the line cuts for the subtracted values
            handle2_sub_hline= handle2_sub[:, indx_x] # y axis of 2D graph     
            handle3_sub_hline= handle3_sub[:, indx_x] # y axis of 2D graph 
            handle4_sub_hline= handle4_sub[:, indx_x] # y axis of 2D graph 
            handle5_sub_hline= handle5_sub[:, indx_x] # y axis of 2D graph 
            handle6_sub_hline= handle6_sub[:, indx_x] # y axis of 2D graph             

            #print ("handle0_hline , handle2_hline, handle2_sub_hline, handle3_hline , handle3_sub_hline, handle4_hline, handle4_sub_hline , handle5_hline, handle5_sub_hline , handle6_hline, handle6_sub_hline , handle0, handle1, handle2, handle2_sub, handle3, handle3_sub,  handle4, handle4_sub ,  handle5, handle5_sub ,  handle6, handle6_sub ")

            return (handle0_hline , handle2_hline, handle2_sub_hline, handle3_hline , handle3_sub_hline, handle4_hline, handle4_sub_hline , handle5_hline, handle5_sub_hline , handle6_hline, handle6_sub_hline , handle0, handle1, handle2, handle2_sub, handle3, handle3_sub,  handle4, handle4_sub ,  handle5, handle5_sub ,  handle6, handle6_sub )
