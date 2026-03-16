import sys, subprocess

try:
    container = sys.argv[1]
except IndexError:
    print("Missing arguments")
    exit(1)

docker_result = subprocess.check_output(f"docker ps --filter name={container}", shell=True, text=True)

if ("Up".casefold() in docker_result.casefold()):
    print("The container is running")
else:
    print("The container is NOT running")


