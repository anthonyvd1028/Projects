# Landing Zone

> Anthony DiTaranto | 10/18/2024

## Description

We have compromised a remote system belonging to deephax, and it’s your job to log in and investigate what you can find. Your mission is to locate a file named flag1.txt, which contains the first piece of crucial information.

Use your skills to gain access to the system and find flag1.txt. Remember, this is just the beginning—DEADFACE might have hidden other secrets deeper within the system.

## Additional Info 

Connection Info:
Host: deephax@deephax.deadface.io
Username: deephax
Password: D34df4c32024$

## Solution

So we are given the host and password for a remote server, which we need to log into and locate a file named `flag1.txt`. Now I had a feeling we would enter the server through SSH, but I ran NMAP on the server to make sure we could. I used NMAP by running the command `nmap -Pn deephax.deadface.io`. From the command, I see that port 22 is open, which is the default port for SSH.

I then entered the machine using SSH by entering the command `ssh deephax@deephax.deadface.io` and was prompted for the password, which we know is `D34df4c32024$`. Once inside the machine, I entered `ls -a` to see all the files in the current directory and saw `flag1.txt`. Finally, I used Cat to see the contents of the file and got the flag.

## Flag

`flag{hostbusters1_e361b9b8352eea50}`
