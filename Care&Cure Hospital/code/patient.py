import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='root', password='Newtonlaw3', host='localhost', database='hospital')

if conn:
    print("connected successfully")
else:
    print("connection not established")

select_patient = """SELECT * FROM patient"""
cursor = conn.cursor()
cursor.execute(select_patient)
result = cursor.fetchall()

p = []

tbl = "<tr><td>NAME</td><td>EMAIL</td><td>ID</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>" % row[0]
    p.append(a)
    b = "<td>%s</td>" % row[1]
    p.append(b)
    c = "<td>%d</td></tr>" % row[2]
    p.append(c)


contents = '''<!DOC TYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">    
<html>
<head>
<meta content ="text/html; charset=ISO-8859-1"
http-equiv = "content-type">
<title> VIEW PATIENT</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
''' % (p)

filename = 'view_patient.html'

def main(contents, filename):
    output = open(filename, 'w')
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)

if (conn.is_connected()):
    cursor.close()
    conn.close()
    print("my sql connection is closed")
