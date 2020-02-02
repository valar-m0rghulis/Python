
import cx_Oracle


def UI():
    
    print("===========[OPTIONS]==============")
    print("1. Max likes")
    print("2. Min likes")
    print("3. Who liked most")
    print("4. Music pictures")
    print("5. Popular tag")
    print("6. Most liked user")
    print("7. Old tagging")
    print("8. Delete inactive users")
    print("__________________________________")


# MAX Likes 

def MAX_Like(u_name):
    
    query = """SELECT photoid FROM 
            (SELECT photoid,COUNT(userid) AS likes FROM likes 
            GROUP BY(photoid) 
            HAVING photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))) 
            WHERE likes =(SELECT MAX(counts) FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid) 
            HAVING photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))))
            """
    cur.execute(query,{'user_name':u_name})
    print("\nPictures with Maximum likes : \n")
    print("PICTURE_ID\n")
    for row in cur:
        print(row[0],'\n')
        
    result_string = ''.join(cur)
        
# MIN Likes

def MIN_Like(u_name):
    
    query = """SELECT photoid FROM 
            (SELECT photoid,COUNT(userid) AS likes FROM likes 
            GROUP BY(photoid) 
            HAVING photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))) 
            WHERE likes =(SELECT MIN(counts) FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid) 
            HAVING photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))))
            """
    cur.execute(query,{'user_name':u_name})
    print("\nPictures with Minimum likes : \n")
    print("PICTURE_ID\n")
    for row in cur:
        print(row[0],'\n')
    
# Who liked most

def Who_Liked(u_name):
    
    query = """SELECT DISTINCT userid FROM 
            (SELECT userid,COUNT(photoid) AS counts FROM 
            (SELECT userid,photoid FROM likes 
            WHERE photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))) 
            GROUP BY(userid))
            WHERE counts = (SELECT MAX(counts) FROM 
            (SELECT userid,COUNT(photoid) AS counts FROM 
            (SELECT userid,photoid FROM likes 
            WHERE photoid IN(SELECT photoid FROM photos 
            WHERE userid =(SELECT userid FROM users WHERE username = :user_name))) 
            GROUP BY(userid)))"""
            
    cur.execute(query,{'user_name':u_name})
    print("\nUsers who liked your pictures most : \n")
    print("USER_ID\n")
    for row in cur:
        print(row[0],'\n')       

# Pictures related to music

def Music_Pic():
    
    query = """SELECT photoid FROM photo_tag WHERE tagid IN(SELECT tagid FROM tags WHERE tag ='Music')"""
    cur.execute(query)
    print("\nPicturs related to music  : \n")
    print("PICTURE_ID\n")
    for row in cur:
        print(row[0],'\n')

# Popular tag

def Popular_Tag():
    
    query = """SELECT tag FROM tags 
            WHERE tagid IN(SELECT tagid FROM 
            (SELECT tagid,COUNT(tagid) AS counts FROM photo_tag 
            GROUP BY(tagid)) 
            WHERE counts =(SELECT MAX(counts) FROM
            (SELECT tagid,COUNT(tagid) AS counts FROM photo_tag 
            GROUP BY(tagid))))"""
    
    cur.execute(query)
    print("\nPopular Tags  : \n")
    print("TAGS\n")
    for row in cur:
        print(row[0],'\n')
        
# Most liked users
    
def Most_Liked_User():
    
    query = """SELECT DISTINCT userid FROM photos 
            WHERE photoid IN(SELECT photoid FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid)) 
            WHERE counts = (SELECT MAX(counts) FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid))))"""
            
    cur.execute(query)
    print("\nMost liked users  : \n")
    print("USER_ID\n")
    for row in cur:
        print(row[0],'\n')
        

# Old tagging

def Old_Tag():
    
    try:
        
        pid = list()
        
        query = """SELECT tagid FROM tags WHERE tag='Old'"""
        cur.execute(query)
        t_id = cur.fetchone()[0]
        
        query = """SELECT photoid FROM photos WHERE post_date < ADD_MONTHS(SYSDATE,-12*3)"""
        cur.execute(query)
        for row in cur:
            pid.append(row[0])
            
        query = """INSERT INTO photo_tag VALUES(:p_id,:tid)"""
        for i in pid:
            cur.execute(query,(i,t_id))
            
        con.commit()
        print("\nTag added successfully !")
    
    except cx_Oracle.DatabaseError as e:
        
        print("Error ::",e)

    

# delete inactive users

def Delete_Inactive():
    
    uid = list()
    query = """SELECT userid FROM users 
            WHERE userid NOT IN
            (SELECT DISTINCT userid FROM photos 
            WHERE post_date > ADD_MONTHS(SYSDATE,-12*1))"""      
    cur.execute(query)
    for row in cur:
        uid.append(row[0])
        
    query = """DELETE FROM users WHERE userid = :uids"""
    for i in uid:
        
        cur.execute(query,{'uids':i})
        
    con.commit()    
    print("\nInactive users deleted :\n")
    print("USER_ID :: ",uid)
    

def Interact():
    
    flag = 1    
    while (flag == 1):
        
        UI()
        
        choice = int(input("Enter your choice :: "))
        
        if(choice == 1):
            
            u_name = input("Enter Your Username ::")
            
            MAX_Like(u_name)
        
        elif(choice == 2):
            
            u_name = input("Enter Your Username ::")
            
            MIN_Like(u_name)
            
        elif(choice == 3):
            
            u_name = input("Enter Your Username ::")
            
            Who_Liked(u_name)
            
        elif(choice == 4):
            
            Music_Pic()
            
        elif(choice == 5):
            
            Popular_Tag()
            
        elif(choice == 6):
            
            Most_Liked_User()
            
        elif(choice == 7):
            
            Old_Tag()
            
        elif(choice == 8):
            
            Delete_Inactive()
            
        else:
            
            print(" Please Enter valid Choice!!")
        
        print("\n Do you want to continue ?(1/0) ::")
        flag = int(input())
        
        if(flag == 0):
            print("Thank You !")
            break
    
    

if __name__=="__main__":
    
    con = cx_Oracle.connect('infosys/admin@localhost/xe')
    cur = con.cursor()
    Interact()
    cur.close()
    con.close()
    
    
#####################################################################################
#####################################################################################
# OUTPUT :
'''
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 1
Enter Your Username ::asmith

Pictures with Maximum likes : 

PICTURE_ID

9 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 2
Enter Your Username ::asmith

Pictures with Minimum likes : 

PICTURE_ID

1 

2 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 3
Enter Your Username ::asmith

Users who liked your pictures most : 

USER_ID

2 

7 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 4

Picturs related to music  : 

PICTURE_ID

18 

10 

2 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 5

Popular Tags  : 

TAGS

World 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 6

Most liked users  : 

USER_ID

1 

2 


 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 7

Tag added successfully !

 Do you want to continue ?(1/0) ::
1
===========[OPTIONS]==============
1. Max likes
2. Min likes
3. Who liked most
4. Music pictures
5. Popular tag
6. Most liked user
7. Old tagging
8. Delete inactive users
__________________________________
Enter your choice :: 8

Inactive users deleted :

USER_ID ::  [11, 7]

 Do you want to continue ?(1/0) ::
0
Thank You !
'''    