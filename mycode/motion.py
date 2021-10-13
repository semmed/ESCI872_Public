import os
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from numpy import pi, cos, sin, log, exp
import numpy as np

# 7.0: Creating Classes
class Motion:
    """A Class for handling Motion Data"""

    # 7.0.0 Class Initialization and Attributes
    def __init__(self):
        pass # Remove this once adding code)
        
    # 7.0.1 The String Representation Method
#     def __str__(self):                               ##Uncomment this once you are working on step 7.0.1
#         pass # Remove this once adding code)
    
    # 7.8.0 Creating a Read Method for the Motion Class
    def read_jhc_file(self, fullpath):
        pass # Remove this once adding code)
        
            
    # 7.9 Creating a Draw Method for the Motion Class
    def draw(self):
        pass # Remove this once adding code)
        
        # 7.9.0 Defining the plot area
                
        # 7.9.1 Creating subplots
        
        # 7.9.2 Plot the Data
                
        # 7.9.3 Labeling the Axes
        
        #Last thing to do
        plt.show()
        
    # 7.11 Getting Motion Data as a Vector for a Specific Epoch
    def get_motion(self, time = datetime.fromtimestamp(0, timezone.utc)):
        pass # Remove this once adding code)
        # 7.10.1 Allocating Memory
                
        # 7.10.2 Map the Input Times to POSIX Times
        
        # 7.10.3 Linearly Interpolate the Motion Data
         
    
    # 7.11 Getting Motion Data as a Rotation Matrix for a Specific Epoch
    def get_rotation_matrix(self, time = datetime.fromtimestamp(0, timezone.utc)):
        pass
        # 7.11.1 Determining the Attitude

        #  7.11.2 Creating the Axes Rotation Matrices

        #  7.11.3 Creating Rotation Matrix
    
    def geo_reference_la(self, time = datetime.fromtimestamp(0, timezone.utc), la = np.array([[0],[0],[0]])):
        pass # Remove this once adding code)
        # 7.12.0 Getting the Attitude
        
        # 7.12.1 Obtaining the Lever Arm in Geo-Referenced Space

        

