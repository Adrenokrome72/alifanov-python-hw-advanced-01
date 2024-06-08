from application.salary import calculate_salary
from application.db.people import get_employees
from application.docker_example.docker_runner import run_container
from datetime import datetime


if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()
    image = 'ubuntu:latest'
    command = 'echo "Hello, Docker!"'
    output = run_container(image, command)
    print(output)