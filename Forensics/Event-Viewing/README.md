![image](https://github.com/user-attachments/assets/5bae6c62-e061-4554-baee-e8728d87e969)# Event-Viewing



## Description
One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. 
The story given by the employee is as follows:
1. They installed software using an installer they downloaded online
2. They ran the installed software but it seemed to do nothing
3. Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.
See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!

This question requires player to find the flag from the Windows Logs (download from the challenge).

## Hints
1. Try to filter the logs with the right event ID
2. What could the software have done when it was ran that causes the shutdowns every time the system starts up?

As the description mentioned, the flag is splitted into three pieces and according to the hints given, we need to find the flag pieces by filter the logs with the right event ID.
The second hint told us about the event ID that related to the case so we can get the flag easily.

