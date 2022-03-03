import os
import subprocess

os.system("ls")
subprocess.run(["ls","-l","README.md"])
# Ex 5
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
# Ex 6
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


