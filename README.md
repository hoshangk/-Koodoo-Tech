# -Koodoo-Tech

Purpose of this script is to extract the "Top Stories" data from the Link (url) provided.

# Language Used : 
Python 3.7

# Libraries Used : -
beautifulsoup4==4.10.0
bs4==0.0.1
certifi==2021.5.30
charset-normalizer==2.0.6
idna==3.2
lxml==4.6.3
requests==2.26.0
soupsieve==2.2.1
urllib3==1.26.7

# Steps to Be Followed : -
Step 1: -
    Create a Python project in any of the Editor.
    
Step 2: -
    Run Command 
          pip install -r /path/to/requirements.txt
          
    This Will install all the required libraries which are required to get the output.
    
    Note :- Please Save the Requirement.txt inside the project folder to access its relative path easily
    
 Step 3: -
    Run the "readData.py" file
    
 # Output : -
 It will generate 3 files
 1. Log File  - script.log    - This file will contain all the logs which may required to backtrace in terms of any failure
 2. top_stories_only_headers.csv - As per requirement, this file will contain all the top soties headlies in the form of csv file.
 3. top_stories_all_data.csv  - This file will contain some more data like pubDate corresponding to the top Story.


