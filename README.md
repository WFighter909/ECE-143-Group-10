# ECE-143-Group-10
## Global Warming (Climate Change) in United States

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
            
        4. others
            
            Some historical code and demo.

    4. Text and .csv Files
        
        City name and their corresponding code reference.
        
    5. PPT (.pdf)
        
        Presentation ppt.

3. Libraries Dependency

    numpy, pandas, seaborn, matplotlib
4. Reuse Code Guideline

    1. Find the city code in the reference or on the website's url (4 character string,usually start with 'K')
    
    2. Use the data_crawler.py, change the parameters: start_date, end_data and city to generate generate a .csv file
    containing all original data
    
    3. Get to the data_cleaner.py, specify the .csv file name to generated the cleaned data. (will create a new 
    .csv file from xxx.csv to xxx_cleaned.csv)
    
    4. Use the Jupyter-notebook to generate all the plots. Also, you can use plot_generator.py (which is just a for 
    loop wrapper function) to generate plots by year/month wise. (remember to change the parameters)
    
    5. Note: 
 
        1. The selected columns, the color of the weather representation can be modified in the global_variables.py
        
        2. data_generator.py 's main function has been comment, it just a example of combing the collecting and cleaning
        process, and also to generate all cities' cleaned data at once in a for-loop  

    
4.  Relative Links

    [Underground weather](https://www.wunderground.com/history/daily/us/ca/san-diego/KSAN/date/2019-4-30)
    
    [Project's GitHub](https://github.com/WFighter909/ECE-143-Group-10)