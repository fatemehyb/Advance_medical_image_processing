# Simple enough, just import everything from tkinter.
from tkinter import *
import two_components as twc
import visualization_results as vis


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()


    def Exit_clicked(self):
             exit(0)

    def vis_clicked(self):
        txt_Wurl=self.txt_Wurl.get()
        vis.visualize(txt_Wurl)
    # def con_clicked(self):
    #          root.withdraw()
             # res = "Welcome to " + txt.get()
             #
             # lbl.configure(text= res)
    def clicked2(self):

            # Frame.__init__(self, self.master)
            # Frame.__init__(self, self.master)
            # self.init_window()
            txt_Wedge=float(self.txt_Wedge.get())
            txt_Wline=float(self.txt_Wline.get())
            txt_Wterm=float(self.txt_Wterm.get())
            txt_alpha=float(self.txt_alpha.get())
            txt_beta=float(self.txt_beta.get())
            txt_sigma=float(self.txt_sigma.get())
            txt_gamma=float(self.txt_gamma.get())
            txt_start=int(self.txt_start.get())
            txt_end=int(self.txt_end.get())
            txt_url=self.txt_url.get()
            txt_start2=int(self.txt_start2.get())
            txt_end2=int(self.txt_end2.get())
            txt_flagDown=int(self.txt_flagDown.get())
            txt_Wurl=self.txt_Wurl.get()


            twc.execute(txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_sigma,txt_gamma,txt_start,txt_end,txt_url,txt_start2,txt_end2,1,txt_flagDown,txt_Wurl)
            # return 1
    def clicked22(self):

            # Frame.__init__(self, self.master)
            # Frame.__init__(self, self.master)
            # self.init_window()
            txt_Wedge=float(self.txt_Wedge.get())
            txt_Wline=float(self.txt_Wline.get())
            txt_Wterm=float(self.txt_Wterm.get())
            txt_alpha=float(self.txt_alpha.get())
            txt_beta=float(self.txt_beta.get())
            txt_sigma=float(self.txt_sigma.get())
            txt_gamma=float(self.txt_gamma.get())
            txt_start=int(self.txt_start.get())
            txt_end=int(self.txt_end.get())
            txt_url=self.txt_url.get()
            txt_start2=int(self.txt_start2.get())
            txt_end2=int(self.txt_end2.get())
            txt_flagDown=int(self.txt_flagDown.get())
            txt_Wurl=self.txt_Wurl.get()

            twc.execute(txt_Wedge,txt_Wline,txt_Wterm,txt_alpha,txt_beta,txt_sigma,txt_gamma,txt_start,txt_end,txt_url,txt_start2,txt_end2,0,txt_flagDown,txt_Wurl)
            # return 1

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI-Snake 3D")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)




        self.label_Wedge=Label(self,text="Wedge")
        self.label_Wedge.grid(row=0,column=0)
        # self.label_Wedge.pack()
        self.txt_Wedge = Entry(self,width=10)
        self.txt_Wedge.insert(END,'5')
        self.txt_Wedge.grid(row=0,column=1)
        # self.btn_Wedge=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_Wedge.grid(row=0,column=2)
        #########################################
        self.label_Wline=Label(self,text="Wline")
        self.label_Wline.grid(row=1,column=0)
        # self.label_Wedge.pack()
        self.txt_Wline = Entry(self,width=10)
        self.txt_Wline.insert(END,'0.0001')
        self.txt_Wline.grid(row=1,column=1)
        # self.btn_Wline=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_Wline.grid(row=1,column=2)
        #####################################################
        self.label_Wterm=Label(self,text="Wterm")
        self.label_Wterm.grid(row=2,column=0)
        # self.label_Wedge.pack()
        self.txt_Wterm = Entry(self,width=10)
        self.txt_Wterm.insert(END,'0.0001')
        self.txt_Wterm.grid(row=2,column=1)
        # self.btn_Wterm=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_Wterm.grid(row=2,column=2)
        #########################################################
        self.label_alpha=Label(self,text="alpha")
        self.label_alpha.grid(row=3,column=0)
        # self.label_Wedge.pack()
        self.txt_alpha = Entry(self,width=10)
        self.txt_alpha.insert(END,'0.001')
        self.txt_alpha.grid(row=3,column=1)
        # self.btn_alpha=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_alpha.grid(row=3,column=2)
        ##########################################################
        self.label_beta=Label(self,text="beta")
        self.label_beta.grid(row=4,column=0)
        # self.label_Wedge.pack()
        self.txt_beta = Entry(self,width=10)
        self.txt_beta.insert(END,'4')
        self.txt_beta.grid(row=4,column=1)
        # self.btn_beta=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_beta.grid(row=4,column=2)
        ###########################################################
        self.label_sigma=Label(self,text="sigma")
        self.label_sigma.grid(row=5,column=0)
        # self.label_Wedge.pack()
        self.txt_sigma = Entry(self,width=10)
        self.txt_sigma.insert(END,'0.05')
        self.txt_sigma.grid(row=5,column=1)
        # self.btn_sigma=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_sigma.grid(row=5,column=2)
        ############################################################
        self.label_gamma=Label(self,text="gamma")
        self.label_gamma.grid(row=6,column=0)
        # self.label_Wedge.pack()
        self.txt_gamma = Entry(self,width=10)
        self.txt_gamma.insert(END,'0.01')
        self.txt_gamma.grid(row=6,column=1)
        # self.btn_gamma=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_gamma.grid(row=6,column=2)
        ##############################################################
        self.label_url=Label(self,text="image reading url")
        self.label_url.grid(row=7,column=0)
        # self.label_Wedge.pack()
        self.txt_url = Entry(self,width=50)
        self.txt_url.insert(END,'U:\Documents\medical_imaging\Hip')

        self.txt_url.grid(row=7,column=1)
        # self.btn_url=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_url.grid(row=7,column=2)
        ##############################################################
        self.label_Wurl=Label(self,text="volume writting url")
        self.label_Wurl.grid(row=8,column=0)
        # self.label_Wedge.pack()
        self.txt_Wurl = Entry(self,width=50)
        self.txt_Wurl.insert(END,'U:\Documents\medical_imaging\Results\Totlavolume.nii')

        self.txt_Wurl.grid(row=8,column=1)
        # self.btn_url=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_url.grid(row=7,column=2)
        ##############################################################
        self.label_start=Label(self,text="start slice number")
        self.label_start.grid(row=9,column=0)
        # self.label_Wedge.pack()
        self.txt_start = Entry(self,width=50)
        self.txt_start.insert(END,'1')
        self.txt_start.grid(row=9,column=1)
        # self.btn_start=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_start.grid(row=8,column=2)
        ##############################################################
        self.label_end=Label(self,text="end slice number")
        self.label_end.grid(row=10,column=0)
        # self.label_Wedge.pack()
        self.txt_end = Entry(self,width=50)
        self.txt_end.insert(END,'80')
        self.txt_end.grid(row=10,column=1)
        # self.btn_end=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_end.grid(row=9,column=2)
        ##############################################################
        self.label_start2=Label(self,text="start slice2 number")
        self.label_start2.grid(row=11,column=0)
        # self.label_Wedge.pack()
        self.txt_start2 = Entry(self,width=50)
        self.txt_start2.insert(END,'1')
        self.txt_start2.grid(row=11,column=1)
        # self.btn_start=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_start.grid(row=8,column=2)
        ##############################################################
        self.label_end2=Label(self,text="end slice2 number")
        self.label_end2.grid(row=12,column=0)
        # self.label_Wedge.pack()
        self.txt_end2 = Entry(self,width=50)
        self.txt_end2.insert(END,'80')
        self.txt_end2.grid(row=12,column=1)
        # self.btn_end=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_end.grid(row=9,column=2)
        ##############################################################
        self.label_flagDown=Label(self,text="counter down")
        self.label_flagDown.grid(row=13,column=0)
        # self.label_Wedge.pack()
        self.txt_flagDown = Entry(self,width=50)
        self.txt_flagDown.insert(END,'0')
        self.txt_flagDown.grid(row=13,column=1)
        # self.btn_end=Button(self,text="save",command=self.clicked)
        # #
        # self.btn_end.grid(row=9,column=2)
        ##############################################################


        self.btn_execute=Button(self,text="execute",command=self.clicked2)
        #
        self.btn_execute.grid(row=14,column=0)
        ##################################################################
        self.btn_execute2=Button(self,text="execute_multiple",command=self.clicked22)
        #
        self.btn_execute2.grid(row=15,column=0)
        ##################################################################
        self.btn_exit=Button(self,text="exit",command=self.Exit_clicked)
        #
        self.btn_exit.grid(row=16,column=1)
        ######################################################################
        self.btn_vis=Button(self,text="Visualize",command=self.vis_clicked)
        #
        self.btn_vis.grid(row=17,column=1)
        ######################################################################
        # self.btn_con=Button(self,text="continue",command=self.con_clicked)
        # #
        # self.btn_con.grid(row=11,column=0)
        ######################################################################


    #     # creating a menu instance
    #     menu = Menu(self.master)
    #     self.master.config(menu=menu)
    #
    #     # create the file object)
    #     file = Menu(menu)
    #
    #     # adds a command to the menu option, calling it exit, and the
    #     # command it runs on event is client_exit
    #     file.add_command(label="Exit", command=self.client_exit)
    #
    #     #added "file" to our menu
    #     menu.add_cascade(label="File", menu=file)
    #
    #     # create the file object)
    #     edit = Menu(menu)
    #
    #     # adds a command to the menu option, calling it exit, and the
    #     # command it runs on event is client_exit
    #     edit.add_command(label="Undo")
    #
    #     #added "file" to our menu
    #     menu.add_cascade(label="Edit", menu=edit)
    #
    #
    # def client_exit(self):
    #     exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("500x500")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()
