## consider solow axis as X-axis, and fast axis as Y-axis. 
## The class extractor can extract all the variables, and plot horizontal linecuts, and 
# vertical lincuts, from a 2D map at any setpoint value. 
## 
## slow axis changes for each slow_axis[n,:]
## fast-axis changes for each fast-axis[:,m]
import numpy as np

class mplot_data:
    def __init__(self, slow_axis, fast_axis, Z1, Z2 , setpoint=None , degree=None):
#         super().__init__(name = "Plot 3D or 2D from .dat file")
        self._slow_axis = slow_axis
        self._fast_axis= fast_axis 
        self._Z1= Z2
        self._Z1= Z2        
        self._setpoint = setpoint 
        self._degree= degree 
    

    #### vertical cross section. along slow axis @ each fast axis datapoint.   
    def vmean ( slow_axis, fast_axis, Z1, Z2 , setpoint=None , degree=None): 
        slow_axis = slow_axis
        fast_axis= fast_axis 
        Z1= Z1
        Z2= Z2    

        bkg_map_Z1 = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_Z2 = np.zeros_like(slow_axis)    # an empty image for background fits
        for col in np.arange(slow_axis.shape[0]):  # for the length of the column (i.e. each column ...)
            bkg_map_Z1[col , :]=  np.mean(Z1[col , :])  # Eval poly at ALL row positions
            bkg_map_Z2[col , :]=  np.mean(Z2[col , :])  # Eval poly at ALL row positions
        Z1_sub = Z1-bkg_map_Z1
        Z2_sub = Z2-bkg_map_Z2      

        # check if condition to check if it is sweep up or sweep down  
#         print("slow_axis[0,0] =",slow_axis[0,0])
#         print("slow_axis[1,0] =",slow_axis[1,0])    
        if slow_axis[0,0] < slow_axis[1,0]:
            indx_x = np.where( slow_axis[:,0] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            Z1_vline= Z1[indx_x, :] # y axis of 2D graph     
            Z2_vline= Z2[indx_x, :] # y axis of 2D graph  
            
            Z1_sub_vline= Z1_sub[indx_x, :] # y axis of 2D graph     
            Z2_sub_vline= Z2_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , Z1_vline, Z1_sub_vline, Z2_vline , Z2_sub_vline, slow_axis, fast_axis, Z1, Z1_sub, Z2, Z2_sub  )
        else:
            indx_x = np.where( slow_axis[:,0] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            Z1_vline= Z1[indx_x, :] # y axis of 2D graph     
            Z2_vline= Z2[indx_x, :] # y axis of 2D graph 

            Z1_sub_vline= Z1_sub[indx_x, :] # y axis of 2D graph     
            Z2_sub_vline= Z2_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , Z1_vline, Z1_sub_vline, Z2_vline , Z2_sub_vline, slow_axis, fast_axis, Z1, Z1_sub, Z2, Z2_sub  )

        
        


