import numpy as np
import cv2
#options
Verbose=1
Wedge=20
Wline=2
Alpha=0.2
Beta=0.2
Mu=0.2
Giteration=200
Sigma2=1
Kappa=0.5
Delta=0.1000
Gamma=1
Iterations=20
Sigma1=2
# Sigma2=2
Lambda=0.8

#P_=[]
Fext1=[]
Fext2=[]
def create_A(a, b, N):
    """
    a: float
    alpha parameter
    b: float
    beta parameter
    N: int
    N is the number of points sampled on the snake curve: (x(p_i), y(p_i)), i=0,...,N-1
    """
    row = np.r_[
        -2*a - 6*b,
        a + 4*b,
        -b,
        np.zeros(N-5),
        -b,
        a + 4*b
    ]
    A = np.zeros((N,N))
    for i in range(N):
        A[i] = np.roll(row, i)
    return A

def external_energy( I,smoothed,Wline, Wedge, Wterm,Sigma ):
    """
    Given an image, returns 2 functions, fx & fy, that compute
    the gradient of the external edge force in the x and y directions.
    img: ndarray
        The image.
    """

    # Gaussian smoothing.
    # smoothed = filt.gaussian_filter( (img-img.min()) / (img.max()-img.min()), sigma )
    # Gradient of the image in x and y directions.
    gix=cv2.Sobel(smoothed,cv2.CV_64F,1,0,ksize=5)
    giy=cv2.Sobel(smoothed,cv2.CV_64F,0,1,ksize=5)

    #giy, gix = np.gradient( smoothed )
    # Gradient magnitude of the image.
    gmi = (gix**2 + giy**2)**(0.5)
    # Normalize. This is crucial (empirical observation).
    gmi = (gmi - gmi.min()) / (gmi.max() - gmi.min())
    eedge=-gmi
    eline=smoothed
    # %masks for taking various derivatives
    # m1 = np.array([-1,1])
    # m2 = np.array(np.mat('1;-1'))
    # m3 = np.array([1,-2,1])
    # m4 = np.array(np.mat('1;-2;1'))
    # m5 = np.array(np.mat('1,-1;-1,1'))
    cx=cv2.Sobel(smoothed,cv2.CV_64F,1,0,ksize=5)
    cy=cv2.Sobel(smoothed,cv2.CV_64F,0,1,ksize=5)
    cxx=cv2.Sobel(cx,cv2.CV_64F,1,0,ksize=5)
    cyy=cv2.Sobel(cy,cv2.CV_64F,0,1,ksize=5)
    cyx=cv2.Sobel(cy,cv2.CV_64F,1,0,ksize=5)
    cxy=cv2.Sobel(cx,cv2.CV_64F,0,1,ksize=5)

    eterm = (np.multiply(cyy,np.multiply(cx,cx)) -[2*i for i in  np.multiply(cxy,np.multiply(cx,cy))] + np.multiply(cxx,np.multiply(cy,cy)))/(np.power(1+(np.multiply(cx,cx) + np.multiply(cy,cy)),1.5))
    E1=[[x*Wline for x in y] for y in eline]
    E2=[[x*Wedge for x in y] for y in eedge]
    E3=[[x*Wterm for x in y] for y in eterm]
    E4=np.subtract(E1,E2)
    E5=np.subtract(E4,E3)
    Eextern= E5

    ggmix=cv2.Sobel(Eextern,cv2.CV_64F,1,0,ksize=5)
    ggmiy=cv2.Sobel(Eextern,cv2.CV_64F,0,1,ksize=5)
    #ggmix,ggmiy=np.gradient(Eextern)

    #  #Make the external force (flow) field.
    # Fx=ggmix
    # Fy=ggmiy
    #
    # Fext1=-np.multiply(np.multiply(Fx,2),np.power(Sigma2,2));
    # Fext2=-np.multiply(np.multiply(Fy,2),np.power(Sigma2,2));
    # #Squared magnitude of force field
    # Fx= Fext1
    # Fy= Fext2
    #
    # #Calculate magnitude
    # sMag = np.power(Fx,2)+ np.power(Fy,2)
    #
    # # Set new vector-field to initial field
    # u=Fx;
    # v=Fy;
    #
    # #Iteratively perform the Gradient Vector Flow (GVF)
    # for i in range(Giteration):
    #   # % Calculate Laplacian
    #   ux=cv2.Sobel(u,cv2.CV_64F,1,0,ksize=5)
    #   uy=cv2.Sobel(u,cv2.CV_64F,0,1,ksize=5)
    #   Uxx=cv2.Sobel(ux,cv2.CV_64F,1,0,ksize=5)
    #   Uyy=cv2.Sobel(uy,cv2.CV_64F,0,1,ksize=5)
    #
    #   # Vxx=ImageDerivatives2D(v,Sigma,'xx');
    #   # Vyy=ImageDerivatives2D(v,Sigma,'yy');
    #   vx=cv2.Sobel(v,cv2.CV_64F,1,0,ksize=5)
    #   vy=cv2.Sobel(v,cv2.CV_64F,0,1,ksize=5)
    #   Vxx=cv2.Sobel(vx,cv2.CV_64F,1,0,ksize=5)
    #   Vyy=cv2.Sobel(vy,cv2.CV_64F,0,1,ksize=5)
    #
    #   # % Update the vector field
    #   u = u + np.multiply(Mu,(np.add(Uxx,Uyy))) - np.multiply(sMag,np.subtract(u,Fx));
    #   v = v + np.multiply(Mu,np.add(Vxx,Vyy)) - np.multiply(sMag,np.subtract(v,Fy));
    #
    #
    # Fext1 = u;
    # Fext2 = v;
    # ggmix=Fext1
    # ggmiy=Fext2


    def fx(x, y):
        """
        Return external edge force in the x direction.
        x: ndarray
            numpy array of floats.
        y: ndarray:
            numpy array of floats.
        """
        # Check bounds.
        x[ x < 0 ] = 0.
        y[ y < 0 ] = 0.

        x[ x > I.shape[1]-1 ] = I.shape[1]-1
        y[ y > I.shape[0]-1 ] = I.shape[0]-1

        return ggmix[ (y.round().astype(int), x.round().astype(int)) ]

    def fy(x, y):
        """
        Return external edge force in the y direction.
        x: ndarray
            numpy array of floats.
        y: ndarray:
            numpy array of floats.
        """
        # Check bounds.
        x[ x < 0 ] = 0.
        y[ y < 0 ] = 0.

        x[ x > I.shape[1]-1 ] = I.shape[1]-1
        y[ y > I.shape[0]-1 ] = I.shape[0]-1

        return ggmiy[ (y.round().astype(int), x.round().astype(int)) ]

    return fx, fy

