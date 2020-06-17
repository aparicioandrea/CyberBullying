from os import listdir                                                                                                                                        
import pandas as pd                                                                                                                                           
                                                                                                                                                              
files = listdir("/Volumes/Transcend/Instagram_normal_users")                                                                                                  
                                                                                                                                                              
key_IGuser = "instagram user id:"                                                                                                                             
len_IGuser = len(key_IGuser)                                                                                                                                  
key_com = "comments for this media:"                                                                                                                          
len_com = len(key_com)                                                                                                                                        
key_user = "userID:"                                                                                                                                          
len_user = len(key_user)                                                                                                                                      
key_likes = "likes for" 


for k in files:                                                                                                                                               
    #k=files[0]                                                                                                                                               
    print(k)                                                                                                                                                  
    if k[0]=="N":                                                                                                                                             
        file = open("/Volumes/Transcend/Instagram_normal_users/"+k)                                                                                           
        content = file.read()                                                                                                                                 
        file.close()                                                                                                                                          
        i=0                                                                                                                                                   
        connectedUsers = []                                                                                                                                   
        while content.find(key_IGuser,i) != -1:                                                                                                               
            OwnStart = content.find(key_IGuser,i)+len_IGuser                                                                                                  
            OwnEnd = content.find(" ",OwnStart)                                                                                                               
            ownerId = int(content[OwnStart:OwnEnd])                                                                                                           
            usersId = [ownerId]                                                                                                                               
            #print(ownerId)                                                                                                                                   
            i = OwnEnd                                                                                                                                        
            while content.find(key_com,i)<content.find(key_IGuser,i):                                                                                         
                #print(i)                                                                                                                                     
                pos_comm = content.find(key_com,i)+len(key_com)+1                                                                                             
                #print(content.find(key_com,i))                                                                                                               
                i = pos_comm                                                                                                                                  
                if content[pos_comm:pos_comm+len_user] == key_user:                                                                                           
                    j = pos_comm+len_user                                                                                                                     
                    #print(j)                                                                                                                                 
                    IDstart = j                                                                                                                               
                    IDend = content.find(" ",IDstart)                                                                                                         
                    next_user = int(content[IDstart:IDend])                                                                                                   
                                                                                                                                                              
                    if next_user != ownerId :                                                                                                                 
                        usersId.append(next_user)                                                                                                             
                        #print("s")                                                                                                                           
                        #print(next_user)                                                                                                                     
                    #it = 0                                                     
                    while content.find(key_user,j)<content.find(key_likes,j):                                                                                 
                        #it = it+1                                                                                                                            
                        #print(it)                                                                                                                            
                        IDstart = content.find(key_user,j)+len_user                                                                                           
                        IDend = content.find(" ",IDstart)                                                                                                     
                        next_user = int(content[IDstart:IDend])                                                                                               
                        j = IDstart+1                                                                                                                         
                        if next_user != ownerId:                                                                                                              
                            #print("ns")                                                                                                                      
                            #print(next_user)                                                                                                                 
                            usersId.append(next_user)                                                                                                         
            usersId = list(dict.fromkeys(usersId))                                                                                                            
            connectedUsers.append(usersId)                                                                                                                    
                                                                                                                                                              
        connectedUsers = pd.DataFrame(connectedUsers)                                                                                                         
        connectedUsers.to_csv('ConnectedUsers/'+k[18:-4]+'.csv', index=False, header=False, sep= ' ')    


