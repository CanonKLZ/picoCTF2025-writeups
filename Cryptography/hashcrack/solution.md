![image](https://github.com/user-attachments/assets/f1ddd781-9ff5-4a37-8d9a-6161b48348fe)

Hints:
1. Understanding hashes is very crucial. (https://primer.picoctf.org/#_hashing)
2. Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.
3. Tried using any hash cracking tools?

Not hard, you just need to determine the type of hash algorithm used for this challenge.

First Attempt
I found that MD5 is used to produce the hash and the password is "password123".

Second Attempt
SHA1: letmein

Third Attempt
SHA256: qwerty098

Enter the password and get the flag.
