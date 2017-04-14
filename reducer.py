sorted = open("jobsort.txt","r")     
results = open("output.txt", "w")   

CASE_STATUS = 0        
JOB_TITLE = None    
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisjob, thisCase = datalist  # read into variables
    if JOB_TITLE and JOB_TITLE != thisjob:        
        results.write("{0}\t{1}\n".format(JOB_TITLE, CASE_STATUS))
        JOB_TITLE = thisjob;
        CASE_STATUS = 0

    JOB_TITLE = thisjob        
    CASE_STATUS += 1   

if JOB_TITLE != None: 
    results.write("{0}\t{1}\n".format(JOB_TITLE, CASE_STATUS))

sorted.close() 
results.close() 