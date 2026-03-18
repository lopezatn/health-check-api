from flask import Flask, request
import sys, subprocess

app = Flask(__name__)

@app.route("/container-health")
def health_check():

    try:
        container = request.args.get("container")
    except IndexError:
        return("Missing arguments")

    docker_result = subprocess.check_output(f"docker ps --filter name={container}", shell=True, text=True)

    if ("Up".casefold() in docker_result.casefold()):
        return("The container is running")
    else:
        return("The container is NOT running")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
