# ECE-143-Group-10
Global Warming (Climate Change) in United States

1. Introduction
    
    This project is mainly focus on analyzing the climate change of several cities in 
    the United States by data visualiztion.
 
2. File Description

    1. Folders
        1. './data/'
            
            This folder is to store the original data scraped from the website and also
            the cleaned data generated from the code.
         
        2. './pics/'
            
            This folder is the place to store all the plots generated from the jupyter-notebook
            code.
        
    2. Python Files
        1. data_cleaner.py
            
            Select specified columns of origin data and auto-fill the missing data.
            
        2. data_crawler.py
            
            Crawling web pages, parsing and fetching table data and storing them in csv files.
            
        3. data_generator.py
            
            The integration of data gathering and cleaning.
            
        4. data_processor.py
        
            Helper functions for data visualization. (eg. get monthly start & end, get the 
            weather info of a specific type)
            
        5. global_variables.py
        
            Global variables. Including the columns information
            
        6. plot_generator.py
           
            To batchly generate images.
     
     3. Jupyter Notebook Files
     
        1. Data Visualization.ipynb
        
            Integrated data visualization code
            
        1. data_visualization_precipitation.ipynb
            
            Visualization and plotting precipitation data of a single city and all cities's comparison.
            
        2. data_visualization_temperature.ipynb
        
            Visualization and plotting temperature data of a single city and all cities's comparison.
        
        3. data_visualization_weather.ipynb
        
            Visualization and plotting weather data of a single city and all cities's comparison.
            
        4. others
            
            Some historical code and demo.

    4. Text and .csv Files
        
        City name and their corresponding code reference.
        
    5. PPT (.pdf)
        
        Presentation ppt.
        
3. Links

    [Underground weather](https://www.wunderground.com/history/daily/us/ca/san-diego/KSAN/date/2019-4-30)
    
    [Project's GitHub](https://github.com/WFighter909/ECE-143-Group-10)