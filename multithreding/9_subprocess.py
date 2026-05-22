#This code executes a Windows CMD command from Python and captures its 
# output
#Example:1
import subprocess

# Run a simple shell command
result = subprocess.run([ "cmd", "/c","echo", "Hello from subprocess!"], capture_output=True, text=True)
print("Output:", result.stdout)
print("Exit code:", result.returncode)

result1 = subprocess.run(["cmd", "/c", "date /t"], capture_output=True, text=True)
print("Today:", result1.stdout.strip())


#Example:2
print("---------------------------------------------")
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(result.stdout)

#Note : Explore ifference between subprocess.run and Popen

#Example:3
print("--------------------Files and Folders:----------------------")

result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result.stdout)   