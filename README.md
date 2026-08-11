# CodeCraftHub

## Project Overview and Description
CodeCraftHub is a simple personalized learning platform that allows developers to track courses they want to learn. It's built using Python and Flask, providing an easy way to manage study progress through a RESTful API. This project is a great starting point for beginners looking to learn about REST APIs, JSON data handling, and Flask web development.

## Features
- **Create Courses**: Add new courses with a name, description, target completion date, and status.
- **Retrieve Courses**: Get a list of all courses or retrieve details of a specific course.
- **Update Courses**: Modify existing course information, including the status of the course.
- **Delete Courses**: Remove courses from your list.
- **JSON Data Storage**: All course data is stored in a simple JSON file.

## Installation Instructions
Follow these steps to set up CodeCraftHub on your local machine:

1. **Prerequisites**: Ensure you have Python 3.x installed on your machine. You can download it from [the official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/CodeCraftHub.git
   cd CodeCraftHub

1. Create a Virtual Environment (recommended):
    ```bash
    python -m venv venv

2. Activate the Virtual Environment:
    On Windows:
        ```bash
        venv\Scripts\activate
    On macOS/Linux:
        ```bash
        source venv/bin/activate

3. Install Dependencies: Make sure you have Flask installed:
    ```bash
    pip install Flask

4. Create the JSON Data File: The application will automatically generate a courses.json file when you run the app for the first time. There's no need for manual setup.

## How to Run the Application

To start the CodeCraftHub API, simply run the following command:
    ```bash
    python app.py

The application should display a message indicating it is running, typically at http://127.0.0.1:5000.

## API Endpoints Documentation

Here's a list of available API endpoints and examples of how to use them.

1. POST /api/courses
    Add a new course.
    Request Example:

        ```bash
        curl -X POST http://127.0.0.1:5000/api/courses \
            -H "Content-Type: application/json" \
            -d '{
                "name": "Introduction to Python",
                "description": "Learn the basics of Python programming.",
                "target_date": "2023-12-31",
                "status": "Not Started"
                }'
        

Expected Response (Successful):

    {
        "id": 1,
        "name": "Introduction to Python",
        "description": "Learn the basics of Python programming.",
        "target_date": "2023-12-31",
        "status": "Not Started",
        "created_at": "2023-10-07 12:00:00"
    }

2. GET /api/courses
    Retrieve all courses.
    Request Example:

        ```bash
        curl -X GET http://127.0.0.1:5000/api/courses


Expected Response (Successful):

    [
        {
            "id": 1,
            "name": "Introduction to Python",
            "description": "Learn the basics of Python programming.",
            "target_date": "2023-12-31",
            "status": "Not Started",
            "created_at": "2023-10-07 12:00:00"
        }
    ]

3. GET /api/courses/int:course_id
    Retrieve a specific course by ID.
    Request Example:

        ```bash
        curl -X GET http://127.0.0.1:5000/api/courses/1


Expected Response (Successful):

    {
        "id": 1,
        "name": "Introduction to Python",
        "description": "Learn the basics of Python programming.",
        "target_date": "2023-12-31",
        "status": "Not Started",
        "created_at": "2023-10-07 12:00:00"
    }


4. PUT /api/courses/int:course_id
    Update a specific course by ID.
    Request Example:

        ```bash
        curl -X PUT http://127.0.0.1:5000/api/courses/1 \
        -H "Content-Type: application/json" \
        -d '{
            "status": "In Progress"
            }'


Expected Response (Success):

    {
        "id": 1,
        "name": "Introduction to Python",
        "description": "Learn the basics of Python programming.",
        "target_date": "2023-12-31",
        "status": "In Progress",
        "created_at": "2023-10-07 12:00:00"
    }


5. DELETE /api/courses/int:course_id
    Delete a course by ID.
    Example Request:

        ```bash
        curl -X DELETE http://127.0.0.1:5000/api/courses/1


Expected Response (Success):

    {
        "message": "Course deleted"
    }


6. GET /api/courses/stats
    Get statistics about courses.
    This endpoint returns the total number of courses and gives a count of courses by their current status.
    Example Request:
    
        ```bash
        curl -X GET http://127.0.0.1:5000/api/courses/stats

Expected Response (Success):

    {
        "total_courses": 3,
        "status_counts": {
            "Not Started": 1,
            "In Progress": 1,
            "Completed": 1
        }
    }

- total_courses: The total number of courses in the system.
- status_counts: An object that counts the courses based on their status ("Not Started", "In Progress", "Completed").

## Testing Instructions
To ensure everything is functioning correctly, you can test the API endpoints using the provided curl commands. Here are steps to run the tests:

1. Run the Flask Application: Make sure your application is up and running as described in the "How to Run the Application" section.

2. Execute Each CURL Command: Copy and paste each curl command from the API documentation section into your terminal to test each endpoint. Ensure that you do the following:
    - Use POST to create courses first before trying to GET, PUT, or DELETE .
    - Adjust the "course_id" in PLACEHOLDER to match the ID of courses you have created.

3. Check Responses: Verify that the expected responses match the actual responses you get after running the curl commands.

## Troubleshooting Common Issues
If you encounter issues while working with CodeCraftHub, consider the following common problems:

- Flask Application Not Running: Ensure you ran the application using the command "python app.py". Look for any errors in the terminal for clues if it fails to start.

- Invalid JSON Payloads: When making POST and PUT requests, make sure that your JSON payload is well-formed and contains all necessary fields (name, description, target_date, status).

- File Permission Issues: If you're having trouble with "courses.json", ensure that the file has the right read/write permissions for the user running the Flask app.

- Port Already in Use: If you receive an error that the port is already in use, check if another application is using port 5000. You can change the Flask app's port by modifying the run command:
    app.run(port=5001)  # Change 5001 to any available port

## Project Structure Explanation
Here is an overview of the project structure for CodeCraftHub:
```bash
CodeCraftHub/
│
├── app.py                # The main application file containing all Flask routes and logic
├── courses.json          # JSON file storing all course data (auto-generated by the app)
└── README.md             # This documentation file

- app.py
    : Contains all the routes and logic for the REST API. It handles incoming requests, processes data, and returns the appropriate responses.
- courses.json
    : The file where all created courses are stored in JSON format. The app will create it automatically when it first runs.
- README.md
    : Documentation for the project, including setup instructions, API details, and other important information for users and developers.

