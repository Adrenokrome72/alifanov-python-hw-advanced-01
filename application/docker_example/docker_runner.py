import docker

def run_container(image, command):
    client = docker.from_env()
    container = client.containers.run(image, command, detach=True)
    logs = container.logs().decode('utf-8')
    container.remove()
    return logs
