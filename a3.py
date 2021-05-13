import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()


class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        # Initialized four lists for storing coordinates of corners:
        # 1. xi = initial x coordinates
        # 2. xi = initial y coordinates
        # 3. xo = final x coordinates
        # 4. yo = final y coordinates
        self.xi = []
        self.yi = []
        for i in range(len(A)):
            self.xi.append(A[i][0])
            self.yi.append(A[i][1])
        self.xo = self.xi
        self.yo = self.yi
        
        # Initialized four instance var for storing coordinates of centres:
        # 1. cxi = initial x coordinates of centre
        # 2. cxi = initial y coordinates of centre
        # 3. cxo = final x coordinates of centre
        # 4. cyo = final y coordinates of centre
        self.cxi = sum(self.xi)/len(self.xi)
        self.cyi = sum(self.yi)/len(self.yi)
        self.cxo = self.cxi
        self.cyo = self.cyi
        
 
    
    def translate(self, dx, dy=None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        if dy == None:
            dy = dx

        # Calling translate() of Shape class which sets T_t matrix
        super().translate(dx, dy)
        
        # Storing previous coordinates as initial coordinates
        self.xi = self.xo[:]
        self.yi = self.yo[:]
        self.cxi = self.cxo
        self.cyi = self.cyo
        
        # ***Updating final coordinates by carrying out transformation***
        # Translate - Multiplication of T_t matrix with coordinates matrix [x, y, 1] 
        
        # Setting centre of poygon
        self.cxo, self.cyo, l = np.dot(self.T_t, np.array([self.cxo, self.cyo, 1]))  
        
        # Setting corners of poygon
        for i in range(len(self.xi)):
            self.xo[i], self.yo[i], l = np.dot(self.T_t, [self.xi[i], self.yi[i], 1])
            
        # return [ round(elem, 2) for elem in self.xo ], [ round(elem, 2) for elem in self.yo ]
        return list(np.around(np.array(self.xo),2)), list(np.around(np.array(self.yo),2))

    
    def scale(self, sx, sy=None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        if sy == None:
            sy = sx
            
        # Calling scale() of Shape class which sets T_s matrix
        super().scale(sx, sy)

        # Storing previous coordinates in different var
        storedxi = self.xo[:]
        storedyi = self.yo[:]
        storedcxi = self.cxo
        storedcyi = self.cyo
        
        # ***Updating final coordinates by carrying out transformation***
        # Translate the figure to Origin wrt to centre of polygon 
        self.xo, self.yo = self.translate(-self.cxo, -self.cyo)
        
        # Scale the polygon by multiplying T_s matrix with [x, y, 1]  
        for i in range(len(self.xo)):
            self.xo[i], self.yo[i], l = np.dot(self.T_s, np.array([self.xo[i],self.yo[i], 1]))       

        # Translate the polygon back to initial centre coordinates  
        self.xo, self.yo = self.translate(storedcxi, storedcyi)
        
        # Setting previous coordinates as initial coordinates using stored var
        self.xi = storedxi
        self.yi = storedyi
        self.cxi = storedcxi
        self.cyi = storedcyi
        
        return list(np.around(np.array(self.xo),2)), list(np.around(np.array(self.yo),2))
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        # Calling rotate() of Shape class which sets T_r matrix
        super().rotate(deg)

        # Storing previous coordinates in different var
        storedxi = self.xo[:]
        storedyi = self.yo[:]
        storedcxi = self.cxo
        storedcyi = self.cyo
        
        # ***Updating final coordinates by carrying out transformation***
        # Rotate the polygon by multiplying T_r matrix with [x, y, 1]
          
        # Set m and n for finding the amount of shift in rotation wrt to rx, ry (point of rotation) 
        m, n, l = np.dot(self.T_r, np.array([rx, ry, 1]))       

        # Setting final coordinates by multiplication with T_r and adding shift of rotation, m and n
        for i in range(len(self.xo)):
            self.xo[i], self.yo[i], l = np.dot(self.T_r, np.array([self.xo[i], self.yo[i], 1]))       
            self.xo[i] += rx-m
            self.yo[i] += ry-n
            
        # Setting centre coordinates by multiplication with T_r and adding shift of rotation, m and n
        self.cxo, self.cyo, l = np.dot(self.T_r, np.array([self.cxo, self.cyo, 1]))       
        self.cxo += rx-m
        self.cyo += ry-n
        
        # Setting previous coordinates as initial coordinates using stored var
        self.xi = storedxi
        self.yi = storedyi
        self.cxi = storedcxi
        self.cyi = storedcyi       
        
        return list(np.around(np.array(self.xo),2)), list(np.around(np.array(self.yo),2))
    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        
        # Initialize the plt.plot() method for plotting the initial polygon before transformation 
        plt.plot(np.append(self.xi, self.xi[0]), np.append(self.yi, self.yi[0]), color = "black", linestyle = 'dashed')

        # Initialize the plt.plot() method for plotting the final polygon after transformation 
        plt.plot(np.append(self.xo, self.xo[0]), np.append(self.yo, self.yo[0]), color = "black")

        # Setting dimensions of plot as r  and passing it in params of super class plot()
        r = max(max(list(map(abs,self.xo))), max(list(map(abs,self.xi))), max(list(map(abs,self.yi))), max(list(map(abs,self.yo))))

        # Calling plot() of the Shape class which plots the polygons
        super().plot(r, r)


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        # Initialized three vars for storing initial x, y coordinates of centre and radius
        self.xi = x
        self.yi = y
        self.radiusi = radius
        
        # Initialized three vars for storing final x, y coordinates of centre and radius
        self.xo = self.xi
        self.yo = self.yi
        self.radiuso = self.radiusi

    
    def translate(self, dx, dy=None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        if dy == None:
            dy = dx
            
        # Calling translate() of Shape class which sets T_t matrix
        super().translate(dx, dy)
        
        # Storing previous coordinates and radius as initial coordinates and initial radius
        self.xi = self.xo
        self.yi = self.yo
        self.radiusi = self.radiuso

        # ***Updating final coordinates by carrying out transformation***
        # Translate - Multiplication of T_t matrix with coordinates matrix [x, y, 1]
        self.xo, self.yo, l = np.dot(self.T_t, np.array([self.xo,self.yo, 1]))     
          
        return round(self.xo, 2), round(self.yo, 2), round(self.radiuso, 2)
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        # Calling scale() of Shape class which sets T_s matrix
        super().scale(sx, sx)

        
        # Storing previous coordinates and radius as initial coordinates and initial radius
        self.xi = self.xo
        self.yi = self.yo
        self.radiusi = self.radiuso
        
        # ***Updating final coordinates by carrying out transformation***
        # Translate - Multiplication of T_s matrix with coordinates matrix [x, y, 1]
        # Centre remains unchanged
        # Radius gets scaled
        self.radiuso, ll, l = np.dot(self.T_s, np.array([self.radiuso, 1, 1]))     

        return round(self.xo, 2), round(self.yo, 2), round(self.radiuso, 2)
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        # Calling rotate() of Shape class which sets T_r matrix
        super().rotate(deg)

        # Storing previous coordinates and radius as initial coordinates and initial radius
        storedxo = self.xo
        storedyo = self.yo
        storedradiuso = self.radiuso
        
        # ***Updating final coordinates by carrying out transformation***
        # Rotate the polygon by multiplying T_r matrix with [x, y, 1]
          
        # Setting final coordinates by multiplication with T_r and adding shift of rotation, m and n
        self.xo, self.yo, l = np.dot(self.T_r, np.array([self.xo, self.yo, 1]))       

        # Set m and n for finding the amount of shift in rotation wrt to rx, ry (point of rotation) 
        m, n, l = np.dot(self.T_r, np.array([rx, ry, 1]))       
        self.xo += rx-m
        self.yo += ry-n
        
        self.xi = storedxo
        self.yi = storedyo
        self.radiusi = storedradiuso
        
        return round(self.xo, 2), round(self.yo, 2), round(self.radiuso, 2)
 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        # plot circle before transformation
        ci = plt.Circle((self.xi, self.yi), self.radiusi, fill=False, linestyle='dashed')
        # plot circle after transformation
        co = plt.Circle((self.xo, self.yo), self.radiuso, fill=False)

        # Initialize the plt plot() methods for plotting circles 
        ax = plt.gca()
        ax.cla()
        ax.add_patch(ci)
        ax.add_patch(co)
        
        # Setting dimensions of plot as r and passing it in params of super class plot()
        r = max(max(abs(self.xo)+self.radiuso, abs(self.xi)+self.radiusi), max(abs(self.yo)+self.radiuso, abs(self.yi)+self.radiusi))
        # Calling plot() of the Shape class which plots the circles
        super().plot(r, r)
        

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    # ******************* INPUTS: ***********************************
    # verbose -> testCases -> shapeType ->
    # [polygon] sides -> (x,y)*sides ->
    # [circle] x,y,radius ->
    # queries -> [R deg (rx) (ry), T dx (dy), S sx (sy) OR S sr, P]*queries

    # ******************* OUTPUTS: (For each query) ******************
    # updated a b r values
    # space separated x and y lists before transformation and then in the next line transformed x and y lists
    # If verbose = 1, after every transformation plot the previous and current state of shape
    
    try:
        while True:
            # Input - Verbose
            verbose = int(input("Enter 1 if you want to see plot also alongwith results (else 0): "))
            if verbose in [0,1]:
                break
            else:
                print("[Invalid Code] Please enter the Valid Entries as specified.")
        
        # Input -Testcases  
        testCases = int(input("Enter no. of test cases (must be integer): "))
        for i in range(testCases): 
            while True:  
                # Input - Shapetype 
                shapeType = int(input("Enter 0 for the polygon and 1 for Circle: "))
                if shapeType==0:
                    sides = int(input("Enter no. of sides (must be integer): "))
                    A=[]
                    print("Enter space-separated x, y")
                    # get coordinates
                    for j in range(sides):
                        corner = list(map(float, input(f"x{j+1} y{j+1} : ").split()))
                        A.append(corner)
                    # set polygon
                    myPolygon = Polygon(A)
                    break
                elif shapeType==1:
                    print("Enter space-separated x, y, radius")
                    # get centre and radius
                    x, y, radius = list(map(float, input("a b r : ").split()))
                    # set circle
                    myCircle = Circle(x, y, radius)
                    break
                else:
                    print("[Invalid Code] Please enter the Valid Entries as specified.")
                
            # Input no. of queries
            queries = int(input("Enter no. of queries (must be integer): "))
            print("Enter Query (brackets means optional): \n1) R deg (rx) (ry) \n2) T dx (dy) \n3) S sx (sy) \n4) P\n")
            for j in range(queries):
                getquery = input().split()
                
                # Do Transformation - Translate
                if getquery[0] == 'T':
                    if shapeType==1:
                        if len(getquery)==3:
                            myCircle.translate(float(getquery[1]), float(getquery[2]))  
                        else: 
                            myCircle.translate(float(getquery[1]))
                        print(round(myCircle.xi, 2), round(myCircle.yi, 2), round(myCircle.radiusi, 2))
                        print(round(myCircle.xo, 2), round(myCircle.yo, 2), round(myCircle.radiuso, 2))
                        if verbose==1:
                            myCircle.plot()
                    else:
                        if len(getquery)==3:
                            myPolygon.translate(float(getquery[1]), float(getquery[2]))  
                        else: 
                            myPolygon.translate(float(getquery[1]))
                        for k in range(len(myPolygon.xi)):
                            print(round(myPolygon.xi[k], 2), end = " ")
                        for k in range(len(myPolygon.yi)):
                            print(round(myPolygon.yi[k], 2), end = " ")
                        print()
                        for k in range(len(myPolygon.xo)):
                            print(round(myPolygon.xo[k], 2), end = " ")
                        for k in range(len(myPolygon.yo)):
                            print(round(myPolygon.yo[k], 2), end = " ")
                        print()
                        if verbose==1:
                            myPolygon.plot()
                    print()

                # Do Transformation - Rotate
                elif getquery[0] == 'R':
                    if shapeType==1:
                        if len(getquery)==4:
                            myCircle.rotate(float(getquery[1]), float(getquery[2]), float(getquery[3]))  
                        elif len(getquery)==3:
                            myCircle.rotate(float(getquery[1]), float(getquery[2]))  
                        else: 
                            myCircle.rotate(float(getquery[1]))
                        print(round(myCircle.xi, 2), round(myCircle.yi, 2), round(myCircle.radiusi, 2))
                        print(round(myCircle.xo, 2), round(myCircle.yo, 2), round(myCircle.radiuso, 2))
                        if verbose==1:
                            myCircle.plot()
                    else:
                        if len(getquery)==4:
                            myPolygon.rotate(float(getquery[1]), float(getquery[2]), float(getquery[3]))  
                        elif len(getquery)==3:
                            myPolygon.rotate(float(getquery[1]), float(getquery[2]))  
                        else: 
                            myPolygon.rotate(float(getquery[1]))
                        for k in range(len(myPolygon.xi)):
                            print(round(myPolygon.xi[k], 2), end = " ")
                        for k in range(len(myPolygon.yi)):
                            print(round(myPolygon.yi[k], 2), end = " ")
                        print()
                        for k in range(len(myPolygon.xo)):
                            print(round(myPolygon.xo[k], 2), end = " ")
                        for k in range(len(myPolygon.yo)):
                            print(round(myPolygon.yo[k], 2), end = " ")
                        print()
                        if verbose==1:
                            myPolygon.plot()
                    print()
                
                # Do Transformation - Scaling
                elif getquery[0] == 'S':
                    if shapeType==1:
                        myCircle.scale(float(getquery[1]))
                        print(round(myCircle.xi, 2), round(myCircle.yi, 2), round(myCircle.radiusi, 2))
                        print(round(myCircle.xo, 2), round(myCircle.yo, 2), round(myCircle.radiuso, 2))
                        if verbose==1:
                            myCircle.plot()
                    else:
                        if len(getquery)==3:
                            myPolygon.scale(float(getquery[1]), float(getquery[2]))  
                        else: 
                            myPolygon.scale(float(getquery[1]))
                        for k in range(len(myPolygon.xi)):
                            print(round(myPolygon.xi[k], 2), end = " ")
                        for k in range(len(myPolygon.yi)):
                            print(round(myPolygon.yi[k], 2), end = " ")
                        print()
                        for k in range(len(myPolygon.xo)):
                            print(round(myPolygon.xo[k], 2), end = " ")
                        for k in range(len(myPolygon.yo)):
                            print(round(myPolygon.yo[k], 2), end = " ")
                        print()
                        if verbose==1:
                            myPolygon.plot()
                    print()
               
                # Plot the shape  
                elif getquery[0] == 'P':
                    if shapeType==1:
                        myCircle.plot()
                    else:
                        myPolygon.plot()
                    print()
            
    except Exception as e:
        print("[Invalid Code] Please enter the Valid Entries as specified.")
        print(e)
        
    finally:
        print("Code Successfully Executed!")
# ************************** End Of Code ************************