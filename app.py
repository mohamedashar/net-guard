from flask import Flask, redirect, render_template, flash, request,session,send_file
from cryptography.fernet import Fernet
import mysql.connector
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
import yagmail
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/adminlogin")
def AdminLogin():
    return render_template('admin.html')
@app.route("/userfile")
def userfile():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM file ")
    data = cur1.fetchall()
    # return 'file register successfully'
    # return render_template('order.html', data=data)
    return render_template('userfile.html',data=data)
@app.route("/viewattack")
def viewattack():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM attacker1")
    data = cur1.fetchall()
    # return 'file register successfully'
    # return render_template('order.html', data=data)
    return render_template('viewattack.html',data=data)
@app.route("/NewUser")
def NewUser():
    return render_template('register.html')
@app.route("/UserLogin")
def UserLogin():
    return render_template('stud.html')
@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cur = conn.cursor()

    # ✅ total owners / staff
    cur.execute("SELECT COUNT(*) FROM regtb")
    staff_total = cur.fetchone()[0]

    # ✅ total data users / students
    cur.execute("SELECT COUNT(*) FROM userregtb")
    user_total = cur.fetchone()[0]

    # ✅ owner list
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()

    conn.close()

    return render_template(
        "AdminHome.html",
        staff_total=staff_total,
        user_total=user_total,
        data=data
    )


@app.route("/userdetails")
def userdetails():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM userregtb ")
    data = cur1.fetchall()
    # return 'file register successfully'
    # return render_template('order.html', data=data)
    return render_template('userdetails.html', data=data)

