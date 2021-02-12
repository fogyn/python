import  sqlite3 as sq
import  sys
import  os


db="task.db"
table = "hierarhy"
title0="id"
title1="id_parent"
title2="name"
title3="image"
title4="state"

#Дополнительная функция для перекодирования фото в бинарный файл
def image_binary(path):
    f = open(path,'rb')
    image_b = f.read()
    return  image_b

#Дополнительная функция преобразования фото из базы в картинку

def image_db_image(image_b,name):

    path="./outimage/"+str(name)+".png"
    f = open(path, 'wb')
    f.write(image_b)


#Функция создания новой записи
def new_element(datadase, table, model):
    #print("Hai2")
    con= sq.connect(datadase)
    cur = con.cursor()
    query = "INSERT INTO " +str(table) + "(id_parent, name, image, state) VALUES(?,?,?,?)"
    cur.execute(query, model)
    con.commit()
    cur.close()
    con.close()

#Функция редактирования записи в базе
def element_update(datadase, table, model):
    con= sq.connect(datadase)
    cur = con.cursor()
    #print("Hai3")
    query2 = 'UPDATE ' + table + ' SET id_parent=?, name=?, image=?, state=? WHERE id=?'
    #print(query2)
    cur.execute(query2, model)
    con.commit()
    cur.close()
    con.close()

#Функция удаления элемента из базы
def element_del(datadase, table, title, value):
    #print("Hai4")
    con= sq.connect(datadase)
    cur = con.cursor()
    query = 'DELETE FROM ' +table + " WHERE " + title + '=' + str(value)
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

#Функция запроса из базы всех записей
def element_all(datadase, table):
    #print("Hai5")
    con= sq.connect(datadase)
    cur = con.cursor()
    query = "SELECT * FROM " + str(table)
    cur.execute(query)

    result = cur.fetchall()
    #con.commit()
    cur.close()
    con.close()

    return result

def element_all_id(datadase, table):
        #print("Hai5")
        con = sq.connect(datadase)
        cur = con.cursor()
        # убрал str()
        query = "SELECT id FROM " + str(table)
        cur.execute(query)

        result = cur.fetchall()
        # con.commit()
        cur.close()
        con.close()

        return result

    #for row in result:
        #name = row[2]
        #state = row[4]
        #print(row)

#Функция запроса из базы записей по критерию
def element_select_param(datadase, table, param, date):
    #print("Hai6")
    con= sq.connect(datadase)
    cur = con.cursor()
    #query = 'UPDATE ' +table + " SET " + title + "=" + str(value) + " WHERE " + param + '=' + str(date)
    query = "SELECT * FROM " + str(table) + " WHERE "+ param + '=' + str(date)
    cur.execute(query)

    result = cur.fetchall()
    # con.commit()
    cur.close()
    con.close()

    #for row in result:
        # name = row[2]
        # state = row[4]
       # print(row)
    return result




