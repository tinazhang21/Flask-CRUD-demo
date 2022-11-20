from flask import Flask, render_template, request, redirect, flash
#from flask_mysqldb import MySQL
#import yaml
import mysql.connector

app=Flask(__name__)

app.config['SECRET_KEY'] = 'my secrect key'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "rootroot",
    database = "employees"
) 

@app.route("/")
def index():
    #cur = db.cursor(dictionary=True)
    #cur.execute("select * from employee;")
    #userDetails = cur.fetchall()
    return render_template('index.html')
    #for user in userDetails: print(user)
    #return render_template('index.html',userDetails=userDetails)
    #return render_template('templates/index.html')

@app.route("/employee", methods=['GET','POST'])
def employee():
    cur = db.cursor(dictionary=True)
    cur.execute("select * from employee;")
    userDetails = cur.fetchall()
    #for user in userDetails: print(user)
    return render_template('employee.html',userDetails=userDetails)
    #return render_template('templates/index.html')

@app.route("/insert", methods=['POST']) 
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        birthday = request.form['birthday']
        entrytime = request.form['entrytime']    
        department = request.form['department'] 
        position = request.form['position'] 
        cur = db.cursor()
        cur.execute("insert into employee(name,email,gender,birthday,entrytime,department,position) values(%s,%s,%s,%s,%s,%s,%s);",(name,email,gender,birthday,entrytime,department,position))
        db.commit()
        cur.close()
        flash("Employee Inserted Successfully! ")
        return redirect('/employee') 

@app.route("/update/<emp_id>", methods=['GET','POST'])
def update(emp_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        birthday = request.form['birthday']
        entrytime = request.form['entrytime']
        department = request.form['department']
        position = request.form['position']
        cur = db.cursor()
        cur.execute("update employee set name=%s,email=%s,gender=%s,birthday=%s,entrytime=%s,department=%s,position=%s where emp_id=%s;",(name,email,gender,birthday,entrytime,department,position,emp_id))
        db.commit()
        cur.close()
        flash("Employee Updated Successfully! ")
        return redirect('/employee') 

@app.route('/delete/<emp_id>', methods=['GET','POST'])
def delete(emp_id): 
    print(type(emp_id))
    cur = db.cursor()
    #sql = "delete from users where name=%s"
    #cur.execute(sql,name)
    cur.execute("delete from employee where emp_id=" + emp_id + ";")
    db.commit()
    cur.close()
    flash("Employee Deleted Successfully! ")
    return redirect('/employee') 


if __name__ == '__main__':
    app.run(debug=True)


"""
def main():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = db.cursor()
        cur.execute("insert into users(name,email) values(%s,%s);",(name,email))
        db.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route("/users")

"""


