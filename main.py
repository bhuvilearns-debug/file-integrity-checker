import hashlib
import os


def generate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()


def save_hash(filename, hash_value):
    with open("hashes.txt", "a") as file:
        file.write(f"{filename}:{hash_value}\n")


def verify_hash(filename):
    if not os.path.exists("hashes.txt"):
        print("\nNo saved hashes found.")
        return

    current_hash = generate_hash(filename)

    with open("hashes.txt", "r") as file:
        for line in file:
            saved_filename, saved_hash = line.strip().split(":", 1)

            if saved_filename == filename:
                if saved_hash == current_hash:
                    print("\n✅ File integrity verified.")
                else:
                    print("\n❌ Warning! File has been modified.")
                return

    print("\nNo hash found for this file.")


while True:

    print("\n==============================")
    print(" FILE INTEGRITY CHECKER")
    print("==============================")
    print("1. Generate Hash")
    print("2. Verify File")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        filename = input("Enter file name: ")

        try:
            hash_value = generate_hash(filename)

            print("\nSHA-256 Hash:")
            print(hash_value)

            save_hash(filename, hash_value)

            print("\n✅ Hash saved successfully.")

        except FileNotFoundError:
            print("\nFile not found.")

    elif choice == "2":

        filename = input("Enter file name: ")

        try:
            verify_hash(filename)

        except FileNotFoundError:
            print("\nFile not found.")

    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")