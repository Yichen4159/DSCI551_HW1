import requests
import sys

firebase_url = 'https://enrollment-system-18ede-default-rtdb.firebaseio.com/'

def add_student(student_id, name, program):

    data = {'name': name,'program': program}

    resp = requests.put(firebase_url + f'/Students/{student_id}.json', json=data)

    if resp.status_code == 200:
        print(f"Student {name} added successfully.")
    else:
        print(f"Error adding student: {resp.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 add_student.py <student_id> <name> <program>")
    else:
        student_id, name, program = sys.argv[1], sys.argv[2], sys.argv[3]
        add_student(student_id, name, program)