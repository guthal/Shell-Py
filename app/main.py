import sys
import shutil

def main():
    builtin=["echo","exit","type"]
    while True:
        sys.stdout.write("$ ")
        pass
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
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
 