@app.route("/rNewUser", methods=['GET', 'POST'])
def rNewUser():
    if request.method == 'POST':

        # ✅ OTP CHECK
        if not session.get("otp_verified"):
            return "Verify OTP first"

        name = request.form.get('name')
        department = request.form.get('department')
        email = request.form.get('email')
        uname = request.form.get('uname')
        password = request.form.get('password')

        # Basic validation
        if not all([name, department, email, uname, password]):
            return "All fields are required"

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='1cloud'
        )
        cursor = conn.cursor()

        # ✅ DUPLICATE CHECK
        cursor.execute(
            "SELECT * FROM regtb WHERE email=%s OR UserName=%s",
            (email, uname)
        )
        if cursor.fetchone():
            conn.close()
            flash("Staff already registered!", "warning")
            return redirect("/NewUser")

        # ✅ INSERT (Removed subject_handling column)
        cursor.execute("""
            INSERT INTO regtb
            (name, department, email, UserName, Password)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, department, email, uname, password))

        conn.commit()
        conn.close()

        # clear OTP session
        session.pop("otp_verified", None)

        flash("Staff Registration Successful!", "success")
        return redirect("/NewUser")


    return render_template('register.html')

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        # basic validation
        if not username or not password:
            return render_template('stud.html', error="Please enter Username and Password")

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()

        # SAFE QUERY
        cursor.execute("SELECT * FROM regtb WHERE UserName=%s AND Password=%s", (username, password))
        data = cursor.fetchone()

        if data:
            session['uname'] = username
            cursor.execute("SELECT * FROM regtb WHERE UserName=%s", (username,))
            data = cursor.fetchall()
            return render_template('UserHome.html', data=data)
        else:
            return render_template('stud.html', error="Invalid Username or Password")

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        if not username or not password:
            return render_template('admin.html', error="Please enter Username and Password")

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM admintb WHERE UserName=%s AND Password=%s", (username, password))
        data = cursor.fetchone()

        if data:
            session['uname'] = username
            cursor.execute("SELECT * FROM regtb")
            data = cursor.fetchall()
            return render_template('AdminHome.html', data=data)
        else:
            return render_template('admin.html', error="Invalid Username or Password")

@app.route("/userhome")
def UserHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where  UserName= '" + uname + "' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)
@app.route("/fileupload")
def fileupload():
    return render_template('Fileupload.html')
@app.route("/upload1", methods=['GET', 'POST'])
def upload1():
    if request.method == 'POST':

        # 🔹 Form Fields (NO department from form)
        subject = request.form.get('subject')
        year = request.form.get('year')
        description = request.form.get('description')
        staff_name = session.get('uname')

        if not staff_name:
            return redirect("/UserLogin")

        # 🔥 GET DEPARTMENT FROM STAFF TABLE
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='1cloud'
        )
        cur = conn.cursor()

        cur.execute(
            "SELECT department FROM regtb WHERE UserName=%s",
            (staff_name,)
        )
        dept_data = cur.fetchone()

        if not dept_data:
            conn.close()
            return "Staff department not found"

        department = dept_data[0]
        conn.close()

        # ========= SAVE FILE =========
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(filename)

        # ========= ENCRYPT FILE =========
        key = Fernet.generate_key()
        cipher = Fernet(key)

        with open(filename, 'rb') as file:
            encrypted_data = cipher.encrypt(file.read())

        with open(filename, 'wb') as file:
            file.write(encrypted_data)

        encryption_key = key.decode()
        file_size = os.path.getsize(filename)

        # ========= STORE IN DATABASE =========
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='1cloud'
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO file
            (subject, year, staff_name, filename, file_size, prkey, department, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            subject,
            year,
            staff_name,
            filename,
            file_size,
            encryption_key,
            department,
            description
        ))

        conn.commit()
        conn.close()

        # ========= GET STAFF EMAIL =========
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='1cloud'
        )
        cur = conn.cursor()
        cur.execute("SELECT email FROM regtb WHERE UserName=%s", (staff_name,))
        staff_data = cur.fetchone()
        conn.close()

        if staff_data:
            staff_email = staff_data[0]

            yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')
            yag.send(
                to=staff_email,
                subject="Your Material Encryption Key",
                contents=f"Encryption Key for your uploaded material:\n\n{encryption_key}"
            )

        flash("Material uploaded successfully!", "success")
        return redirect("/fileupload")

@app.route("/viewfile")
def viewfile():
    uname = session.get('uname')

    if not uname:
        return redirect("/UserLogin")

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='1cloud'
    )

    cur = conn.cursor(dictionary=True)

    # 🔥 Case-insensitive safe matching
    cur.execute("""
        SELECT id, filename, description, year
        FROM file
        WHERE LOWER(staff_name) = LOWER(%s)
    """, (uname,))

    data = cur.fetchall()

    conn.close()

    print("Logged user:", uname)
    print("Fetched rows:", data)

    return render_template("viewfile.html", data=data)
@app.route("/dwonload")
def dwonload():
    pid = request.args.get('pid')
    uname = session['uname']
    path=pid
    return send_file(path, as_attachment=True)
@app.route("/delete_file")
def delete_file():
    fid = request.args.get('id')

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cursor = conn.cursor()

    # get filename before deleting
    cursor.execute("SELECT filename FROM file WHERE id=%s", (fid,))
    data = cursor.fetchone()

    if data:
        filename = data[0]

        # delete from DB
        cursor.execute("DELETE FROM file WHERE id=%s", (fid,))
        conn.commit()

        # delete from folder
        import os
        if os.path.exists(filename):
            os.remove(filename)

    conn.close()

    return redirect(request.referrer)

@app.route("/dwonload1")
def dwonload1():
    pid = request.args.get('pid')
    session['fid']=pid
    uname = session['uname']
    path=pid
    return render_template('key.html')
@app.route("/fkey", methods=['GET', 'POST'])
def fkey():
    error = None
    if request.method == 'POST':
        filekey = request.form['filekey']
        print(filekey)
        fid = session['fid']
        print(fid)
        uname = session['uname']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()
        cursor.execute("SELECT * from file where id='" + str(fid) + "' and prkey='" + str(filekey) + "'")
        data = cursor.fetchone()
        if data is None:
            import socket
            h_name = socket.gethostname()
            IP_addres = socket.gethostbyname(h_name)
            print("Host Name is:" + h_name)
            print("Computer IP Address is:" + IP_addres)
            import datetime
            date = datetime.datetime.now()
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO attacker1 VALUES ('','" + h_name + "','" + IP_addres + "','" + str(date) + "')")
            conn.commit()
            conn.close()
            flash("Invalid key entered!", "danger")
            return redirect("/userdwonload1")
        else:
            path = data[4]
            return send_file(path, as_attachment=True)
@app.route("/userrequest")
def userrequest():
    uname = session['uname']

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cur = conn.cursor()

    # ✅ show only pending
    cur.execute("""
    SELECT id, fname, details, uname, filename
    FROM userfilerequest
    WHERE oname=%s AND status='Waiting'
""", (uname,))

    data = cur.fetchall()
    conn.close()

    return render_template('userquest.html', data=data)
@app.route("/revoke")
def revoke():
    rid = request.args.get("id")   # request id

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cur = conn.cursor()

    # remove access + destroy key
    cur.execute("""
        UPDATE userfilerequest
        SET status='Revoked', prkey=''
        WHERE id=%s
    """, (rid,))

    conn.commit()
    conn.close()

    return redirect("/accepted_users")


@app.route("/Datauser")
def Datauser():

    return render_template('datauserlogin.html')
@app.route("/datauserregister")
def datauserregister():

    return render_template('datauserregister.html')

@app.route("/datauserlogin", methods=['GET', 'POST'])
def datauserlogin():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('password')

        if not username or not password:
            return render_template('datauserlogin.html', error="Please enter Username and Password")

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()

        # SAFE QUERY
        cursor.execute("SELECT * FROM userregtb WHERE UserName=%s AND Password=%s", (username, password))
        data = cursor.fetchone()

        if data:
            session['duname'] = username
            cursor.execute("SELECT * FROM userregtb WHERE UserName=%s", (username,))
            data = cursor.fetchall()
            return render_template('DataUserHome.html', data=data)
        else:
            return render_template('datauserlogin.html', error="Invalid Username or Password")


@app.route("/rNewDataUser", methods=['GET', 'POST'])
def rNewDataUser():
    if request.method == 'POST':

        if not session.get("otp_verified"):
            return "Verify OTP first"

        name = request.form.get('name')
        gender = request.form.get('gender')
        regno = request.form.get('register_number')
        year = request.form.get('year')
        department = request.form.get('department')
        email = request.form.get('email')
        uname = request.form.get('uname')
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM userregtb WHERE email=%s OR UserName=%s OR register_number=%s",
            (email, uname, regno)
        )
        if cursor.fetchone():
            conn.close()
            flash("User already exists!", "warning")
            return redirect("/datauserregister")

        cursor.execute("""
            INSERT INTO userregtb
            (name, gender, register_number, year_of_study, department, email, UserName, Password)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (name, gender, regno, year, department, email, uname, password))

        conn.commit()
        conn.close()

        session.pop("otp_verified", None)
        flash("Student registered successfully!", "success")
        return redirect("/datauserregister")

    return render_template('datauserregister.html')


