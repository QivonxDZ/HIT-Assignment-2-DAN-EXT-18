# File Encription and decription checker through shift based cipher, 


import os 

def encrypt_text(text: str, shift1: int, shift2: int) -> str: 
    result = ""

    for char in text: 
        if char.islower():
            if char <= 'n': # a-n
                shift = shift1 * shift2
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:  # o-z
                shift = shift1 + shift2
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += new_char  

        elif char.isupper():
            if char <= 'M':  # A-M
                shift = shift1
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:  # N-Z
                shift = shift2 ** 2
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        elif char.isdigit():
            shift = shift1 - shift2
            new_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            result += new_char
            
        else:
            result += char  # spaces, punctuation, etc. unchanged
    
    return result


def encrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    # Fail safe programing: Checking the uinput file actually exists before trying to read it. Using textbook.

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    with open(input_path, 'r') as file:
        content = file.read()

    encrypted = encrypt_text(content, shift1, shift2)   # type: ignore

    with open(output_path, 'w') as file:
        file.write(encrypted)
    print(f"Encrypted content written to {output_path}")



def decrypt_text(text: str, shift1: int, shift2: int) -> str:
    result = ""
    
    for char in text:
        if char.islower():
            if char <= 'n':  # a-n was shifted forward, so reverse = shift backward
                shift = shift1 * shift2
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:  # o-z was shifted backward, so reverse = shift forward
                shift = shift1 + shift2
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        
        elif char.isupper():
            if char <= 'M':  # A-M was shifted backward, so reverse = shift forward
                shift = shift1
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:  # N-Z was shifted forward, so reverse = shift backward
                shift = shift2 ** 2
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result += new_char
        
        elif char.isdigit():
            shift = shift1 - shift2
            new_char = chr((ord(char) - ord('0') - shift) % 10 + ord('0'))
            result += new_char
        
        else:
            result += char
    
    return result


def decrypt_file(shift1: int, shift2: int, input_path: str, output_path: str) -> None:
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r') as file:
        content = file.read()

    decrypted = decrypt_text(content, shift1, shift2)

    with open(output_path, 'w') as file:
        file.write(decrypted)

    print (f"Decrypted content written to {output_path}")


def verify_files(original_path: str, decrypted_path: str) -> bool:
    if not os.path.exists(original_path):
        print(f"Error: {original_path} not found.")
        return False
    if not os.path.exists(decrypted_path):
        print(f"Error: {decrypted_path} not found.")
        return False

    with open(original_path, 'r') as file:
        original_content = file.read()

    with open(decrypted_path, 'r') as file:
        decrypted_content = file.read()

    if original_content == decrypted_content:
        print("Verification successful: decrypted file matches the original.")
        return True
    else:
        print("Verification failed: decrypted file does NOT match the original.")
        return False


# MAIN CODE 

def main():
    # Prompt the user for shift1 and shift2 values.
    shift1 = int(input("Enter shift1 (non-negative integer): "))
    shift2 = int(input("Enter shift2 (non-negative integer): "))

    raw_path = "raw_text.txt"
    encrypted_path = "encrypted_text.txt"
    decrypted_path = "decrypted_text.txt"

    # 1. Encrypt raw_text.txt -> encrypted_text.txt
    encrypt_file(shift1, shift2, raw_path, encrypted_path)

    # 2. Decrypt encrypted_text.txt -> decrypted_text.txt
    decrypt_file(shift1, shift2, encrypted_path, decrypted_path)

    # 3. Verify decrypted_text.txt matches raw_text.txt
    verify_files(raw_path, decrypted_path)


if __name__ == "__main__":
    main()

