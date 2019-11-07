import tkinter as tk # this is in python 3.4. For python 2.x import Tkinter
from PIL import Image, ImageTk
import dicom
import itk
import read_image_m as RIM
import pylab
import numpy as np
import shapely
from shapely.geometry import Polygon
from shapely.geometry import MultiPoint
from shapely.geometry import Point
import scipy

# X=[]
# Y=[]
class ExampleApp(tk.Toplevel):

    drawing_tool = "pencil"
    left_but = "up"

    # x and y positions for drawing with pencil
    x_pos, y_pos = None, None

    X=[]
    Y=[]

    # Tracks x & y when the mouse is clicked and released
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None
    def __init__(self,Image_matrix):
        # super(ExampleApp,self).__init__(self,Image_matrix)
        tk.Toplevel.__init__(self)

        self.Image_matrix=Image_matrix
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=1000, height=1000, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        #self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<B1-Motion>", self.motion)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None



        self._draw_image()


    def _draw_image(self):

         # im=RIM.dicom_reader('U:\Documents\medical_imaging\D3Slice270.dcm')
         # PixelType = itk.ctype('signed short')
         # Dimension = 2
         # ImageType_threshold = itk.Image[PixelType, Dimension]
         # thresholdFilter= itk.IntensityWindowingImageFilter[ImageType_threshold,ImageType_threshold].New()
         # thresholdFilter.SetInput(im)
         # thresholdFilter.SetWindowMinimum(600)
         # thresholdFilter.SetWindowMaximum(1000)
         # thresholdFilter.SetOutputMinimum(0)
         # thresholdFilter.SetOutputMaximum(255)
         # thresholdFilter.Update()
         # # threshold_input=thresholdFilter.GetOutput()
         # im=itk.GetArrayFromImage(thresholdFilter.GetOutput())
         f=self.Image_matrix

         # sa=Image.fromarray(f)
         #f=Image.open('U:\Documents\medical_imaging\ytestimage.png')
         # pylab.imsave('U:\Documents\medical_imaging\ytestimage_copy.gif',f,cmap=pylab.cm.bone)
         #
         # self.im = Image.open('U:\Documents\medical_imaging\ytestimage_copy.gif')
         pylab.imsave('U:\Documents\medical_imaging\ytestimage_copy.dcm',f,cmap=pylab.cm.bone)
         sa=Image.open('U:\Documents\medical_imaging\ytestimage_copy.dcm')
         # sa=Image.fromarray(f)
         #sa=scipy.misc.imrotate(sa,90)
         self.tk_im = ImageTk.PhotoImage(sa)
         # label=self.Label(self,image=self.tk_im)
         # label.image=self.tk_im
         self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)



    def on_button_press(self, event):
        # save mouse drag start position
        # self.start_x = event.x
        # self.start_y = event.y
        #
        # # create rectangle if not yet exist
        # #if not self.rect:
        # self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill="black")
        self.left_but = "down"

        # Set x & y when mouse is clicked
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    ######################################
    def motion(self, event=None):

        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    # ---------- DRAW PENCIL ----------

    def pencil_draw(self, event=None):
        if self.left_but == "down":

            # Make sure x and y have a value
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=True,fill="red")

            self.x_pos = event.x
            self.y_pos = event.y
            self.X.append(self.x_pos)
            self.Y.append(self.y_pos)
    #####################################

    def on_button_release(self, event):
        pass


def main(Image_matrix):


    # root=tk.Toplevel()
    app = ExampleApp(Image_matrix)
    app.X=[]
    app.Y=[]
    app.mainloop()
    k=np.ones(app.X.__len__())
    #print(X)
    #print(Y)
    P=((app.X,app.Y,k))


    return P



    # P=np.transpose(P)
    # Poly=Polygon(P)
    #
    # Poly.contains(Point(100,100))
    # x,y = Poly.exterior.xy
    # x1,y1=Poly.interiors.coords
    # pp=(x,y)
    # pp=np.transpose(pp)

    #print(P)

# canvas = Canvas(width=200, height=200, bg='black')
# im = dicom.read_file('U:\Documents\medical_imaging\y015.dcm')
# # pylab.imsave('U:\Documents\medical_imaging\y015_copy.gif',im.pixel_array,cmap=pylab.cm.bone)
# im2=Image.open('U:\Documents\medical_imaging\y015_copy.gif')
# im2.save('U:\Documents\medical_imaging\y015_copy.gif','gif')
# Image._show(im2)
# canvas.pack(expand=YES, fill=BOTH)
# gif1=PhotoImage(('U:\Documents\medical_imaging\y015_copy.png'))
# #pylab.imsave('U:\Documents\medical_imaging\y015_copy.gif',im.pixel_array,cmap=pylab.cm.bone)
# #Image._show(gif1)
# #canvas.create_image(50, 10, image=im2, anchor=NW)
# gif1 = PhotoImage(file=('U:\Documents\medical_imaging\y015_copy.gif'))
# #canvas.create_image(1, 10, image=gif1, anchor=NW)
# #Image._show(gif1)
# #im2=Image.open('U:\Documents\medical_imaging\y015_copy.png')
# lable=Label(root,image=gif1)
# lable.image=gif1
# lable.pack()
# # canvas.create_image(50, 10, image=im2, anchor=NW)
#
# # im = dicom.read_file('U:\Documents\medical_imaging\y015.dcm')
# # # im=RIM.dicom_reader()
# # # im=itk.GetArrayFromImage(im)
# # # f=im.pixel_array
# # # sa=Image.fromarray(f)
# # # tkimage = ImageTk.PhotoImage(sa)
# # pylab.imsave('U:\Documents\medical_imaging\y015_copy.png',im.pixel_array,cmap=pylab.cm.bone)
# # im2=Image.open('U:\Documents\medical_imaging\y015_copy.png')
# # Image._show(im2)
# # tkinter.Label(root, image=im2).pack()
