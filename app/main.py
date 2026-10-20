import sys
import shutil
import shlex
import subprocess

def main():
    builtin=["echo","exit","type"]
    while True:
        sys.stdout.write("$ ")
        command=input()
        if command == "exit":
            break

        elif command.startswith("echo "):
            cmd=command[5:]
            print(cmd)
        elif command.startswith("type "):
            cmd=command[5:]
            if cmd in builtin:
                print(f"{cmd} is a shell builtin")
            elif path := shutil.which(cmd):
                print(f"{cmd} is {path}")
            else:
                print(f"{command[5:]}: not found")
        else:
            args = shlex.split(command)
            if args and (path := shutil.which(args[0])):
                subprocess.run(args, executable=path, check=False)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
 