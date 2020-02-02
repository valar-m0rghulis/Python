

from tkinter import*
from tkinter.font import Font
import cx_Oracle
from InstaDBIntegration import Most_Liked_User, Popular_Tag, Music_Pic

con = cx_Oracle.connect('infosys/admin@localhost/xe')
cur = con.cursor()

def MAX_Like():
    accept()
    ids = list()
    u_name = entry1.get()
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
    for row in cur:
            ids.append(row[0])
    result_string = '''\nPictures with Maximum likes : \nPICTURE_ID\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)
    
def MIN_Like():
    accept()
    ids = list()
    u_name = entry1.get()
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
    for row in cur:
            ids.append(row[0])
    result_string = '''\nPictures with Minimum likes : \nPICTURE_ID\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)

def Who_Liked():
    accept()
    ids = list()
    u_name = entry1.get()
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
    for row in cur:
            ids.append(row[0])
    print(ids)
    result_string = '''\nUsers who liked your pictures most : \nUSER_ID\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)
     
# Pictures related to music

def Music_Pic():
    ids = list()
    query = """SELECT photoid FROM photo_tag WHERE tagid IN(SELECT tagid FROM tags WHERE tag ='Music')"""
    cur.execute(query)
    for row in cur:
            ids.append(row[0])
    result_string = '''\nPicturs related to music  : \nPICTURE_ID\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)

# Popular tag

def Popular_Tag():
    ids = list()
    query = """SELECT tag FROM tags 
            WHERE tagid IN(SELECT tagid FROM 
            (SELECT tagid,COUNT(tagid) AS counts FROM photo_tag 
            GROUP BY(tagid)) 
            WHERE counts =(SELECT MAX(counts) FROM
            (SELECT tagid,COUNT(tagid) AS counts FROM photo_tag 
            GROUP BY(tagid))))"""
    
    cur.execute(query)
    for row in cur:
            ids.append(row[0])
    result_string = '''\nPopular Tags  : \nTAGS\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + row + '\n'
    result_string = result_string + rs
    display(result_string)
        
# Most liked users
    
def Most_Liked_User():
    ids = list()
    query = """SELECT DISTINCT userid FROM photos 
            WHERE photoid IN(SELECT photoid FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid)) 
            WHERE counts = (SELECT MAX(counts) FROM 
            (SELECT photoid,COUNT(userid) AS counts FROM likes 
            GROUP BY(photoid))))"""
            
    cur.execute(query)
    for row in cur:
            ids.append(row[0])
    result_string = '''\nMost liked users  : \nUSER_ID\n'''
    rs = ''
    for row in ids:
        rs = rs + '   ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)
        

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
        result_string = "\nTag added successfully !"
        display(result_string) 
    except cx_Oracle.DatabaseError as e:
        result_string = "\nError ::"
        rs = '' + str(e)
        result_string = result_string + rs
        display(result_string) 
    
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
    result_string = "\nInactive users deleted :\nUSER_ID :: "
    rs = ''
    for row in uid:
        rs = rs + '    ' + str(row) + '\n'
    result_string = result_string + rs
    display(result_string)

root = Tk()
root.geometry('900x600')
root.title('InstaDB')
root.configure(bg='powder blue')





instaFont = Font(family = 'French Script MT',size = 50)
textFont = Font(family = 'Bahnschrift',size = 18)
xp = 2
yp = 2

frame1 = Frame(root)
frame1.pack(fill = X)
instaTitle = Label(frame1,text = 'Instagram',font = instaFont,fg = 'navy',bg = 'SteelBlue1')
instaTitle.pack(fill = X)


frame2 = Frame(root,background = 'RoyalBlue1',relief=SUNKEN)
frame2.pack(fill = X)
sub1 = Label(frame2,text = 'Options',font = textFont,bg = 'RoyalBlue1',bd = 3)
sub2 = Label(frame2,text = 'Results',font = textFont,bg = 'RoyalBlue1',bd = 3)
sub1.pack(side = LEFT,padx = 90,fill = X)
sub2.pack(side = RIGHT,padx = 120,fill = X)


options = Frame(root,width = 300,height = 400)
options.pack(side = LEFT,padx = 20,fill = X)


max_likes = Button(options,text = "Max Likes",fg = 'white',bg = 'DarkOrange1',font = textFont,command = MAX_Like)
min_likes = Button(options,text = "Min Likes",fg = 'white',bg = 'DarkOrange1',font = textFont,command = MIN_Like)
most_liker = Button(options,text = "Who Liked Most",fg = 'white',bg = 'DarkOrange1',font = textFont,command = Who_Liked)
music_pic = Button(options,text = "Music Pictures",fg = 'white',bg = 'DarkOrange1',font = textFont,command = Music_Pic)
popular_tag = Button(options,text = "Popular Tag",fg = 'white',bg = 'DarkOrange1',font = textFont,command= Popular_Tag)
maxlike_user = Button(options,text = "Most Liked User",fg = 'white',bg = 'DarkOrange1',font = textFont,command = Most_Liked_User)
old_tag = Button(options,text = "Old Tagging",fg = 'white',bg = 'DarkOrange1',font = textFont,command = Old_Tag)
del_inactive = Button(options,text = "Delete Inactive Users",fg = 'white',bg = 'DarkOrange1',font = textFont,command = Delete_Inactive)

max_likes.pack(padx = xp,pady = yp,fill = X)
min_likes.pack(padx = xp,pady = yp,fill = X)
most_liker.pack(padx = xp,pady = yp,fill = X)
music_pic.pack(padx = xp,pady = yp,fill = X)
popular_tag.pack(padx = xp,pady = yp,fill = X)
maxlike_user.pack(padx = xp,pady = yp,fill = X)
old_tag.pack(padx = xp,pady = yp,fill = X)
del_inactive.pack(padx = xp,pady = yp,fill = X)

get = Frame(root,width = 300,height = 400)
username = Label(get,text = "Enter Username",font = textFont)
entry1 = Entry(get)

def accept():
    get.pack(side = LEFT)
    username.pack(padx = xp,pady = yp,fill = X)
    entry1.pack(padx = xp,pady = yp,fill = X)

results = Frame(root,width = 300,height = 200)
results.pack(side = RIGHT,padx = 20)
result_text = Text(results,width = 40,height = 30)
result_text.pack(padx = 10,pady = 10)

def display(result_string):
    result_text.delete(1.0,END)
    result_text.insert(CURRENT,result_string)

root.mainloop()

