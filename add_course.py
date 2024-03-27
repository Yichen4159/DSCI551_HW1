import sys
import requests

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'

def add_course(course_number,title,semester):

    data = {'title': title, 'semester': semester}

    resp = requests.put(firebase_url + f'/Courses/{course_number}.json', json=data)

    if resp.status_code == 200:
        print(f"Course {course_number} added successfully.")
    else:
        print(f"Error adding course: {resp.status_code}")



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ")
    else:
        course_number, title, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        add_course(course_number, title, semester)