import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='root', password='Newtonlaw3', host='localhost', database='hospital')

if conn:
    print("connected successfully")
else:
    print("connection not established")


select_appointment = """SELECT * FROM appointment"""
cursor = conn.cursor()
cursor.execute(select_appointment)
result = cursor.fetchall()

tbl = "<tr><td>NAME</td><td>EMAIL</td><td>ID<td>SPECIALITY</td></tr>"
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>" % row[0]
    p.append(a)
    b = "<td>%s</td>" % row[1]
    p.append(b)
    c = "<td>%d</td>" % row[2]
    p.append(c)
    d = "<td>%s</td></tr>" % row[3]
    p.append(d)

contents = '''<!DOC TYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">    
<html>
<head>
<meta content ="text/html; charset=ISO-8859-1"
http-equiv = "content-type">
<title> View Appointments</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
''' % (p)

contents1 = 'add_appointment.html' % (p)

filename = 'view_appointment.html'


def main(content, filename1):
    output = open(filename1, 'w')
    output.write(content)
    output.close()


main(contents, filename)
webbrowser.open(filename)

if conn.is_connected():
    cursor.close()
    conn.close()
    print("my sql connection is closed")