@app.route("/datauserhome")
def datauserhome():

            conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
            cur1 = conn1.cursor()
            cur1.execute("SELECT * FROM userregtb where UserName='"+ session['duname'] +"' ")
            data = cur1.fetchall()
            # return 'file register successfully'
            # return render_template('order.html', data=data)
            return render_template('DataUserHome.html',data=data)


@app.route("/datauserfile")
def datauserfile():

    uname = session['duname']

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='1cloud'
    )
    cur = conn.cursor()

    # 🔹 Get student's year AND department
    cur.execute(
        "SELECT year_of_study, department FROM userregtb WHERE UserName=%s",
        (uname,)
    )
    student = cur.fetchone()

    if not student:
        conn.close()
        return "Student not found"

    student_year = student[0]
    student_department = student[1]

    # 🔹 Filter by year AND department
    cur.execute("""
        SELECT id, subject, description, staff_name, filename
        FROM file
        WHERE year=%s AND department=%s
    """, (student_year, student_department))

    data = cur.fetchall()
    conn.close()

    return render_template('DataUserFile.html', data=data)

@app.route("/Requestfile")
def Requestfile():
    pid = request.args.get('pid')
    session['fid'] = pid
    uname = session['duname']   # requester username

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur = conn.cursor()

    # ================= GET REQUESTER EMAIL =================
    cur.execute("SELECT Email FROM userregtb WHERE UserName=%s", (uname,))
    requester = cur.fetchone()
    requester_email = requester[0]

    # ================= GET FILE DETAILS ====================
    cur.execute("SELECT * FROM file WHERE id=%s", (pid,))
    file_data = cur.fetchone()

    if file_data is None:
        return "No record found"

    fname = file_data[1]
    details = file_data[2]
    oname = file_data[3]   # owner username
    filename = file_data[4]
    # prkey = file_data[7]

    # ================= SAVE REQUEST ========================
    cur.execute("""
INSERT INTO userfilerequest
VALUES ('', %s, %s, %s, %s, %s, %s, %s, %s, 'Waiting')
""", (pid, fname, details, oname, filename, '', uname, requester_email))

    conn.commit()

    # ================= GET OWNER EMAIL =====================
    cur.execute("SELECT Email FROM regtb WHERE UserName=%s", (oname,))
    owner = cur.fetchone()
    owner_email = owner[0]

    conn.close()

    # ================= SEND EMAIL TO OWNER =================
    import yagmail

    yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')

    subject = "File Access Request"

    body = f"""
Hello {oname},

User '{uname}' has requested access to your file.

File Name : {fname}
Details   : {details}

Please login to your account to Accept or Reject the request.

Thank You.
"""

    yag.send(to=owner_email, subject=subject, contents=body)

    print("Mail sent to owner!")

    return "Request Sent To Owner Successfully"


