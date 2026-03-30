from flask import Flask, request
import subprocess, re

app = Flask(__name__)

@app.route("/container-health")
def health_check():
    container = request.args.get("container")
    if container == None:
        return "Missing parameters, try again", 400
    elif not re.match(r'^[a-zA-Z0-9_-]+$', container):
        return "Invalid container name", 400

    docker_result = subprocess.check_output(f"docker ps --filter name={container}", shell=True, text=True)

    if ("Up".casefold() in docker_result.casefold()):
        return("The container is running.\n")
    else:
        return("The container is NOT running.\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
