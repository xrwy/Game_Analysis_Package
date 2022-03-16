from flask import Flask, render_template, request
import sqlite3
import random
import time


app = Flask(__name__)

upperCharacters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZWX"
lowerCharacters = "abcçdefgğhıijklmnoöprsştuüvyzwx"

@app.route('/', methods = ['GET','POST'])
def main():
    return 'Main Page'


@app.route('/firstlogin', methods=['GET','POST'])
def firstLogin():
    if request.method == 'POST':
        systemLang = request.args.get('systemlanguage')
        with sqlite3.connect('users.db') as db:
            cursorIm = db.cursor()
            cursorIm.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,token text,win text, lose text, level_ text, system_language text, temp_day text, totalDays text, second text, minutes_ text, hours_ text)""")
            cursorIm.execute("""SELECT * FROM users""")
            data = cursorIm.fetchall()
            
            if(len(data) == 0):
                data_ = [(1,'','','','',str(systemLang),'','','','','')]
                for dt__ in data_:
                    cursorIm.execute("""INSERT INTO users VALUES %s""" % (dt__,))
                db.commit()
                
                return str(1)
        
            else:
                dt_ = len(data) + 1
                data = [(dt_,'','','','',str(systemLang),'','','','','')]
                for dt in data:
                    cursorIm.execute("""INSERT INTO users VALUES %s""" % (dt,))
                db.commit()
                      
                return str(dt_)
    else:
        return 'For post processing only'           


@app.route('/gettoken', methods=['GET','POST'])
def getToken():
    token = ""
    __id = ""
    if request.method == 'POST':
        __id = request.args.get('id')
        
        with sqlite3.connect('users.db') as db:
            cursorIm = db.cursor()
            cursorIm.execute("""SELECT * FROM users""")
            data = cursorIm.fetchall()
            print(__id)
            for dt in data:
                if(str(dt[0]) == __id):
                    rndNum = random.randint(100,9999)
                    rndNum2 = random.randint(100,9999)
                    rndChar1 = random.choice(upperCharacters)
                    rndChar2 = random.choice(lowerCharacters)
                    rndCharFull = rndChar1 + rndChar2
                    token = str(rndNum) + rndCharFull + str(rndNum2)

                    sqliteUpdate = """UPDATE users SET token = ? WHERE id = ? """
                    columsValues = (token,__id)   
                    cursorIm.execute(sqliteUpdate,columsValues) 
                    
                    return str(token)
                            
                else:
                    ""
                                
            return "Id Not Found"
        
    else:
        return 'For post processing only'


@app.route('/checkinternet', methods=['GET','POST']) 
def checkInternet():
    return '1'
    
    
@app.route('/increasingwinning', methods=['GET','POST'])
def increasingWinning():
    if request.method == 'POST':    
        id_ = request.form.get('id')
        token = request.form.get('token')
        
        with sqlite3.connect('users.db') as db:
            cursorIm = db.cursor()
            cursorIm.execute("""SELECT * FROM users""")
            data = cursorIm.fetchall()
            for dt in data:
                if(str(dt[0]) == str(id_) and str(dt[1]) == str(token)):
                    with sqlite3.connect('users.db') as db:
                        cursorIm = db.cursor()
                        cursorIm.execute("""SELECT * FROM users where id=?""", (id_,))
                        data = cursorIm.fetchall()
                            
                        for _dt in data:
                            if _dt[2] == '':
                                sqliteUpdate = """UPDATE users SET win = ? WHERE id = ? """
                                columsValues = (1,_dt[0])   
                                cursorIm.execute(sqliteUpdate,columsValues)
                                sqliteUpdate2 = """UPDATE users SET level_ = ? WHERE id = ? """
                                columsValues2 = (1,_dt[0])   
                                cursorIm.execute(sqliteUpdate2,columsValues2)
                                        
                                return "Successful"

                            else:
                                x = int(_dt[2])
                                y = x + 1
                                sqliteUpdate = """UPDATE users SET win = ? WHERE id = ? """
                                columsValues = (y,_dt[0])   
                                cursorIm.execute(sqliteUpdate,columsValues)
                                sqliteUpdate = """UPDATE users SET level_ = ? WHERE id = ? """
                                columsValues = (y,_dt[0])   
                                cursorIm.execute(sqliteUpdate,columsValues)
                                        
                                return "Successful"

                           
            return "Check the data" 
    
    else:
        return 'For post processing only'       
    

@app.route('/increasinglosing', methods=['GET','POST'])
def increasingLosing():
    if request.method == 'POST':    
        id_ = request.form.get('id')
        token = request.form.get('token')
        
        with sqlite3.connect('users.db') as db:
            cursorIm = db.cursor()
            cursorIm.execute("""SELECT * FROM users""")
            data = cursorIm.fetchall()
            for dt in data:
                if(str(dt[0]) == str(id_) and str(dt[1]) == str(token)):
                    with sqlite3.connect('users.db') as db:
                        cursorIm = db.cursor()
                        cursorIm.execute("""SELECT * FROM users where id=?""", (id_,))
                        data = cursorIm.fetchall()
                            
                        for _dt in data:
                            if _dt[3] == '':
                                sqliteUpdate = """UPDATE users SET lose = ? WHERE id = ? """
                                columsValues = (1,_dt[0])   
                                cursorIm.execute(sqliteUpdate,columsValues)
                                
                                return "Successful"
                            
                            else:
                                x = int(_dt[3])
                                y = x + 1
                                sqliteUpdate = """UPDATE users SET lose = ? WHERE id = ? """
                                columsValues = (y,_dt[0])     
                                cursorIm.execute(sqliteUpdate,columsValues)
                                        
                                return "Successful"
                    
            return "Check the data"
        
    else:
        return 'For post processing only'


@app.route('/getday', methods=['GET','POST'])
def getDay():
    if request.method == 'POST':    
        id_ = request.args.get('id')
        token = request.args.get('token')
        print(id_, token)
        with sqlite3.connect('users.db') as db:
            cursorIm = db.cursor()
            cursorIm.execute("""SELECT * FROM users""")
            data = cursorIm.fetchall()
            for dt in data:
                if(str(dt[0]) == str(id_) and str(dt[1]) == str(token)):
                    with sqlite3.connect('users.db') as db:
                        cursorIm = db.cursor()
                        cursorIm.execute("""SELECT * FROM users where id=?""", (id_,))
                        data = cursorIm.fetchall()
                        print(data[0][6])
                        if(data[0][6] == str(time.asctime().split()[2])):
                            return "Even if you enter on the same day, the total counts as 1"
                        else:
                            if(data[0][6] == ''):
                                sqliteUpdate = """UPDATE users SET temp_day = ?, totalDays = ? WHERE id = ? """
                                value = str(time.asctime().split()[2]) # get day
                                columsValues = (value,1,id_)     
                                cursorIm.execute(sqliteUpdate,columsValues)
                                return "Successful"
                            else:
                                if(data[0][6] != str(time.asctime().split()[2])):
                                    sqliteUpdate = """UPDATE users SET temp_day = ?, totalDays = ? WHERE id = ? """
                                    value = str(time.asctime().split()[2])
                                    totalDays = int(data[0][7]) + 1
                                    columsValues = (value,totalDays,id_)     
                                    cursorIm.execute(sqliteUpdate,columsValues)
                                    return "Successful"   
    
                else:
                    ''
                        
            return 'Check the information'
        
    else:
        return 'For post processing only'
        

@app.route('/time', methods=['GET','POST'])
def time():
    if(request.method == 'POST'):
        id_ = request.args.get('id')
        token = request.args.get('token')
        time = request.args.get('time')
        
        with sqlite3.connect('users.db') as userDb:
            userDbCur = userDb.cursor()
            userDbCur.execute("""SELECT * FROM users""")

            fullData = userDbCur.fetchall()
            print(id_, token, time)
            for _data in fullData:
                if(str(_data[0]) == id_ and str(_data[1]) == str(token)):
                    if(_data[8] == ''):
                        sqliteUpdate = """UPDATE users SET second = ? WHERE id = ? """
                        _time = (time,id_)
                        userDbCur.execute(sqliteUpdate,_time)
                        
                        userDbCur.execute("""SELECT * FROM users""")
                        fullData = userDbCur.fetchall()
                        
                        sqliteUpdate2 = """UPDATE users SET minutes_ = ? WHERE id = ? """
                        _time2 = int(fullData[0][8]) // 60
                        values = (_time2,id_)
                        userDbCur.execute(sqliteUpdate2,values)
                        
                        
                        hours = int(fullData[0][8]) // 3600
                        if(hours > 0 and str(hours) != fullData[0][10]):
                            sqliteUpdate3 = """UPDATE users SET hours_ = ? WHERE id = ? """
                            values2 = (hours,id_)
                            userDbCur.execute(sqliteUpdate3,values2)
                        else:
                            ''
                        return "Completed"

                    else:
                        sqliteUpdate = """UPDATE users SET second = ? WHERE id = ? """
                        newSecond = int(_data[8]) + int(time)
                        _time = (newSecond,id_)
                        userDbCur.execute(sqliteUpdate,_time)
                        
                        userDbCur.execute("""SELECT * FROM users""")
                        fullData = userDbCur.fetchall()

                        sqliteUpdate2 = """UPDATE users SET minutes_ = ? WHERE id = ? """
                        _time2 = int(fullData[0][8]) // 60
                        values = (_time2,id_)
                        userDbCur.execute(sqliteUpdate2,values)
                        

                        hours = int(fullData[0][8]) // 3600
                        if(hours > 0 and str(hours) != fullData[0][10]):
                            sqliteUpdate3 = """UPDATE users SET hours_ = ? WHERE id = ? """
                            values2 = (hours,id_)
                            userDbCur.execute(sqliteUpdate3,values2)
                        else:
                            ''
                        return "Completed"
                else:
                    ''
            
            return 'Unauthorized Access !!!'
            
         
@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/adminpanel', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        
        with sqlite3.connect('admin.db') as adminDb:
            cursorDb = adminDb.cursor()
            cursorDb.execute("""CREATE TABLE IF NOT EXISTS admin_ (username text, password_ text)""")
            cursorDb.execute("""SELECT * FROM admin_ where username=? and password_=?""", (username,password,))
            data = cursorDb.fetchall()
            for dt in data:
                if(dt[0] == username and dt[1] == password):
                    with sqlite3.connect('users.db') as usersDb:
                        usersDbCursor = usersDb.cursor()
                        usersDbCursor.execute("""SELECT * FROM users""")
                        data_ = usersDbCursor.fetchall()
                            
                        return render_template('adminpanel.html', _data = data_)
                        
                else:
                    ''
                        
            return 'Unauthorized Access !!!'
        
    else:
        return 'For post processing only'
    

@app.route('/userslist', methods=['GET','POST'])
def userList():
    with sqlite3.connect('users.db') as usersDb:
        usersDbCursor = usersDb.cursor()
        usersDbCursor.execute("""SELECT * FROM users""")
        data_ = usersDbCursor.fetchall()
                        
        return render_template('userslist.html', _data = data_)
            


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
    #app.run(debug=True, port=4000)  We can use any port we want but the default ports is 5000.
    
    
