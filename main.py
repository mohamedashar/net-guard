from flask import Flask, render_template, flash, request, session,send_file,jsonify
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
import time
import matplotlib.pyplot as plt
import io
import base64

holland_questions = {
    "R": [
        "I enjoy working with machines and tools.",

    "Lay brick or tile",
    "Work on an offshore oil-drilling rig"

    ],
    "I": [
        "I enjoy solving puzzles and brain teasers.",

        "I enjoy analyzing data to find patterns and trends.",
"Study the structure of the human body",


    ],
    "A": [
        "I enjoy drawing, painting, or creating visual art.",
        "I like expressing myself through music or dance.",

    "Write a song",


    ],
    "S": [
        "I enjoy helping people solve their problems.",
        "I like volunteering and contributing to my community.",
        "I enjoy teaching and educating others.","Give career guidance to people",


    ],
    "E": [
        "I enjoy taking on leadership roles and responsibilities.",
        "I like persuading and convincing others.",
        "I like organizing events and gatherings.","Sell restaurant franchises to individuals",


    ],
    "C": [
        "I prefer working with numbers and data.",
        "I like creating and following organized systems.",
        "I enjoy record-keeping and data analysis.","Inventory supplies using a hand-held computer",


    ]
}

# Define information and career recommendations for each Holland Personality Type
personality_info = {
    "R": {
        "name": "Realistic",
        "description": "Realistic individuals are practical, hands-on, and enjoy working with tools and machines.",
        "careers": [
            "Carpenter",
            "Electrician",
            "Mechanic",
            "Plumber",
            "Welder"
        ]
    },
    "I": {
        "name": "Investigative",
        "description": "Investigative individuals are analytical and enjoy solving complex problems.",
        "careers": [
            "Scientist",
            "Engineer",
            "Researcher",
            "Computer Programmer",
            "Mathematician"
        ]
    },
    "A": {
        "name": "Artistic",
        "description": "Artistic individuals are creative and enjoy expressing themselves through art and design.",
        "careers": [
            "Artist",
            "Graphic Designer",
            "Writer",
            "Interior Designer",
            "Photographer"
        ]
    },
    "S": {
        "name": "Social",
        "description": "Social individuals are compassionate and enjoy helping and caring for others.",
        "careers": [
            "Teacher",
            "Social Worker",
            "Nurse",
            "Counselor",
            "Psychologist"
        ]
    },
    "E": {
        "name": "Enterprising",
        "description": "Enterprising individuals are ambitious and enjoy leadership roles and entrepreneurship.",
        "careers": [
            "Entrepreneur",
            "Sales Manager",
            "Marketing Manager",
            "Business Consultant",
            "Politician"
        ]
    },
    "C": {
        "name": "Conventional",
        "description": "Conventional individuals are detail-oriented and enjoy organizing and managing tasks and data.",
        "careers": [
            "Accountant",
            "Financial Analyst",
            "Data Analyst",
            "Office Manager",
            "Banker"
        ]
    }
}

aptitude_questions = [
    "What is 15 + 32?",
    "Solve: 3x + 5 = 20",
    "What is the square root of 256?",
    "What is the value of π (Pi) rounded to two decimal places?",
    "A car travels 60 km in 1 hour. How far will it travel in 5 hours?",
    "What is the area of a rectangle with length 10 cm and width 5 cm?",
    "If a triangle has sides of 3 cm, 4 cm, and 5 cm, what is the area?",
    "What is the volume of a cube with a side length of 4 cm?",
    "Solve the equation: 2x + 4 = 18.",
    "What is the derivative of the function f(x) = 2x² + 3x?"
]

# Define the correct answers
correct_answers = [
    47, 5, 16, 3.14, 300, 50, 6, 64, 7, 4
]

# Career recommendations based on score
career_recommendations = {
    "Low": [
        "Humanities: Teacher, Social Worker",
        "Arts: Artist, Writer, Musician",
        "Sales: Retail, Customer Service"
    ],
    "Moderate": [
        "Design: Graphic Designer, Marketing",
        "Healthcare: Nursing, Medical Assistant",
        "Sales & Marketing"
    ],
    "High": [
        "Engineering: Mechanical, Computer",
        "Data Science, Finance, Research & Development",
        "Business Strategy: Consultant, Product Manager"
    ]
}


