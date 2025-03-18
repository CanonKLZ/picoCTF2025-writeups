Updated: Solution found thanks to writeups provided by 0xSherfa (https://medium.com/@ahmedgamer250/picoctf-2025-writeups-by-0xsherfa-96b348942348).

![image](https://github.com/user-attachments/assets/730378af-a81e-4a02-bb5b-2972276650b3)

Hints:
1. I heard that SHA-256 is the best hash function out there!
2. Remember Squeexy, we enjoy our cheese with exactly 2 nibbles of hexadecimal-character salt!
3. Ever heard of rainbow tables?

### Challenge Analysis
Download the cheese_list.txt from the challenge and connect to the program using the nc command given.

![image](https://github.com/user-attachments/assets/396b8bb4-290c-4b83-981e-b3ffec4b8330)

The mouse provided me a secret cheese, a SHA256 hash (matched hint 1). Then according to hint 2, the hash was produced using the cheese name from cheese_list.txt, hashed with sha256 hash algorithm with a 2 nibbles of hex-character salt (meaning: a byte == two hexadecimal characters). 

-> SHA256(Cheese name + 2 hexadecimal characters)

Unlike Part 1, the option available is guess my cheese (g). 

### Original brute force to get the secret cheese is not recommended.
As according to hint 3, rainbow table is the best method that we can crack the sha256 hash provide by the mouse. This means we need to prepare a rainbow table (usually a txt file) that contains all the computed sha256 hash.

### But how?
Pretty simple, the produced hash is computed using sha256 algorithm with 2 hex characters as salt. Hence, we need to compute the rainbow table using the same way, implement the hash the cheese name with SHA256 algorithm with salts. 

### Things that the challenge does not clarify
1. SHA256 hash can be produced immediately regardless of how the input looks like (Can be uppercase, lowercase, mixed cases, has special symbols and so on)
2. How the salt is added before hashing? Does it put at the front (Prefix), put at the end (Postfix) or both?
3. The salt added is in lowercase, uppercase, or both? (Eg: ab, AB, aB or Ab)

### Before obtaining updated findings (Reason I cannot get the solid solution)
I appended cheese with the decoded salt raw bytes using latin1 encoding. (You can view from rainbow_table_original.py)

### Updated findings
1. Before the hash is produced, the cheese name MUST be in lowercase, remain the whitespace and special symbols, and convert to bytes using UTF-8 encoding.
2. Salt needed to be converted to raw bytes before append to the end of cheese bytes.

Then using the findings, you can create script(s) to compute a rainbow table.

Then guess the cheese by searching the hash provided by the mouse using the rainbow table. Enter the cheese name and the salt to get the flag.

### Steps if want to use my solution
1. Download cheese_list.txt, rainbow_table.py and salts.py files, put them together in a single folder.
2. Run salts.py
3. Run rainbow_table.py
