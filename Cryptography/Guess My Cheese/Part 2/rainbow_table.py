import hashlib
import hmac

def hash_cheese_with_salt(cheese, salt):
    salted_cheese = cheese.lower().encode() + bytes.fromhex(salt)
    return hashlib.sha256(salted_cheese).hexdigest()

def load_cheese_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def load_salts(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_hashes(cheese_file, salt_file, output_file):
    cheeses = load_cheese_names(cheese_file)
    salts = load_salts(salt_file)
    
    with open(output_file, 'w') as file:
        for cheese in cheeses:
            for salt in salts:
                cheese_hash = hash_cheese_with_salt(cheese, salt)
                file.write(f"{salt},{cheese},{cheese_hash}\n")
    print(f"Hashes saved to {output_file}")

# Usage example
cheese_file = 'cheese_list.txt'  # Update with your cheese names file path
salt_file = 'hex_salts.txt'        # Update with your salts file path
output_file = 'cheese_hashes.txt'  # Output file for the hashes
generate_hashes(cheese_file, salt_file, output_file)
