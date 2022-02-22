from date import Date

class TemperatureData:
    def __init__(self, date, maxTemp,minTemp,snowFall ):
        self.date=date 
        self.maxTemp=maxTemp
        self.minTemp=minTemp
        self.snowFall=snowFall

#Single row in excel sheet represents a TemperatureData class which includes a Date class.
