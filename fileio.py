import numpy as np

class FileIO:
  def __init__(self,fileName):
    self.fileName = fileName
    
  def read_weather(self):
    data = np.loadtxt(self.fileName,delimiter=',',skiprows=1,usecols=(0,1,2,3,4), dtype=np.float) # numpy loadtxt loads data from a text file,
    return data                                                                                   #each row in text file must have the same number of values

#Reading contents of excel sheet and storing it in 'data'.