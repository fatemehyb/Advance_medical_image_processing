import numpy as np
import numpy as np
from PIL import Image, ImageTk
import pylab
#import skimage.filter as filt
import numpy as np
import overlaying
import test_canvas_plot as ICP
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
import show_contour_m as SCM
from skimage.draw import line, polygon, circle, ellipse
import read_points_countour_m as RPM
import mouse_input_m as MIM
import cv2
import write_image_m as WIM

# #options
# Verbose=1
# Wedge=2
# Wline=0.0001
# Wterm=0.0001
# Alpha=0.1
# Beta=4
# Kappa=0.5
# Delta=0.1
# Gamma=0.1
# Iterations=20
# Sigma1=4
# Sigma2=20
# Lambda=0.8
# #options
# Verbose=1
# Wedge=10
# Wline=0.001
# Wterm=0.001
# Alpha=0.001
# Beta=4
# Kappa=0.5
# Delta=0.1
# Gamma=0.1
# Iterations=20
# Sigma1=4
# Sigma2=20
# Lambda=0.8


def function_abstract(P,input_matrix,input_matrix_smoothed,zslice,d,output_volume,flag,txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_gamma,txt_flagDown):
    #options

    Wedge=txt_Wedge
    Wline=txt_Wline
    Wterm=txt_Wterm
    Alpha=txt_alpha
    Beta=txt_beta
    Kappa=0.5
    Delta=0.1
    Gamma=txt_gamma
    Iterations=20
    Sigma1=4
    Sigma2=20
    Lambda=0.8
    x_default=P[0]
    y_default=P[1]
    input_matrix=np.asarray(input_matrix)
    input_matrix_smoothed=np.asarray(input_matrix_smoothed)

    # for k in range(zslice,d-1):
    for k in range(zslice,d-1):
        print('segmenting slice number:')
        print(k)
        x=P[0]

        y=P[1]

        # pylab.imshow(input_matrix[:][:][k])

        x=np.asarray(x)
        y=np.asarray(y)

        fx,fy=s2d.external_energy(input_matrix[k][:][:],input_matrix_smoothed[k][:][:],Wline,Wedge,Wterm, 30. )
        P=s2d.iterate_snake(x,y, Alpha, Beta, fx, fy, Gamma, n_iters=100, return_all=False)
        ##############################
        tck,u= interpolate.splprep( [P[0],P[1]] ,s = 0 )
        xnew,ynew = interpolate.splev( np.linspace( 0, 1, P[0].shape[0] ), tck,der = 0)
        P=[xnew[:],ynew[:]]

    #############################
        contours = np.asarray(P)
        # a3 = np.array( [[[10,10],[100,10],[100,100],[10,100]]], dtype=np.int32 )
        # im = np.zeros([240,320],dtype=np.uint8)
        # cv2.fillPoly( im, a3, 255 )
        # output_volume[:][:][k]=input_matrix[:][:][k]
        #img = np.zeros( (200,200) ) # create a single channel 200x200 pixel black image
        # cv2.fillPoly(output_volume[:][:][k], pts =np.int32([contours]), color=(255,255,255))
        a=np.asarray(P[0]).astype(int)
        b=np.asarray(P[1]).astype(int)
        c=np.ones((1,P[0].size))*int(k)
        # c=c.astype(int)
        # D=np.zeros((1,a.size))
        # for i in range(a.size):
        #     D[:][i]=(a[i],b[i],c[i])


        #output_volume[[([int(i) for i in P[0]])]][[([int(i) for i in P[1]])]][k]=255
        # for i in range(0,w):
        #     # for j in range(0,h):
        #
        #                 index[0]=P[0]
        #                 index[1]=P[1]
        b=np.clip(b,0,511)
        a=np.clip(a,0,511)
        output_volume[k,b[:],a[:]]=255
        rr, cc = polygon(contours[0,:], contours[1,:])
        output_volume[k,cc,rr] = 255
        # cv2.fillPoly(output_volume[k][:][:], pts =np.int32([(contours)]), color=(255,255,255))
        # cv2.imshow("",output_volume[:][:][k])
        # bb=output_volume[k][:][:]
        # Image._show(Image.bb)
        # fig = plt.figure()
        # ax  = fig.add_subplot(111)
        # ax.imshow(bb)
    # # ax.set_xticks([])
    # # ax.set_yticks([])
    # # ax.set_xlim(0,input_matrix.shape[1])
    # # ax.set_ylim(0,input_matrix.shape[2])
    # # pylab.imshow(bb)
    #     plt.show()
        # newImage=overlaying.overlaying(input_matrix[k][:][:],bb)
        #
        # pylab.imshow(bb)
        # #output_volume[P[0]][P[1]][k]=255
        # SCM.show_countour_2d(P,input_matrix,input_matrix_smoothed)
        # #######################################################
        # fig = plt.figure()
        # ax  = fig.add_subplot(111)
        # ax.imshow((input_matrix[:][:][k]), cmap=plt.cm.gray)
        # ax.set_xticks([])
        # ax.set_yticks([])
        # ax.set_xlim(0,input_matrix.shape[1])
        # ax.set_ylim(0,input_matrix.shape[2])
        # #ax.plot(np.r_[x,x[0]], np.r_[y,y[0]], c=(0,1,0), lw=2)
        #
        # # for i, snake in enumerate(contours):
        # #     if i % 10 == 0:
        # #         ax.plot(np.r_[snake[0], snake[0][0]], np.r_[snake[1], snake[1][0]], c=(0,0,1), lw=2)
        #
        # # Plot the last one a different color.
        # ax.plot(P[0],P[1], c=(1,0,0), lw=2)
        #
        #
        # plt.show()

        # ############################################################
                #input_matrix[i][j][k]=  float(input_volume.GetPixel(index))
    if txt_flagDown==1:
        x=x_default
        y=y_default
        for k in range(zslice-1,1,-1):
            print('segmenting slice number:')
            print(k)
            x=np.asarray(x)
            y=np.asarray(y)
            # input_matrix=np.asarray(input_matrix)
            # input_matrix_smoothed=np.asarray(input_matrix_smoothed)
            fx,fy=s2d.external_energy(input_matrix[k][:][:],input_matrix_smoothed[k][:][:],Wline,Wedge,Wterm, 30. )
            P=s2d.iterate_snake(x,y, Alpha, Beta, fx, fy, Gamma, n_iters=100, return_all=False)
            ##############################
            tck,u= interpolate.splprep( [P[0],P[1]] ,s = 0 )
            xnew,ynew = interpolate.splev( np.linspace( 0, 1, P[0].shape[0] ), tck,der = 0)
            P=[xnew[:],ynew[:]]

        #############################
            contours = np.asarray(P)
            # a3 = np.array( [[[10,10],[100,10],[100,100],[10,100]]], dtype=np.int32 )
            # im = np.zeros([240,320],dtype=np.uint8)
            # cv2.fillPoly( im, a3, 255 )
            # output_volume[:][:][k]=input_matrix[:][:][k]
            #img = np.zeros( (200,200) ) # create a single channel 200x200 pixel black image
            # cv2.fillPoly(output_volume[:][:][k], pts =np.int32([contours]), color=(255,255,255))
            a=np.asarray(P[0]).astype(int)
            b=np.asarray(P[1]).astype(int)
            c=np.ones((1,P[0].size))*int(k)
            # c=c.astype(int)
            # D=np.zeros((1,a.size))
            # for i in range(a.size):
            #     D[:][i]=(a[i],b[i],c[i])


            #output_volume[[([int(i) for i in P[0]])]][[([int(i) for i in P[1]])]][k]=255
            # for i in range(0,w):
            #     # for j in range(0,h):
            #
            #                 index[0]=P[0]
            #                 index[1]=P[1]
            b=np.clip(b,0,511)
            a=np.clip(a,0,511)
            output_volume[k,b[:],a[:]]=255
            rr, cc = polygon(contours[0,:], contours[1,:],input_matrix[k][:][:].shape)
            output_volume[k,cc,rr] = 255
            # cv2.fillPoly(output_volume[:][:][k], pts =np.int32([(contours)]), color=(255,255,255))
            # cv2.imshow("",output_volume[:][:][k])
            bb=output_volume[k][:][:]
               #   #######################################################
               #  fig = plt.figure()
               #  ax  = fig.add_subplot(111)
               #  ax.imshow((input_matrix[:][:][k]), cmap=plt.cm.gray)
               #  ax.set_xticks([])
               #  ax.set_yticks([])
               #  ax.set_xlim(0,input_matrix.shape[1])
               #  ax.set_ylim(0,input_matrix.shape[2])
               #  #ax.plot(np.r_[x,x[0]], np.r_[y,y[0]], c=(0,1,0), lw=2)
               #
               #  # for i, snake in enumerate(contours):
               #  #     if i % 10 == 0:
               #  #         ax.plot(np.r_[snake[0], snake[0][0]], np.r_[snake[1], snake[1][0]], c=(0,0,1), lw=2)
               #
               #  # Plot the last one a different color.
               #  ax.plot(P[0],P[1], c=(1,0,0), lw=2)
               #
               #
               #  plt.show()


    return output_volume
