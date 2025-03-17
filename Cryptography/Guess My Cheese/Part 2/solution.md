![image](https://github.com/user-attachments/assets/730378af-a81e-4a02-bb5b-2972276650b3)

Hints:
1. I heard that SHA-256 is the best hash function out there!
2. Remember Squeexy, we enjoy our cheese with exactly 2 nibbles of hexadecimal-character salt!
3. Ever heard of rainbow tables?

### The first challenge I give dislikes.

The challenge isn't very hard, but took me 2 days to solve because of missing out something that the challenge doesn't clarify clearly (will be explained later). Otherwise can be solved within an hour.

Download the cheese_list.txt from the challenge and connect to the program using the nc command given.

![image](https://github.com/user-attachments/assets/396b8bb4-290c-4b83-981e-b3ffec4b8330)

The mouse provided me a secret cheese, a SHA256 hash (matched hint 1). Then according to hint 2, the hash was produced using the cheese name from chees_list.txt, hashed with sha256 hash algorithm with a 2 nibbles of hex-character salt (meaning: a byte == two hexadecimal characters). 

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

### So, can only assuming
Since this is a writeups, I just provided my findings:
1. Before the hash is produced, the cheese name MUST be in lowercase and WITHOUT any whitespace, remain the special symbols.
2. Salt is added at the end (Postfix)
3. Salt added is in UPPERCASE as predefined in Hexadecimal characters list.

Then using the findings, you can create script(s) to compute a rainbow table.

Then guess the cheese by searching the hash provided by the mouse using the rainbow table. Enter the cheese name and the salt to get the flag.

## My feedback
I understood that creating a CTF challenge is not an easy job and is hoping players can enjoy. But, if possible, make sure to do careful examination. Still, this is a good challenge. Bravo!
