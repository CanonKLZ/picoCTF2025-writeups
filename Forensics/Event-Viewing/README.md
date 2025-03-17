# Event-Viewing

![image](https://github.com/user-attachments/assets/5bae6c62-e061-4554-baee-e8728d87e969)

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

To solve this, open the logs using a Windows 10 Virtual Machine. (If you want to open locally also can)

From hint 2, I know that the software caused shutdown during the system boots up, so I need to filter the logs by the event ID that related to reboot/boots up.

![image](https://github.com/user-attachments/assets/400a873d-462d-4d60-a627-cbd48a41b9e9)

### Hence, the first event ID: 1074

![image](https://github.com/user-attachments/assets/85800943-0303-49b8-b6b9-e8e593f61617)

After filtering, we can notice that the comment section's value is weird, that is the flag pieces.

### How about the other two?
Since I'm not a Windows Logs professional, so I obtained help from my friend, ChatGPT.
ChatGPT suggested these IDs:
1. 11707
2. 1033
3. 4688
4. 4104
5. 9009
6. 6005
7. 6008
8. 1074
9. 106
10. 4698
11. 4657

From the list, I obtained flag pieces from 1033 and 4657.

#### 1033
![image](https://github.com/user-attachments/assets/bfb87204-7271-45e6-a583-59a6509e6fce)

#### 4657
![image](https://github.com/user-attachments/assets/c11c7466-71d7-487b-898e-0caa73416d27)

Then decode them to get the completed flag.
