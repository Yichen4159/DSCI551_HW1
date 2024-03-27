import requests
import sys

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'


def teach_course(instructor_id, course_number, semester):
    # Check if class and instructor info user provided is valid
    instructor_resp = requests.get(firebase_url + f'/Instructors/{instructor_id}.json')
    course_resp = requests.get(firebase_url + f'/Courses/{course_number}.json')

    # Return Error if information are invalid
    if instructor_resp.status_code != 200 or course_resp.status_code != 200:
        print("Error: Instructor or course not found in the database.")
        return

    course_data = course_resp.json()

    if course_data['semester'] != semester:
        print("Error: Provided semester does not match the course's semester.")
        return

    # Pack data into json object
    data = {
        'course_number': course_number,
        'semester': semester
    }

    # Use requests.post command to update 'Instructors' in real-time Database
    response = requests.post(firebase_url + f'/Instructors/{instructor_id}/courses.json', json=data)

    if response.status_code == 200:
        print(f"Instructor {instructor_id} is teaching course {course_number} for {semester}.")
    else:
        print(f"Error assigning course to the instructor: {response.status_code}")

    # Use requests.post command to update 'Courses' in real-time Database
    resp = requests.post(firebase_url + f'/Courses/{course_number}/instructor.json', json=instructor_id)

    # Return feedbacks
    if resp.status_code == 200:
        print(f"Course {course_number} instructor info has updated")
    else:
        print(f"Error course instructor updating: {resp.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("This py file register instructors to courses they teach, please enter <instructor_id> "
              "<course_number> <semester>")
    else:
        instructor_id, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        teach_course(instructor_id, course_number, semester)
