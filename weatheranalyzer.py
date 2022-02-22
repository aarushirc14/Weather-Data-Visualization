import numpy as np
from fileio import FileIO
from tempdata import TemperatureData
from date import Date
from chart import Chart

class WeatherAnalyzer(object):

    #instansiating FileIO Object
    fObj = FileIO('CalgaryWeather.csv')         
    data = fObj.read_weather()
    tdList = [] #tempdata list = empty array
    global year_start
    year_start = int(data.min(axis=0)[0]) #Global variables- data.min(axis=0)[0] gives 1990 and data.max(axis=0)[0] gives 2019
    global year_end                        #These variables were made instead of writing '1990' and '2019' so code is reusable with other data sets
    year_end = int(data.max(axis=0)[0])
    
    #creating list of TemperatureData object
    def create_tempdata_list(self,counter_start,counter_end):
        self.tdList = []
        for row in range (counter_start,counter_end):
            #instansiating Date Object
            dateObj = Date(self.data[row,0],self.data[row,1])
            #instantiating TemperatureData object with date object
            tdObj = TemperatureData(dateObj,self.data[row,2],self.data[row,3],self.data[row,4])
            self.tdList.append(tdObj)
        return self.tdList
    #Every 12 objects are made into a list
        

    def get_min_temp(self):
        print("Minimum Temperature of 1990-2019 is",self.data.min(axis=0)[3]) #finding overall of min of column 4 in excel sheet
    
    def get_max_temp(self):
        print ("Maximum Temperature of 1990-2019 is",self.data.max(axis=0)[2]) #finding overall of max of column 3 in excel sheet

    
    def get_min_temp_annual(self):
        list1=[]# calling returned value of td.List
        month_start=0
        month_end=12
        year_array = []
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1= 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            min_temp_array= []#creating a new 1-D array from list1 and taking just the min temp column of a particular year
            year_array.append(year)
            for i in range (0,12):
                min_temp_array.append(list1[i].minTemp) #Finding the lowest value in the min temp column of a particular year and appending to an array with a single value
                min_temp_annual= min(min_temp_array)
           
            print("Minimum Temperature of",year,"is",min_temp_annual) #printing the single value
            month_start=month_start+12 #updating months to move to the next year
            month_end=month_end+12
            
                
    
    def linechart_min_temp_annual (self):
        list1=[] # calling returned value of td.List
        month_start=0 
        month_end=12
        min_temp_allvalues_array= []#empty array to hold all data for this section for graph
        year_array = []
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1 = 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            min_temp_array= [] #creating a new 1-D array from list1 and taking just the min temp column of a particular year
            year_array.append(year)
            for i in range (0,12):
                min_temp_array.append(list1[i].minTemp) #Finding the highest value in the min temp column of a particular year and appending to an array with a single value
                min_temp_annual= min(min_temp_array)
            min_temp_allvalues_array.append(min_temp_annual) #Appending data to empty allvalues array for graph
            month_start=month_start+12  #updating months to move to the next year
            month_end=month_end+12

        chartObj = Chart() #Instantiating chart class
        chartObj.drawLineChart(year_array,min_temp_allvalues_array,"Minimum Temperature of 1990-2019 Annually", "Years", "Temperature") #giving values to drawLineChart objects
                                #    'x'         'y'                         'title'                             'xlabel'    'ylabel'
    
    def get_max_temp_annual(self):
        list1=[] # calling returned value of td.List
        month_start=0 
        month_end=12
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1 = 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            max_temp_array= [] #creating a new 1-D array from list1 and taking just the max temp column of a particular year
            for i in range (0,12):
                max_temp_array.append(list1[i].maxTemp) #Finding the highest value in the max temp column of a particular year and appending to an array with a single value
                max_temp_annual= max(max_temp_array)
            print("Maximum Temperature of",year,"is",max_temp_annual) #printing the single value
            month_start=month_start+12
            month_end=month_end+12  #updating months to move to the next year
            
    def linechart_max_temp_annual (self):
        list1=[] # calling returned value of td.List
        month_start=0 
        month_end=12
        max_temp_allvalues_array= []#empty array to hold all data for this section for graph
        year_array = []
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1 = 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            max_temp_array= [] #creating a new 1-D array from list1 and taking just the max temp column of a particular year
            year_array.append(year)
            for i in range (0,12):
                max_temp_array.append(list1[i].maxTemp) #Finding the highest value in the max temp column of a particular year and appending to an array with a single value
                max_temp_annual= max(max_temp_array)
            max_temp_allvalues_array.append(max_temp_annual) #Appending data to empty allvalues array for graph
            month_start=month_start+12
            month_end=month_end+12 #updating months to move to the next year

        chartObj = Chart() #Instantiating chart class
        chartObj.drawLineChart(year_array,max_temp_allvalues_array,"Maximum Temperature of 1990-2019 Annually", "Years", "Temperature") #giving values to drawLineChart objects
                                   # 'x'           'y'                             'title'                       'xlabel'    'ylabel'
    
    def get_avg_snowfall_annual(self): 
        list1=[] #calling returned value of td.List
        month_start=0
        month_end=12
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1= 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            avg_snow_array= [] #creating a new 1-D array from list1 and taking just the snow column of a particular year
            for i in range (0,12):
                avg_snow_array.append(list1[i].snowFall) #Finding the average value in the snow column of a particular year and appending to an array with a single value
                avg_snow_annual= round(np.mean(avg_snow_array),2)
            print("Average annual snowfall of",year,"is",avg_snow_annual) #printing the single value
            month_start=month_start+12 #updating months to move to the next year
            month_end=month_end+12

    def barchart_avg_snow_annual (self):
        list1=[] # calling returned value of td.List
        month_start=0 
        month_end=12
        avg_snow_allvalues_array= [] #empty array to hold all data for this section for graph
        year_array = []
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1 = 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            avg_snow_array= [] #creating a new 1-D array from list1 and taking just the snow column of a particular year
            year_array.append(year)
            for i in range (0,12):
                avg_snow_array.append(list1[i].snowFall) #Finding the average value of the snow column of a particular year and appending to an array with a single value
                avg_snow_annual= round(np.mean(avg_snow_array),2)
            avg_snow_allvalues_array.append(avg_snow_annual) #Appending data to empty allvalues array for graph
            month_start=month_start+12 #updating months to move to the next year
            month_end=month_end+12

        chartObj = Chart() #Instantiating chart class
        chartObj.drawBarChart(year_array,avg_snow_allvalues_array,"Average Snowfall between 1990-2019 Annually", "Years", "Snowfall") #giving values to drawBarChart objects
                                #'x'           'y'                             'title'                           'xlabel'    'ylabel'
    
    def get_avg_temp_annual(self):
        list1=[] #calling returned value of td.List
        month_start=0
        month_end=12

        for year in range (year_start,year_end+1):#year_start = 1990, year_end + 1= 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            avg_temp_annual_array = [] #empty array for avgtemp
            for i in range (0,12):
                mon_avg_temp= (list1[i].maxTemp + list1[i].minTemp)/2 #finding monthly avgs (mintemp+maxtemp/2)
                avg_temp_annual_array.append(mon_avg_temp)#put monthly avgs into avgtemp array
            
            avg_temp_annual = round(np.mean(avg_temp_annual_array),2) #calc mean of avgtemp array for annual avg
            print("Average annual temperature of",year,"is",avg_temp_annual)
            month_start = month_start +12
            month_end=month_end+12 #updating months to move to the next year

    def barchart_avg_temp_annual (self):
        list1=[] #calling returned value of td.List
        month_start=0
        month_end=12
        avg_temp_allvalues_array= [] #empty array to hold all data for this section for graph
        year_array = []
        
        for year in range (year_start,year_end+1): #year_start = 1990, year_end + 1 = 2019 (+1 ensures value of 2019 is printed)
            list1 = self.create_tempdata_list(month_start,month_end)
            avg_temp_annual_array = [] #empty array for avgtemp
            year_array.append(year)
            for i in range (0,12):
                mon_avg_temp= (list1[i].maxTemp + list1[i].minTemp)/2 #finding monthly avgs (mintemp+maxtemp/2)
                avg_temp_annual_array.append(mon_avg_temp) #put monthly avgs onto avgtemp array
            
            avg_temp_annual = round(np.mean(avg_temp_annual_array),2) #calc mean of avgtemp array for annual avg
            avg_temp_allvalues_array.append(avg_temp_annual)  #Appending data to empty allvalues array for graph
            month_start = month_start+12 #updating months to move to the next year
            month_end=month_end+12
    
        chartObj = Chart() #Instantiating chart class
        chartObj.drawBarChart(year_array,avg_temp_allvalues_array,"Average Temperature between 1990-2019 Annually", "Years", "Temperature") #giving values to drawLineChart objects
                                #'x'           'y'                             'title'                               'xlabel'    'ylabel'