# Calculate total score
def calculate_score(answers):
    score = 0
    for idx, answer in enumerate(answers):
        if float(answer) == correct_answers[idx]:
            score += 1
    return score


# Display career recommendations based on score
def get_career_category(score):
    if score <= 8:
        return "Low"
    elif 9 <= score <= 14:
        return "Moderate"
    else:
        return "High"


app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
cumulative_scores = {}
question_times = {}
def generate_score_chart1(score):
    categories = ['Low', 'Moderate', 'High']
    scores = [score <= 8, 9 <= score <= 14, score > 14]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(categories, scores, color=['red', 'orange', 'green'])

    ax.set_ylabel('Number of Students')
    ax.set_title('Aptitude Score Distribution')

    # Save chart as image in memory
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Encode image in base64
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')

    return img_base64

def generate_donut_chart():
    # Make sure the labels are a list of strings
    labels = [personality_info[ptype]['name'] for ptype in cumulative_scores.keys()]
    scores = list(cumulative_scores.values())

    # Make sure that the labels and scores are correct and not empty
    print(labels)  # This is just to help you debug, remove it after testing

    # Calculate percentages
    total_score = sum(scores)
    percentages = [(score / total_score) * 100 for score in scores]

    # Create a donut chart
    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(center_circle)

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save to a bytes buffer
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Encode to base64 to send to HTML
    chart = base64.b64encode(img_buf.getvalue()).decode('utf8')

    return chart, labels  # Return the chart and labels



@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/adminlogin")
def adminlogin():
    return render_template('adminlogin.html')


@app.route("/adminhome")
def adminhome():
    return render_template('adminhome.html')

@app.route("/stdview")
def stdview():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()

    return render_template('stdview.html',data=data)

@app.route("/train")
def train():
    #import trainmodel
    return render_template('tainmodel.html')
@app.route("/adlogin", methods=['GET', 'POST'])
def adlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM register ")
           data = cur.fetchall()

           return render_template('adminhome.html',data=data)

       else:
        return render_template('index.html', error=error)
@app.route("/modeltrain", methods=['GET', 'POST'])
def modeltrain():
    error = None
    if request.method == 'POST':
        file = request.form['file']
        import pandas as pd
        from sklearn.preprocessing import LabelEncoder
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score, classification_report
        import joblib

        # Load the data
        data = pd.read_csv("stud.csv")

        # Label encoding for the target variable 'Courses'
        label_encoder = LabelEncoder()
        data['Courses_label'] = label_encoder.fit_transform(data['Courses'])

        # Handle categorical features and apply label encoding
        categorical_columns = [
            'Drawing', 'Dancing', 'Singing', 'Sports', 'Video Game', 'Acting',
            'Travelling', 'Gardening', 'Animals', 'Photography', 'Teaching',
            'Exercise', 'Coding', 'Electricity Components', 'Mechanic Parts',
            'Computer Parts', 'Researching', 'Architecture', 'Historic Collection',
            'Botany', 'Zoology', 'Physics', 'Accounting', 'Economics', 'Sociology',
            'Geography', 'Psycology', 'History', 'Science', 'Bussiness Education',
            'Chemistry', 'Mathematics', 'Biology', 'Makeup', 'Designing', 'Content writing',
            'Crafting', 'Literature', 'Reading', 'Cartooning', 'Debating', 'Asrtology',
            'Hindi', 'French', 'English', 'Urdu', 'Other Language', 'Solving Puzzles',
            'Gymnastics', 'Yoga', 'Engeeniering', 'Doctor', 'Pharmisist', 'Cycling',
            'Knitting', 'Director', 'Journalism', 'Bussiness', 'Listening Music'
        ]

        label_encoders = {}
        for col in categorical_columns:
            label_encoder = LabelEncoder()
            data[col] = label_encoder.fit_transform(data[col])
            label_encoders[col] = label_encoder

        # Separate features and target
        X = data[categorical_columns]
        Y = data['Courses_label']

        # Train and Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

        # Initialize and train the RandomForestClassifier model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        classification_rep = classification_report(y_test, y_pred)

        # Save the trained model and label encoders
        joblib.dump(model, 'model.pkl')
        joblib.dump(label_encoders, 'label_encoders.pkl')
        data="Training Complete! Model Accuracy: '"+str(accuracy)+"'"


        print(f"Training Complete! Model Accuracy: {accuracy:.2f}")

        return render_template('modelresult.html', data=data)

