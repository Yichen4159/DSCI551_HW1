import requests
import sys

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'


def take_course(student_id, course_number, semester):
    # Check if class and student info user provided is valid
    student_resp = requests.get(firebase_url + f'/Students/{student_id}.json')
    course_resp = requests.get(firebase_url + f'/Courses/{course_number}.json')
    # semester_resp = requests.get(firebase_url + f'/Courses/{course_number}/semester.json')

    # Return Error if information are invalid
    if student_resp.status_code != 200 or course_resp.status_code != 200:
        print("Error: Invalid input.")
        return

    course_data = course_resp.json()

    if course_data['semester'] != semester:
        print("Error: Provided semester does not match the course's semester.")
        return

    # Pack data into json object
    data_student = {
        'course_number': course_number,
        'semester': semester
    }

    # Use requests.post command to update 'Students' in real-time Database
    resp = requests.post(firebase_url + f'/Students/{student_id}/courses.json', json=data_student)

    # Return feedbacks
    if resp.status_code == 200:
        print(f"Student {student_id} has enrolled in {course_number} for {semester}")
    else:
        print(f"Error enrolling: {resp.status_code}")

    # Use requests.post command to update 'Courses' in real-time Database
    resp = requests.post(firebase_url + f'/Courses/{course_number}/class_list.json', json=student_id)

    # Return feedbacks
    if resp.status_code == 200:
        print(f"Course {course_number} class_list info has updated")
    else:
        print(f"Error class_list updating: {resp.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("This py file used for student course enrollment, please enter <student_id>, <course_number>, <semester>")
    else:
        student_id, course_number, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        take_course(student_id, course_number, semester)
