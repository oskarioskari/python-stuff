import sqlite3 as s3
import random

def dropTable(filename):
    con = s3.connect(filename)
    c = con.cursor()
    try:
        c.execute("DROP TABLE area;")
    except s3.Error as e:
        print e.args[0], "drop"
    print "Deleted table in file ",filename
    con.commit()
    con.close()

def saveToFile(dictlist, filename):
    print "Saving to file                            |"
    print "|",
    con = s3.connect(filename)
    c = con.cursor()
    c.execute("PRAGMA synchronous = OFF")
    c.execute("PRAGMA journal_mode = OFF")
    index = 0
    loading = range(0,len(dictlist),len(dictlist)/20)
    for key in dictlist:
        if loading:
            if index >= min(loading):
                print "-",
                loading.remove(min(loading))
        index = index + 1
        skey = key.split('-')
        tkey = "x",skey[0],"y",skey[1]
        tkey = "".join(tkey)
        line = "UPDATE area SET type = ",str(dictlist[key])," WHERE XY = '",tkey,"';"
        command = "".join(line)
        try:
            c.execute(command)
            con.commit()
        except s3.Error as e:
            print e.args[0], "save"
    print "|"
    print "Table saved to file ",filename
    con.close()

def formatfile(filename, xlim, ylim):
    con = s3.connect(filename)
    c = con.cursor()
    try:
        c.execute("CREATE TABLE area(XY varchar(20) PRIMARY KEY, type integer);")
        for i in range(0,xlim):
            for j in range(0,ylim):
                coords = 'x',str(i),'y',str(j)
                coords = "".join(coords)
                line = "INSERT INTO area (XY,type) VALUES ('",coords,"',1);"
                command = "".join(line)
                try:
                    c.execute(command)
                except s3.Error as e:
                    print e.args[0], "loop"
        print "New table created"
    except s3.Error as e:
        print e.args[0], "create"
    con.commit()
    con.close()
    
def formatfile_random(filename, xlim, ylim):
    con = s3.connect(filename)
    c = con.cursor()
    try:
        c.execute("CREATE TABLE area(XY varchar(20) PRIMARY KEY, type integer);")
        for i in range(0,xlim):
            for j in range(0,ylim):
                rnum = random.randint(1,2)
                coords = 'x',str(i),'y',str(j)
                coords = "".join(coords)
                line = "INSERT INTO area (XY,type) VALUES ('",coords,"',",str(rnum),");"
                command = "".join(line)
                try:
                    c.execute(command)
                except s3.Error as e:
                    print e.args[0], "loop"
        print "New table created"
    except s3.Error as e:
        print e.args[0], "create"
    con.commit()
    con.close()

def getRows(filename, xlim, ylim):
    xylist = dict()
    con = s3.connect(filename)
    c = con.cursor()
    index = 0
    loading = range(0,(xlim*ylim),(xlim*ylim)/20)
    print "Loading from file                         |"
    print "|",
    for i in xrange(0,xlim):
        for j in xrange(0,ylim):
            try:
                if loading:
                    if index >= min(loading):
                        print "-",
                        loading.remove(min(loading))
                index = index + 1
                line = "SELECT type FROM area WHERE XY='x",str(i),'y',str(j),"';"
                command = "".join(line)
                c.execute(command)
                res = c.fetchone()
                key = str(i),'-',str(j)
                key = "".join(key)
                xylist[key] = res[0]
            except s3.Error as e:
                print e.args[0]
    print "|"
    con.commit()
    con.close()
    return xylist