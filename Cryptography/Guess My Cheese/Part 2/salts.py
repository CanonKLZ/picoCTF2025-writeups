def generate_all_salts():
    salts = []
    hex_digits = '0123456789ABCDEF'
    for first_digit in hex_digits:
        for second_digit in hex_digits:
            salts.append(first_digit + second_digit)
    return salts

def save_salts_to_file(file_path):
    salts = generate_all_salts()
    with open(file_path, 'w') as file:
        file.write('\n'.join(salts))
    print(f"Generated {len(salts)} salts and saved to {file_path}")

# Usage
file_path = 'hex_salts.txt'
save_salts_to_file(file_path)
