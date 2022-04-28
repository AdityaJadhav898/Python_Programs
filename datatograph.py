# Connecting to mysql database
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="5252",
                               database="test")
mycursor = mydb.cursor()

# Fecthing Data From mysql to my python progame
mycursor.execute("select cource, boys, girls from table1")
result = mycursor.fetchall
w=0.4
cource = []
boys = []
girls = []

for i in mycursor:
    cource.append(i[0])
    boys.append(i[1])
    girls.append(i[2])

print("cource = ", cource)
print("boys = ", boys)
print("girls = ", girls)

# Visulizing Data using Matplotlib
plt.bar(cource,boys,w,label="boys")
plt.bar(cource,girls,w,bottom=boys,label="girls")
plt.ylim(0, 100)
plt.xlabel("cources")
plt.ylabel("Students")
plt.title("Student's Information")
plt.show()