#         return(slow_axis, fast_axis , Z1, Z1_sub, Z2 , Z2_sub )
    #### vertical cross section. along slow axis @ each fast axis datapoint.   
    def vline ( slow_axis, fast_axis, Z1, Z2 , setpoint=None , degree=None): 

        slow_axis = slow_axis
        fast_axis= fast_axis 
        Z1= Z1
        Z2= Z2    

        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_Z1 = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_Z2 = np.zeros_like(slow_axis)    # an empty image for background fits
        # function to to fitting
        for col in np.arange(slow_axis.shape[0]):  # for the length of the column (i.e. each column ...)
            fit_id_Z1 = np.polyfit(fast_axis[col , :] , Z1[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_Z1[col , :]= np.polyval(fit_id_Z1 , fast_axis[col , :])   # Eval poly at ALL row positions
            fit_id_Z2 = np.polyfit(fast_axis[col , :] , Z2[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_Z2[col , :]= np.polyval(fit_id_Z2 , fast_axis[col , :])   # Eval poly at ALL row positions
        Z1_sub = Z1-bkg_map_Z1
        Z2_sub = Z2-bkg_map_Z2    
                           
            
        # check if condition to check if it is sweep up or sweep down  
#         print("slow_axis[0,0] =",slow_axis[0,0])
#         print("slow_axis[1,0] =",slow_axis[1,0])    
        if slow_axis[0,0] < slow_axis[1,0]:
            indx_x = np.where( slow_axis[:,0] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            Z1_vline= Z1[indx_x, :] # y axis of 2D graph     
            Z2_vline= Z2[indx_x, :] # y axis of 2D graph  
            
            Z1_sub_vline= Z1_sub[indx_x, :] # y axis of 2D graph     
            Z2_sub_vline= Z2_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , Z1_vline, Z1_sub_vline, Z2_vline , Z2_sub_vline, slow_axis, fast_axis, Z1, Z1_sub, Z2, Z2_sub  )
        else:
            indx_x = np.where( slow_axis[:,0] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            fast_axis_vline= fast_axis[indx_x, :] # x axis of 2D graph 
            # To return data linecut
            Z1_vline= Z1[indx_x, :] # y axis of 2D graph     
            Z2_vline= Z2[indx_x, :] # y axis of 2D graph 

            Z1_sub_vline= Z1_sub[indx_x, :] # y axis of 2D graph     
            Z2_sub_vline= Z2_sub[indx_x, :] # y axis of 2D graph 
            
            return (fast_axis_vline , Z1_vline, Z1_sub_vline, Z2_vline , Z2_sub_vline, slow_axis, fast_axis, Z1, Z1_sub, Z2, Z2_sub  )
    
    #### horizontal cross section. along fast axis @ each slow axis datapoint.
    def hline( slow_axis, fast_axis, Z1, Z2 , setpoint=None , degree=None): 

        slow_axis = slow_axis
        fast_axis= fast_axis 
        Z1= Z1
        Z2= Z2    

        # Subtracting a polynomial background from the measurements:
        # make a matrix of the size of the x values
        bkg_map_Z1 = np.zeros_like(slow_axis)    # an empty image for background fits
        bkg_map_Z2 = np.zeros_like(slow_axis)    # an empty image for background fits
        # function to to fitting
        for col in np.arange(slow_axis.shape[0]):  # for the length of the column (i.e. each column ...)
            fit_id_Z1 = np.polyfit(fast_axis[col , :] , Z1[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_Z1[col , :]= np.polyval(fit_id_Z1 , fast_axis[col , :])   # Eval poly at ALL row positions
            fit_id_Z2 = np.polyfit(fast_axis[col , :] , Z2[col , :] , float(degree) ) # Fit poly over bkg rows for col
            bkg_map_Z2[col , :]= np.polyval(fit_id_Z2 , fast_axis[col , :])   # Eval poly at ALL row positions
        Z1_sub = Z1-bkg_map_Z1
        Z2_sub = Z2-bkg_map_Z2        
        
        
        # check if condition to check if it is sweep up or sweep down          
        if fast_axis[0,0] < fast_axis[0,1]:
            indx_x = np.where( fast_axis[0,:] >= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            slow_axis_hline= slow_axis[:, indx_x] # x axis of 2D graph 
            # To return data linecut
            Z1_hline= Z1[:, indx_x] # y axis of 2D graph     
            Z2_hline= Z2[:, indx_x] # y axis of 2D graph   

            Z1_sub_hline= Z1_sub[:, indx_x] # y axis of 2D graph     
            Z2_sub_hline= Z2_sub[:, indx_x] # y axis of 2D graph             
            
            return (slow_axis_hline , Z1_hline, Z1_sub_hline, Z2_hline , Z2_sub_hline, slow_axis, fast_axis, Z1, Z1_sub, Z2,  Z2_sub   )
        else:
            indx_x = np.where( fast_axis[0,:] <= float(setpoint))
            indx_x = indx_x[0][0]
            
            # extract the valus from the y value, and assign it for the new 2D graph
            slow_axis_hline= slow_axis[: , indx_x] # x axis of 2D graph 
            # To return data linecut
            Z1_hline= Z1[:, indx_x] # y axis of 2D graph     
            Z2_hline= Z2[:, indx_x] # y axis of 2D graph        

            Z1_sub_hline= Z1_sub[:, indx_x] # y axis of 2D graph     
            Z2_sub_hline= Z2_sub[:, indx_x] # y axis of 2D graph               
            
            return (slow_axis_hline , Z1_hline, Z1_sub_hline, Z2_hline , Z2_sub_hline, slow_axis, fast_axis, Z1, Z1_sub, Z2,  Z2_sub   )