@app.route("/datauserviewfile")
def datauserviewfile():
    uname=session['duname']
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM userfilerequest where uname='"+uname+"' ")
    data = cur1.fetchall()
    # return 'file register successfully'
    # return render_template('order.html', data=data)
    return render_template('datauserviewfile.html', data=data)

@app.route("/userdwonload1")
def userdwonload1():
    pid = request.args.get('pid')
    session['ffid']=pid
    uname = session['duname']
    path=pid
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM userfilerequest where uname='" + uname + "' and id='"+pid+"' and status='Accepted' ")
    data = cur1.fetchone()
    if data is None:
        return "File Not Dwonlaod"
    else:
        return render_template('key1.html')



@app.route("/fkey1", methods=['GET', 'POST'])
def fkey1():
    if request.method == 'POST':

        user_key = request.form['filekey']
        fid = session['ffid']
        attacker_name = session['duname']

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='1cloud'
        )
        cursor = conn.cursor()

        # ✅ Verify personal key
        cursor.execute(
            "SELECT * FROM userfilerequest WHERE id=%s AND prkey=%s",
            (fid, user_key)
        )
        data = cursor.fetchone()

        # ================= WRONG KEY =================
        if data is None:
            import socket, datetime

            ip = socket.gethostbyname(socket.gethostname())
            date = datetime.datetime.now()

            # 🔹 Get attacker (student) info
            cursor.execute(
                "SELECT email, register_number, department FROM userregtb WHERE UserName=%s",
                (attacker_name,)
            )
            udata = cursor.fetchone()

            if udata:
                email = udata[0]
                register_number = udata[1]
                department = udata[2]
            else:
                email = "unknown"
                register_number = "unknown"
                department = "unknown"

            # 🔹 Get file + owner info
            cursor.execute(
                "SELECT oname, filename FROM userfilerequest WHERE id=%s",
                (fid,)
            )
            rdata = cursor.fetchone()

            if rdata:
                owner = rdata[0]
                filename = rdata[1]
            else:
                owner = "unknown"
                filename = "unknown"

            # 🔹 Save attack log
            cursor.execute("""
                INSERT INTO attacker1
                (uname, email, register_number, department, owner, filename, ip, date)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (attacker_name, email, register_number, department,
                  owner, filename, ip, str(date)))

            conn.commit()

            # 🔹 Send alert email to staff
            cursor.execute(
                "SELECT email FROM regtb WHERE UserName=%s",
                (owner,)
            )
            owner_data = cursor.fetchone()

            if owner_data:
                owner_email = owner_data[0]

                yag = yagmail.SMTP(
                    'your_email@gmail.com',
                    'your_app_password'
                )

                subject = "🚨 ALERT: Unauthorized Material Access Attempt"

                body = f"""
Hello {owner},

⚠ SECURITY ALERT ⚠

A student entered a WRONG ACCESS KEY for your material.

========== ATTACK DETAILS ==========
Student Username : {attacker_name}
Email            : {email}
Register Number  : {register_number}
Department       : {department}

Material File    : {filename}
Request ID       : {fid}

IP Address       : {ip}
Time             : {date}
====================================

Please review this activity immediately.

Regards,
NETGUARD Security System
"""

                yag.send(
                    to=owner_email,
                    subject=subject,
                    contents=body
                )

                print("Alert mail sent to staff!")

            conn.close()
            return "Key Invalid"

        # ================= CORRECT KEY =================
        else:
            filename = data[5]
            file_id = data[1]

            cursor.execute(
                "SELECT prkey FROM file WHERE id=%s",
                (file_id,)
            )
            real_key = cursor.fetchone()[0]

            cipher = Fernet(real_key.encode())

            with open(filename, 'rb') as f:
                encrypted_data = f.read()

            decrypted_data = cipher.decrypt(encrypted_data)

            temp_path = "temp_" + filename
            with open(temp_path, 'wb') as f:
                f.write(decrypted_data)

            conn.close()

            return send_file(temp_path, as_attachment=True)


@app.route("/delete_owner")
def delete_owner():
    uid = request.args.get('id')

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM regtb WHERE id=%s", (uid,))
    conn.commit()
    conn.close()
    # import redirect
    return redirect("/AdminHome")

@app.route("/delete_user")
def delete_user():
    uid = request.args.get('id')

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cursor = conn.cursor()

    cursor.execute("DELETE FROM userregtb WHERE id=%s", (uid,))
    conn.commit()
    conn.close()

    return "User Deleted Successfully"

@app.route("/accept")
def accept():
    pid = request.args.get('pid')

    import random, string
    def generate_key(size=6):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

    new_key = generate_key()   # ✅ unique per user

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur = conn.cursor()

    cur.execute("SELECT * FROM userfilerequest WHERE id=%s", (pid,))
    data = cur.fetchone()

    if data is None:
        return "File Not Found"

    email = data[8]

    # ✅ store personal key
    cur.execute(
        "UPDATE userfilerequest SET status='Accepted', prkey=%s WHERE id=%s",
        (new_key, pid)
    )

    conn.commit()
    conn.close()

    # ✅ send mail
    yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')

    subject = "Your File Download Key"
    body = "Key --- " + new_key

    yag.send(to=email, subject=subject, contents=body)

    print("Personal key sent!")

    return "User Request Accepted Successfully"



        # return render_template('key1.html')
import random

@app.route("/send_otp", methods=['POST'])
def send_otp():
    email = request.form['email']

    otp = random.randint(100000, 999999)
    session['otp'] = str(otp)

    yag = yagmail.SMTP('your_email@gmail.com', 'your_app_password')
    yag.send(
        to=email,
        subject="NETGUARD OTP",
        contents=f"Your OTP is {otp}"
    )

    return "OTP Sent"
@app.route("/verify_otp", methods=['POST'])
def verify_otp():
    entered = request.form['otp']

    if entered == session.get('otp'):
        session['otp_verified'] = True
        return "success"
    else:
        return "fail"


@app.route("/accepted_users")
def accepted_users():
    uname = session['uname']   # owner

    conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='1cloud'
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM userfilerequest
        WHERE oname=%s AND status='Accepted'
    """, (uname,))

    data = cur.fetchall()
    conn.close()

    return render_template("accepted_users.html", data=data)

