***P06 – Hadoop Map-Reduce

Team members: Shashank Tiruvaipati, 
		   Laxmi Sai Teja Naraharasetty

***Summary: Our MR project is mainly based on extracting the maximum and minimum acceptance of H1-B visas in the year 2016.

***Data source in detail:
	We have chosen H1-B visa petitions data set for the years 2015 and 2016 which consists of status of the case, employer’s name, job title, etc.
	Our data source contains 469 Mega Bytes of data with more than 1,000,000 records. The file extension is .csv(Excel). The format of dataset is structured.
Volume is the main big data problem for this data set.

Volume: Volume of the data set is 469 Mb. There are over 1,000,000 records.

Variety: It is a structured data stored in excel file with .csv extension.

Velocity: Data is between 2015 and 2016.

***Tools and Technologies required: 
	Python
	Notepad / Notepad++
	
***Map Reduce Problems:

MR1: To find which professional background has maximum acceptance for the year 2016

MR2: To find which professional background has minimum acceptance for the year 2016

***Mapper Input: (Sample data is stored in SampleH1.txt)

     JOB_TITLE                                               YEAR

    CHIEF OPERATING OFFICER               		          2016

***Mapper output/Reducer Input:  Mapper function will produce the Intermediate key values pairs. The format is shown below.

![mapper](https://cloud.githubusercontent.com/assets/22079691/25056196/e5c6a3f6-212c-11e7-8e1b-bc65e84436b5.JPG)
		

***Reducer Output:  Reducer will produce the following sample output and the output is stored in output.txt file.

      
 ![reducer](https://cloud.githubusercontent.com/assets/22079691/25056200/e9e9d2dc-212c-11e7-80f5-0866b270e50e.JPG)

***Language used: Python.

***Processing: We will be processing both text & numeric and we have selected first 10,000 lines of data from the original dataset because of the huge data and time complexity while processing it.

***Pulling the repo:
==> Open the project folder in windows(local)
==> Right click anywhere on the screen and select “Open command window here as administrator”
==> Then type the following statement
	$ git clone https://github.com/Shashank7T/DDIS---P12---H1B.git

***Executing the code:
==> Open the project folder in windows(local).
==> Right click anywhere on the screen and select “Open command window here as administrator”
==> Type python
==> Then type the following commands as follows:

		>>>execfile("mapper.py")
		>>>execfile("reducer.py")

***Graphical representation for highest acceptace of H1-B visas for the year 2016
![shashank graph](https://cloud.githubusercontent.com/assets/22079691/25055592/58b060d6-2129-11e7-99f6-29687c6806e8.JPG)


***Graphical representation for lowest acceptace of H1-B visas for the year 2016
![teja graph](https://cloud.githubusercontent.com/assets/22079691/25055630/941f2e04-2129-11e7-925b-70cae0466993.JPG)


***Resources:
	http://kbroman.org/github_tutorial/pages/init.html

