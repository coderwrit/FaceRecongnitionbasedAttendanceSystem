import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionbasedattendan-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')
data = {
    "2105849":
        {
            "name": "Writankar Biswas",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "21052492":
        {
            "name": "Debarghya Bandyopadhyay",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 12,
            "hostel": "KP6C",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105831":
        {
            "name": "Soham Patra",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "21052843":
        {
            "name": "Misbahur Rahman",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105833":
        {
            "name": "Sourin Mukherjee",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105846":
        {
            "name": "Utkal Sahoo",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105832":
        {
            "name": "Soumyendu Das",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105829":
        {
            "name": "Shubham Pal",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP15",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105847":
        {
            "name": "Vishal Banerjee",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP9",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105848":
        {
            "name": "Vivesh Singh",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP14",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "2105792":
        {
            "name": "Harsh Dubey",
            "branch": "CSE",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "KP6",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "852741":
        {
            "name": "Enola Holmes",
            "branch": "Actor",
            "starting_year": 2021,
            "total_attendance": 7,
            "hostel": "NA",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)