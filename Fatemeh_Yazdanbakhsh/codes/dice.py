#!/usr/bin/env python

import vtk
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy
import collections
dir = 'U:\Documents\medical_imaging\Results\Hip_to_compare.nii'
reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(dir)
reader.Update()



#manualy segmented volume using ITK-snap
dir2='U:\Documents\medical_imaging\Segmented_HIP.nii'
reader2 = vtk.vtkNIFTIImageReader()
reader2.SetFileName(dir2)
reader2.Update()




thresh = vtk.vtkImageThreshold()
thresh.SetInputData(reader.GetOutput())
thresh.ThresholdBetween(255, 256)
thresh.ReplaceInOn()
thresh.SetInValue(1)
thresh.ReplaceOutOn()
thresh.SetOutValue(0)
thresh.SetOutputScalarTypeToFloat()
thresh.Update()

im = thresh.GetOutput()
rows, cols, depth1= im.GetDimensions()
sc = im.GetPointData().GetScalars()
a = vtk_to_numpy(sc)
a = a.reshape(rows, cols, depth1)
assert a.shape==im.GetDimensions()


thresh2 = vtk.vtkImageThreshold()
thresh2.SetInputData(reader2.GetOutput())
thresh2.ThresholdBetween(1,2)
thresh2.ReplaceInOn()
thresh2.SetInValue(1)
thresh2.ReplaceOutOn()
thresh2.SetOutValue(0)
thresh2.SetOutputScalarTypeToFloat()
thresh2.Update()

im2 = thresh2.GetOutput()
rows2, cols2, depth2 = im2.GetDimensions()
sc2 = im2.GetPointData().GetScalars()
a2= vtk_to_numpy(sc2)
a2 = a2.reshape(rows2, cols2, depth2)

# assert a2.shape==im2.GetDimensions()

im1 = np.asarray(a)
im2 = np.asarray(a2)

if im1.shape != im2.shape:
    raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

# Compute Dice coefficient
intersection = np.multiply(im1, im2)
print(np.count_nonzero(a))
print(np.count_nonzero(a2))
print(2. * intersection.sum() / (im1.sum() + im2.sum()))
