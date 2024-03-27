import requests
import sys
import json

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'


def find_student_courses(student_id):
    resp = requests.get(firebase_url + f'/Students/{student_id}.json')

    if resp.status_code != 200:
        print(f"Error：Invalid student id!")
        return

    # Parse the return into json object
    student_data = resp.json()
    student_name = student_data['name']

    # Get student courses information
    resp = requests.get(firebase_url + f'/Students/{student_id}/courses.json')

    if resp.status_code != 200:
        print(f"Error getting courses information of student {student_name}!")
        return

    # Parse the return into json object
    courses_data = resp.json()

    #  Create a python list used as json array
    courses_list = []

    # Using a for loop iterate through courses_data's items
    for x, course in courses_data.items():
        courses_list.append({
            'course_number': course['course_number'],
            'semester': course['semester']
        })

    # The first key-value pair is the student_name we get from requests.
    # The second key-value pair has a key "courses", and a value in list.
    json_data = {
        'student_name': student_name,
        'courses': courses_list
    }

    # Dumping json value into string and print it out.

    print(json.dumps(json_data, indent=4))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid input! Please enter valid student_id")
    else:
        student_id = sys.argv[1]
        find_student_courses(student_id)
