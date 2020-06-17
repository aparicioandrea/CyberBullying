#this script opens IG raw data, extracts comment interactions and saves them in the form of an adjacency list
#first enty in every row is the source node and the rest are targets

from os import listdir                                                                                                                                        
import pandas as pd                                                                                                                                           
                                                                                                                                                              
files = listdir("/Volumes/Transcend/Instagram_normal_users")   #Path to Instagram raw data                                                                                               
                                                                                                                                                              
key_IGuser = "instagram user id:"                                                                                                                             
len_IGuser = len(key_IGuser)                                                                                                                                  
key_com = "comments for this media:"                                                                                                                          
len_com = len(key_com)                                                                                                                                        
key_user = "userID:"                                                                                                                                          
len_user = len(key_user)                                                                                                                                      
key_likes = "likes for" 


for k in files:                                                                                                                                                                                                                                                                                              
    #print(k)                                                                                                                                                   
    if k[0]=="N":                                                                                                                                             
        file = open("/Volumes/Transcend/Instagram_normal_users/"+k)                                                                                           
        content = file.read()                                                                                                                                 
        file.close()                                                                                                                                          
        i=0                                                                                                                                                   
        connectedUsers = []                                                                                                                                   
        while content.find(key_IGuser,i) != -1:                                                                                                               
            OwnStart = content.find(key_IGuser,i)+len_IGuser #gets ID of media owner                                                                                                 
            OwnEnd = content.find(" ",OwnStart)                                                                                                               
            ownerId = int(content[OwnStart:OwnEnd])                                                                                                           
            usersId = [ownerId]                                                                                                                               
            #print(ownerId)                                                                                                                                   
            i = OwnEnd                                                                                                                                        
            while content.find(key_com,i)<content.find(key_IGuser,i):                                                                                                                                                                                                                                          
                pos_comm = content.find(key_com,i)+len(key_com)+1  # finds the comments for the media                                                                                           
                i = pos_comm                                                                                                                                  
                if content[pos_comm:pos_comm+len_user] == key_user:                                                                                           
                    j = pos_comm+len_user                                                                                                                     
                    IDstart = j                                                                                                                               
                    IDend = content.find(" ",IDstart)                                                                                                         
                    next_user = int(content[IDstart:IDend]) #gets IDs of first commenter                                                                                                  
                                                                                                                                                              
                    if next_user != ownerId :                                                                                                                 
                        usersId.append(next_user) #If commenter is not owner, adds an edge to owner 
                        
                    while content.find(key_user,j)<content.find(key_likes,j): #finds the rest of commenters if any                                                                                                        IDstart = content.find(key_user,j)+len_user                                                                                           
                        IDend = content.find(" ",IDstart)                                                                                                     
                        next_user = int(content[IDstart:IDend])                                                                                               
                        j = IDstart+1                                                                                                                         
                        if next_user != ownerId:                                                                                                              
                            usersId.append(next_user)                                                                                                         
            usersId = list(dict.fromkeys(usersId)) #removes duplicate edges                                                                                                           
            connectedUsers.append(usersId)                                                                                                                    
                                                                                                                                                              
        connectedUsers = pd.DataFrame(connectedUsers)                                                                                                         
        connectedUsers.to_csv('ConnectedUsers/'+k[18:-4]+'.csv', index=False, header=False, sep= ' ') #DataFrame needs to be in this format to be an adjacency list for the graph    


