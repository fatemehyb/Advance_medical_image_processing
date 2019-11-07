# MDSC 689.03
# February 2017
#Fatemeh Yazdanbakhsh Poodeh
# week 4-visualization
#
# This example shows how to use a basic implicit function to extract a VOI
#
# How to run:
#to run the program you can change option to select between volum rendering or surface rendering
# and by choosing low and high you can select your segmentation threshoulds
#options of visualization
# option='volume' or 'surface'
#
#low defines the low threshould of segmentation
# low=100
#low defines the high threshould of segmentation
# high=500
#
#vtkImg = LoadData('head.nii')
#you can select any dataset you like but you have to put the dataset in the same directory of this program
# then run program
# python week4-assignment.py
########################

# Load packages
import sys
import os
import argparse
import vtk
import random
import numpy as np
import SimpleITK as sitk

def visualize(txt_Wurl):
    winSize = 800


    #############################################
    def LoadData(datapath):
        '''
        Function to load input image in NIFTI or DICOM
        Argument: path to the input file
        Returns: a vtkImageData '''

        reader = vtk.vtkImageReader()
        if (os.path.isdir(datapath)):
            reader = vtk.vtkDICOMImageReader()
            reader.SetDirectoryName(datapath)
        else:
            reader = vtk.vtkNIFTIImageReader()
            reader.SetFileName(datapath)
        reader.SetDataScalarType(vtk.VTK_UNSIGNED_SHORT)
        reader.SetDataByteOrderToLittleEndian()
        reader.SetNumberOfScalarComponents(1)
        reader.Update()
        return reader.GetOutput()

    def Global_theresholding2(Image):
        T1=random.randint(Image.GetScalarRange()[0],Image.GetScalarRange()[1])
        T1=low
        T2=high
        T0=0
        Height = Image.GetDimensions()[0]
        Width = Image.GetDimensions()[1]
        Depth = Image.GetDimensions()[2]

        # Image newImage(3, Matrix(newImageHeight, Array(newImageWidth)))
        newImage = np.zeros((Height, Width, Depth), float)
        F1=[]
        F2=[]
        # for d in range(0,3):
        for i in range(3, Height - 3):
            for j in range(3, Width - 3):
                for z in range(3, Depth - 3):
                    voxelValue = Image.GetScalarComponentAsFloat(i, j, z, 0)
                    if voxelValue>T1 and voxelValue<T2:
                        F1.append((voxelValue))
                        Image.SetScalarComponentFromFloat(i, j, z, 0, 255)
                    else:
                        F2.append((voxelValue))
                        Image.SetScalarComponentFromFloat(i, j, z, 0, 0)

        return Image

    # Display using image view\
    # er convenience class
    ###################################################


    def volume_renderer(img):
        #Create the renderers, render window, and interactor
        renWin=vtk.vtkRenderWindow()
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(renWin)
        ren=vtk.vtkRenderer()
        ren.SetBackground(0.0, 0.0, 0.0)
        renWin.AddRenderer(ren)


        #Create a transfer function mapping scalar value to opacity
        oTFun=vtk.vtkPiecewiseFunction()
        # oTFun.AddSegment(0,1.0,256,0.1)

        oTFun.AddPoint(0, 0.0)
        oTFun.AddPoint(low, 0.1)
        oTFun.AddPoint(high, 0.8)
        oTFun.AddPoint(100, 0.05)

        cTFun=vtk.vtkColorTransferFunction()

        cTFun.AddRGBPoint(0, 0.0, 0.0, 0.0)  # background
        cTFun.AddRGBPoint(low, 0.7, 0.0, 0.3)
        cTFun.AddRGBPoint(high, 0.0, 0.0, 0.5)
        cTFun.AddRGBPoint(200, 1.0, 0.8, 0.5)

        gradient = vtk.vtkPiecewiseFunction()
        gradient.AddPoint(0, 0.0)
        gradient.AddPoint(high, 0.5)
        gradient.AddPoint(150, 1.0)



        property =vtk.vtkVolumeProperty()
        property.SetScalarOpacity(oTFun)
        property.SetColor(cTFun)
        property.SetInterpolationTypeToLinear()



        mapper =vtk.vtkFixedPointVolumeRayCastMapper()
        #mapper.SetBlendModeToMinimumIntensity()
        mapper.SetInputData(img )


        volume =vtk.vtkVolume()
        volume.SetMapper(mapper)
        volume.SetProperty(property)
        volume.Update()

        ren.AddViewProp(volume)

        iren.Initialize()
        iren.Start()







    ###################################################
    def surface_renderer(img):
        # get iso surface as polydata
        marcher = vtk.vtkMarchingCubes()
        marcher.SetInputData(img)
        marcher.SetValue(0, 255)
        marcher.ComputeNormalsOn()
        marcher.Update()

        # mapper-actor-render-renderwindow sequence
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(marcher.GetOutput())
        mapper.ScalarVisibilityOff()

        actor = vtk.vtkLODActor()
        actor.SetMapper(mapper)
        actor.SetNumberOfCloudPoints(1000000)
        actor.GetProperty().SetColor(1.6, 0.0, 2)
        actor.GetProperty().SetOpacity(0.5)

        render = vtk.vtkRenderer()
        render.AddActor(actor)
        render.SetBackground(0.0, 0.0, 0.0)

        window = vtk.vtkRenderWindow()
        window.AddRenderer(render)
        window.PolygonSmoothingOn()
        window.SetSize(500, 500)

        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(window)

        iren.Initialize()
        window.Render()
        iren.Start()


    vtkImg = LoadData(txt_Wurl)

    # filename='/Users/Fatemeh/Documents/Advance_Medical_Image_Datasets/head.nii'

    #options of visualization
    # option='volume'
    option='surface'
    low=70
    high=3000

    viewer = vtk.vtkImageViewer()


    # Smooth the image data
    gauss = vtk.vtkImageGaussianSmooth()
    gauss.SetInputData(vtkImg)
    gauss.SetDimensionality(3)
    gauss.SetStandardDeviations([2.0,2.0,2.0])
    gauss.SetRadiusFactors(1.0,1.0,1.0)
    gauss.Update()


    #theresholding image
    thresh = vtk.vtkImageThreshold()
    thresh.SetInputData(gauss.GetOutput())
    thresh.ThresholdBetween(low, high)
    thresh.ReplaceInOn()
    thresh.SetInValue(255)
    thresh.ReplaceOutOn()
    thresh.SetOutValue(0)
    thresh.SetOutputScalarTypeToFloat()
    thresh.Update()

    if option == 'surface':
      surface_renderer(thresh.GetOutput())
      #surface_renderer(numpy_array)
    if option == 'volume':
        volume_renderer(vtkImg)
    # else:
    #     print('Select a valid option please..')