@app.route("/user")
def user():
    return render_template('userlogin.html')
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['fname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('404.html', data=alert)
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            return render_template('userhome.html', data=username)


@app.route("/userregister", methods=['GET', 'POST'])
def userregister():
    if request.method == 'POST':
        name1 = request.form['name']
        gender = request.form['gender']

        email = request.form['email']

        phone = request.form['phone']

        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        dob = request.form['dob']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO register VALUES ('','" + name1 + "','" + gender + "','"+dob+"','" + address + "','" + email + "','" + phone + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()

    return render_template('userlogin.html')

@app.route("/userhome")
def userhome():
    uname=session['fname']
    return render_template('userhome.html',data=uname)

@app.route("/testcareer")
def testcareer():
    uname=session['fname']
    print(holland_questions)


    return render_template('test.html',data=uname,questions=holland_questions)
@app.route('/submit', methods=['POST'])
def submit():
    global cumulative_scores
    cumulative_scores = {key: 0 for key in holland_questions.keys()}
    question_times.clear()

    # Collect responses and calculate time spent on each question
    for personality_type, questions in holland_questions.items():
        for i, question in enumerate(questions):
            choice = int(request.form.get(f'{personality_type}_{i}'))
            time_spent_str = request.form.get(f'{personality_type}_{i}_time')
            try:
                time_spent = float(time_spent_str) if time_spent_str else 0.0
            except ValueError:
                time_spent = 0.0

            cumulative_scores[personality_type] += choice
            question_times[f'{personality_type}_{i}'] = time_spent

    # Determine the dominant personality
    dominant_personality = max(cumulative_scores, key=cumulative_scores.get)

    # Get personality type information
    personality_type_info = personality_info[dominant_personality]

    # Generate the donut chart and labels
    chart, labels = generate_donut_chart()

    # Calculate total time spent
    total_time_spent = sum(question_times.values())

    # Render the results template and pass all necessary variables
    session['result_text']=personality_type_info['name']
    r = session['result_text']
    session['r']=r
    print(r)
    session['total_time_spent']=total_time_spent
    session['chart']=chart
    session['personality_type_info']=personality_type_info
    session['labels']=labels

    #return render_template('sample1.html', aptitude_questions=aptitude_questions)

    return render_template("result.html",
                           result_text=f"Your Holland Personality Type is: {personality_type_info['name']}",
                           chart=chart,
                           total_time_spent=total_time_spent,
                           personality_type_info=personality_type_info,
                           labels=labels)  # Ensure labels are passed here

# Function to generate donut chart for personality distribution

@app.route('/question_timer/<personality_type>/<int:question_index>', methods=['GET'])
def question_timer(personality_type, question_index):
    start_time = time.time()  # Record the start time of the question
    return jsonify(start_time=start_time)
@app.route("/updatemark")
def updatemark():
    uname=session['fname']
    return render_template('updatemark.html',data=uname)

@app.route("/updatemark1", methods=['GET', 'POST'])
def updatemark1():
    if request.method == 'POST':
        uname=session['fname']
        tamil = request.form['tamil']
        english = request.form['english']

        subject1 = request.form['subject1']

        subject2 = request.form['subject2']

        subject3 = request.form['subject3']
        subject4 = request.form['subject4']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mark VALUES ('','"+uname+"','" + tamil + "','" + english + "','"+subject1+"','" + subject2 + "','" + subject3 + "','" + subject4 + "','')")
        conn.commit()
        conn.close()

    return render_template('userlogin.html')
@app.route("/view")
def view():
    uname=session['fname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='careerguide')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register where uname='"+uname+"' ")
    data = cur.fetchall()
    return render_template('view.html',data=data)
@app.route('/result1', methods=['GET', 'POST'])
def result1():
    if request.method == 'POST':
        answers = [request.form.get(f"q{i}") for i in range(1, 11)]  # Get answers for the first 10 questions
        score = calculate_score(answers)
        category = get_career_category(score)

        # Generate the chart
        chart = generate_score_chart1(score)

        # Return the results and chart image

        r=session['r']
        print(r)
        t=session['total_time_spent']
        print(t)
        c=session['chart'] = chart
        p=session['personality_type_info']
        print(p)
        l=session['labels']
        print(l)


        return render_template('result.html', category=category, careers1=career_recommendations[category], chart1=chart,result_text='',
                           chart='',
                           total_time_spent= '',
                           personality_type_info='',
                           labels='')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)