@app.route("/reject")
def reject():
    pid = request.args.get('pid')


    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM userfilerequest where id='"+pid+"'")
    data = cur1.fetchone()
    if data is None:
        return "File Not Dwonlaod"
    else:
        email=data[8]
        pkey=data[6]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloud')
        cursor = conn.cursor()
        cursor.execute(
            "update userfilerequest set status='reject' where id='"+pid+"'")
        conn.commit()
        conn.close()
        mail = 'your_email@gmail.com';
        password = 'your_app_password';
        # list of email_id to send the mail
        li = [email]
        body = "Key---" + pkey

        yag = yagmail.SMTP(mail, password)

        for dest in li:
            yag.send(
                to=dest,
                subject="File Owner Reject for your File Access Request...!",
                contents=body,

            )
        print("Mail sent to all...!")
        return 'User Request rejected successfully'


        return render_template('key1.html')


@app.route("/checkfile")
def checkfile():
    fname = request.args.get('id')
    str(fname)



    import os
    import time

    # Specify the file path
    file_path = fname

    # Check if the file exists
    if os.path.exists(file_path):
        # Get the last modified time of the file
        last_modified_time = os.path.getmtime(file_path)

        # Get the current time
        current_time = time.time()

        # Define a threshold (e.g., 60 seconds or 1 minute)
        threshold = 60  # in seconds

        # Check if the file was modified within the last threshold period
        if current_time - last_modified_time < threshold:
            p="The file '"+str(file_path)+"' has been modified in the last '"+str(threshold)+"' seconds."
            print(f"The file {file_path} has been modified in the last {threshold} seconds.")
        else:
            p="The file '"+str(file_path)+"' has NOT been modified in the last '"+str(threshold)+"' seconds."
            print(f"The file {file_path} has NOT been modified in the last {threshold} seconds.")
    else:
        p="The file '"+str(file_path)+"' does not exist."
        print(f"The file {file_path} does not exist.")

    return p


def main():
    app.run(debug=True, use_reloader=True)
if __name__ == '__main__':
    main()