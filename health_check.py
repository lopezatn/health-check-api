from flask import Flask, request
import subprocess, re

app = Flask(__name__)

CONTAINER_NAME_RE = re.compile(r'^[a-zA-Z0-9_-]+$')

@app.route("/container-health")
def health_check():
    container = request.args.get("container")

    if not container:
        return "Missing parameters, try again\n", 400

    if not CONTAINER_NAME_RE.match(container):
        return "Invalid container name, try again\n", 400
    
    try:
        result = subprocess.run(
            ["docker", "ps", "-all", "--filter", f"name=^/{container}$", "--format", "{{.State}}"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )

        status = result.stdout.strip()

        if status == "running":
            return f"The container '{container}' is running.\n", 200
        elif status == "":
            return f"The container '{container}' does not exist.\n", 404
        else:
            return f"The container '{container}' is NOT running. (Status: {status})\n", 200
    
    except subprocess.CalledProcessError as e:
        return f"Error checking container status: {e}\n", 500
    except subprocess.TimeoutExpired:
        return "Error: Command timed out while checking container status. Try again later.\n", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