def iterate_snake(x, y, a, b, fx, fy, gamma=0.1, n_iters=10, return_all=True):
    """
    x: ndarray
        intial x coordinates of the snake
    y: ndarray
        initial y coordinates of the snake
    a: float
        alpha parameter
    b: float
        beta parameter
    fx: callable
        partial derivative of first coordinate of external energy function. This is the first element of the gradient of the external energy.
    fy: callable
        see fx.
    gamma: float
        step size of the iteration

    n_iters: int
        number of times to iterate the snake
    return_all: bool
        if True, a list of (x,y) coords are returned corresponding to each iteration.
        if False, the (x,y) coords of the last iteration are returned.
    """
    A = create_A(a,b,x.shape[0])
    B = np.linalg.inv(np.eye(x.shape[0]) - gamma*A)
    P_=np.zeros((2,x.size))
    if return_all:
        snakes = []

    for i in range(n_iters):
        x_ = np.dot(B, x + gamma*fx(x,y))
        y_ = np.dot(B, y + gamma*fy(x,y))
        x, y = x_.copy(), y_.copy()
        # P_[0]=x_
        # P_[1]=y_
        # XP,YP=np.gradient(P_)
        # dx = -(np.linalg.norm(XP))
        # dy = -(np.linalg.norm(YP))
        #
        # x += 0.1*dx
        # y += 0.1*dy
        # dx=x_-x
        # dy=y_-y
        # x+=dx
        # y+=dy
        if return_all:
            snakes.append( (x,y) )

    if return_all:
        return snakes
    else:
        return (x,y)

