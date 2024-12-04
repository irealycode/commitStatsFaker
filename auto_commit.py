import os                                                          
import random                                                      
from datetime import datetime, timedelta                           
                                                                   
fp = "test"                                                        
# start_date = datetime(datetime.now().year, 2, 17)                
num_coms = 150                                                     
                                                                   
for i in range(1, num_coms + 1):                                   
    randhour = random.randint(0,23)                                
    # comdate = start_date + timedelta(days=i - 1, hours=randhour) 
    randday = random.randint(1,365)                                
    randhour = random.randint(0, 23)                               
    randminute = random.randint(0, 59)                             
    randsecond = random.randint(0,59)                              
    comdate = datetime(datetime.now().year, 1, 1) + timedelta(     
        days=randday - 1,                                          
        hours=randhour,                                            
        minutes=randminute,                                        
        seconds=randsecond                                         
    )                                                              
                                                                   
                                                                   
    comdate_str = comdate.strftime("%Y-%m-%d %H:%M:%S")            
                                                                   
    with open(fp, "a") as file:                                    
        file.write(f"commit {i} haha\n")                           
                                                                   
    os.system("git add .")                                         
                                                                   
    os.environ["GIT_AUTHOR_DATE"] = comdate_str                    
    os.environ["GIT_COMMITTER_DATE"] = comdate_str                 
    os.system(f'git commit -m "commit {i}" --date="{comdate_str}"')
                                                                   
    os.system("git push origin main")                              
