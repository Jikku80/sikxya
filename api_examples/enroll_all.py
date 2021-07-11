import requests

username = 'roma'
password = 'jikku123'

base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'Avalable Courses: {available_courses}')

for course in courses:
	course_id = course['id']
	course_title = course['title']
	r = requests.post(f'{base_url}courses/{course_id}/enroll/', auth=(username, password))
	if r.status_code == 200:
		print(f'Successfully enrolled in {course_title}')