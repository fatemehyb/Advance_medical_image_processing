import numpy as np
from PIL import Image, ImageTk
import pylab
#import skimage.filter as filt
import numpy as np
import overlaying
import simple_mouse_click_edited as ICP
import tkinter as tk
import matplotlib.pyplot as plt
import vtk
from scipy import ndimage
#from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk
from scipy import interpolate
# import test_snake_jpg as s2d
import test_19_march as s2d
# import test19_march2 as s2d
import read_image_m as RIM
import smooth_filter_m as SFM
import function_abstract as func
import show_contour_m as SCM

import read_points_countour_m as RPM
import mouse_input_m as MIM
import cv2
import write_image_m as WIM
#options


# Wedge=2
# Wline=0.04
# Wterm=0.01
# Alpha=0.001
# Beta=4
# Kappa=0.5
# Delta=0.1000
# Gamma=100
# Iterations=20
# Sigma1=4
# Sigma2=20
# Lambda=0.8
#image size
w=100
h=100


import itk
def execute(txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_sigma,txt_gamma,txt_start,txt_end,txt_url,txt_start2,txt_end2,flagg,txt_flagDown,txt_Wurl):
    m_string=txt_url
    # m_string='U:\Documents\medical_imaging\Hip'
    input_volume=RIM.dicom_series_reader(m_string)

    # input_volume=im
    #
    PixelType = itk.ctype('signed short')
    Dimension = 3
    ImageType_threshold = itk.Image[PixelType, Dimension]
    # thresholdFilter= itk.BinaryThresholdImageFilter[ImageType_threshold,ImageType_threshold].New()
    thresholdFilter= itk.IntensityWindowingImageFilter[ImageType_threshold,ImageType_threshold].New()
    # thresholdFilter= itk.InvertIntensityImageFilter[ImageType_threshold,ImageType_threshold].New()
    thresholdFilter.SetInput(input_volume)

    # thresholdFilter.SetLowerThreshold(-400)
    # thresholdFilter.SetUpperThreshold(40)
    # thresholdFilter.SetOutsideValue(0)
    # thresholdFilter.SetInsideValue(255)
    ##################################
    thresholdFilter.SetInput(input_volume)
    thresholdFilter.SetWindowMinimum(-500)
    thresholdFilter.SetWindowMaximum(1)
    thresholdFilter.SetOutputMinimum(0)
    thresholdFilter.SetOutputMaximum(255)
    ######################################
    # thresholdFilter.SetMaximum(10)
    #################################
    thresholdFilter.Update()
    threshold_input=thresholdFilter.GetOutput()

    sigma_smooth = float(txt_sigma)
    smooth_volume=SFM.smooth_3d(input_volume,sigma_smooth)
    w = input_volume.GetLargestPossibleRegion().GetSize()[0]
    h = input_volume.GetLargestPossibleRegion().GetSize()[1]
    d = input_volume.GetLargestPossibleRegion().GetSize()[2]




    input_matrix=np.zeros((w,h,d))
    input_matrix_smoothed=np.zeros((w,h,d))


    index=np.zeros((3))

    input_matrix_smoothed=itk.GetArrayFromImage(smooth_volume)
    # input_matrix_smoothed=np.transpose(input_matrix_smoothed,axes=(2,1,0))
    # input_matrix = itk.GetArrayFromImage(SFM.smooth_3d(thresholdFilter.GetOutput(),sigma_smooth))
    input_matrix = itk.GetArrayFromImage(input_volume)
    # input_matrix = itk.GetArrayFromImage(thresholdFilter.GetOutput())
    # input_matrix=np.transpose(input_matrix,axes=(2,1,0))

    input_matrix2=input_matrix
    input_matrix_smoothed2=input_matrix_smoothed
    # P=RPM.read_points()
    #P,zslice=MIM.mouse_input()
    zslice=txt_start
    zslice2=txt_start2
    d1=txt_end
    d2=txt_end2
    # zslice=498
    # d=829
    # X=[]
    # Y=[]
    # P=[]
    if (flagg==0):
        P=ICP.main((input_matrix[:][:][zslice]))

        P2=ICP.main((input_matrix2[:][:][zslice2]))
        npoints=P[0].__len__()

        ############################
        # output_volume = input_matrix
        output_volume=np.zeros((d,h,w))
        output_volume1=np.zeros((d,h,w))
        output_volume2=np.zeros((d,h,w))
        ##############################
        tck,u= interpolate.splprep( [P[0],P[1]] ,s = 0 )

        xnew,ynew = interpolate.splev( np.linspace( 0, 1, P[0].__len__() ), tck,der = 0)

        P=[xnew[:],ynew[:]]

        ##################################################
        tck2,u2= interpolate.splprep( [P2[0],P2[1]] ,s = 0 )

        xnew2,ynew2 = interpolate.splev( np.linspace( 0, 1, P2[0].__len__() ), tck2,der = 0)

        P2=[xnew2[:],ynew2[:]]

        #############################
        output_volume1=func.function_abstract(P,input_matrix,input_matrix_smoothed,zslice,d1,output_volume1,1,txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_gamma,txt_flagDown)
        output_volume2=func.function_abstract(P2,input_matrix2,input_matrix_smoothed2,zslice2,d2,output_volume2,1,txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_gamma,txt_flagDown)
        output_volume=output_volume1+output_volume2
        # output_volume=output_volume1
        ####################################################################
        output_volume=sitk.GetImageFromArray(output_volume)
        output_volume=sitk.Cast(output_volume,sitk.sitkFloat64)

        # #output_volume = sitk.Cast(output_volume, sitk.sitkInt64)
        sitk.WriteImage(output_volume,txt_Wurl)

    if(flagg==1):
        P=ICP.main((input_matrix[:][:][zslice]))

        # P2=ICP.main((input_matrix2[:][:][zslice2]))
        npoints=P[0].__len__()

        ############################
        # output_volume = input_matrix
        output_volume=np.zeros((d,h,w))
        output_volume1=np.zeros((d,h,w))
        output_volume2=np.zeros((d,h,w))
        ##############################
        tck,u= interpolate.splprep( [P[0],P[1]] ,s = 0 )

        xnew,ynew = interpolate.splev( np.linspace( 0, 1, P[0].__len__() ), tck,der = 0)

        P=[xnew[:],ynew[:]]

        ##################################################
        # tck2,u2= interpolate.splprep( [P2[0],P2[1]] ,s = 0 )
        #
        # xnew2,ynew2 = interpolate.splev( np.linspace( 0, 1, P2[0].__len__() ), tck2,der = 0)
        #
        # P2=[xnew2[:],ynew2[:]]

        #############################
        output_volume1=func.function_abstract(P,input_matrix,input_matrix_smoothed,zslice,d1,output_volume1,1,txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_gamma,txt_flagDown)
        # output_volume2=func.function_abstract(P2,input_matrix2,input_matrix_smoothed2,zslice2,d2,output_volume2,1)
        # output_volume=output_volume1+output_volume2
        output_volume=output_volume1
        ####################################################################
        output_volume=sitk.GetImageFromArray(output_volume)
        output_volume=sitk.Cast(output_volume,sitk.sitkFloat64)

        # #output_volume = sitk.Cast(output_volume, sitk.sitkInt64)
        sitk.WriteImage(output_volume,txt_Wurl)
