import requests
import sys

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'

def add_instructor(instructor_id, name, department):

    data = {'name': name, 'department': department}

    resp = requests.put(firebase_url + f'/Instructors/{instructor_id}.json', json=data)

    if resp.status_code == 200:
        print(f"Instructor {name} added successfully.")
    else:
        print(f"Error adding Instructor: {resp.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
    else:
        instructor_id, name, department = sys.argv[1], sys.argv[2], sys.argv[3]
        add_instructor(instructor_id, name, department)