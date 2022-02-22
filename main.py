from weatheranalyzer import WeatherAnalyzer
def main():
    #This gives the menu bar
    running=True #Loop ensures menu bar keeps on appearing ready for user input until '11' is typed
    while running:
        print('               ') #Spaces and * printed for better readablity in terminal output
        print('******************************************************')
        print('               ')
        print('1-  Get Minimum Temperature of 1990-2019')
        print('2-  Get Maximum Temperature of 1990-2019')
        print('3-  Get Minimum Temperature of 1990-2019 Annually')
        print('4-  Get Maximum Temperature of 1990-2019 Annually')
        print('5-  Get Average Snowfall between 1990-2019 Annually')
        print('6-  Get Average Temperature between 1990-2019 Annually')
        print('7-  LineChart Minimum Temperature of 1990-2019 Annually')
        print('8-  LineChart Maximum Temperature of 1990-2019 Annually')
        print('9-  BarChart Average Snowfall between 1990-2019 Annually')
        print('10- BarChart Average Temperature between 1990-2019 Annually')
        print('11- Exit Program')
        print('               ')
        try:
            choice = int(input('Please choose between 1-11 from menu above:'))
            print('               ')
            a1= WeatherAnalyzer() #Instantiating WeatherAnalyzer class and calling each method based on choice
            
            if choice == 1:
                a1.get_min_temp()
            elif choice == 2:
                a1.get_max_temp()
            elif choice == 3:
                a1.get_min_temp_annual()
            elif choice == 4:
                a1.get_max_temp_annual()
            elif choice == 5:
                a1.get_avg_snowfall_annual()
            elif choice == 6:
                a1.get_avg_temp_annual()
            elif choice == 7:
                a1.linechart_min_temp_annual()
            elif choice == 8:
                a1.linechart_max_temp_annual()
            elif choice == 9:
                a1.barchart_avg_snow_annual()
            elif choice == 10:
                a1.barchart_avg_temp_annual()
            elif choice == 11:
                running = False 
            else:
                raise ValueError
        except ValueError:
            print('Invalid selection,try again')
                
if __name__=="__main__":
    main()