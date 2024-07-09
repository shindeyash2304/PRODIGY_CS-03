from PIL import Image
import numpy as np


def encrypt_decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    flat_array = img_array.flatten()
    key_array = np.tile(key, len(flat_array) // len(key) + 1)[:len(flat_array)]
    encrypted_array = flat_array ^ key_array
    encrypted_img_array = encrypted_array.reshape(img_array.shape)
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'))
    encrypted_img.save(output_path)


def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

        if choice == 'q':
            break

        if choice not in ['e', 'd']:
            print("Invalid choice. Please try again.")
            continue

        input_path = input("Enter the path to the input image: ")
        output_path = input("Enter the path for the output image: ")
        key = input("Enter the encryption/decryption key (a string of numbers): ")

        key = [int(k) for k in key.split()]

        encrypt_decrypt_image(input_path, output_path, key)

        print(f"Image {'encrypted' if choice == 'e' else 'decrypted'} successfully!")


if __name__ == "__main__":
    main()
