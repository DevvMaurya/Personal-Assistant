import subprocess

def run_command(command):
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, error = process.communicate()
    return 
