from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'courses.json'

# Ensure the JSON file exists, or create it with an empty array
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

# Helper function to read courses from the JSON file
def read_courses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

# Helper function to write courses to the JSON file
def write_courses(courses):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(courses, file, indent=4)
    except Exception as e:
        print(f"Error writing to the file: {e}")

# Helper function to generate a new course ID
def get_next_id(courses):
    return max(course['id'] for course in courses) + 1 if courses else 1

# Load existing data from JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# POST /api/courses - Add a new course
@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    # Validate required fields
    if not all(key in data for key in ['name', 'description', 'target_date', 'status']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate status value
    if data['status'] not in ['Not Started', 'In Progress', 'Completed']:
        return jsonify({'error': 'Invalid status value'}), 400

    # Create a new course entry
    courses = read_courses()
    new_course = {
        'id': get_next_id(courses),
        'name': data['name'],
        'description': data['description'],
        'target_date': data['target_date'],
        'status': data['status'],
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    courses.append(new_course)
    write_courses(courses)
    return jsonify(new_course), 201

# GET /api/courses - Get all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = read_courses()
    return jsonify(courses), 200

# GET /api/courses/<int:course_id> - Get a specific course
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    courses = read_courses()
    # Find the course by ID
    course = next((course for course in courses if course['id'] == course_id), None)
    if course:
        return jsonify(course), 200
    return jsonify({'error': 'Course not found'}), 404

# PUT /api/courses/<int:course_id> - Update a course
@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    courses = read_courses()
    # Find the course to update
    course = next((course for course in courses if course['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    data = request.json
    # Validate status value if it is included
    if 'status' in data and data['status'] not in ['Not Started', 'In Progress', 'Completed']:
        return jsonify({'error': 'Invalid status value'}), 400

    # Update course fields
    for key in ['name', 'description', 'target_date', 'status']:
        if key in data:
            course[key] = data[key]
    write_courses(courses)
    return jsonify(course), 200

# DELETE /api/courses/<int:course_id> - Delete a course
@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    courses = read_courses()
    # Find the course to delete
    course = next((course for course in courses if course['id'] == course_id), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    courses.remove(course)  # Remove the course from the list
    write_courses(courses)  # Write the updated list back to the file
    return jsonify({'message': 'Course deleted'}), 200

# New endpoint to get courses statistics
@app.route('/api/courses/stats', methods=['GET'])
def course_stats():
    courses = load_data()
    total_courses = len(courses)
    status_counts = {
        "Not Started": 0,
        "In Progress": 0,
        "Completed": 0,
    }

    for course in courses:
        status = course['status']
        if status in status_counts:
            status_counts[status] += 1

    return jsonify({
        "total_courses": total_courses,
        "status_counts": status_counts
    })

if __name__ == '__main__':
    app.run(debug=True)