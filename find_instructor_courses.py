import requests
import sys
import json

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'


def find_instructor_courses(instructor_id):

    resp = requests.get(firebase_url + f'/Instructors/{instructor_id}.json')

    if resp.status_code != 200:
        print(f"Error：Invalid instructor id!")
        return

    # Parse the return into json object
    instructor_data = resp.json()
    instructor_name = instructor_data['name']

    # Get student courses information
    resp = requests.get(firebase_url + f'/Instructors/{instructor_id}/courses.json')

    if resp.status_code != 200:
        print(f"Error getting courses information of instructor {instructor_name}!")
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
        'instructor_name': instructor_name,
        'courses': courses_list
    }

    # Dumping json value into string and print it out.

    print(json.dumps(json_data, indent=4))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Invalid input! Please enter valid instructor_id")
    else:
        instructor_id = sys.argv[1]
        find_instructor_courses(instructor_id)
