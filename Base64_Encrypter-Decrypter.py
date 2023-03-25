# Module Importing
import time as t
from os import system, name


def encode_base64(message):
    """
    Encodes the text into base64 encryption
    :param message: It receives the text which will encrypt on base64
    :return: It returns text after being encrypted
    """
    # It opens the text file in which each line consists of a base64 code followed by a space and
    # then the corresponding character.
    # It iterates through each line in the file, splits the line into the base64 code and character.
    # Adds an entry to the base64_map dictionary where the key is the base64 code and the value is the
    # corresponding character.
    with open('base64code.txt') as f:
        base64_map = {}
        for line in f:
            code, char = line.strip().split()
            base64_map[code] = char

    # Converts the text to binary
    binary = ""
    for char in message:
        binary += bin(ord(char))[2:].zfill(8)

    # Splits the binary into groups of 6 bits
    groups = [binary[i:i + 6] for i in range(0, len(binary), 6)]

    # Creates a padding on the last group with zeros if necessary
    if len(groups[-1]) < 6:
        groups[-1] += "0" * (6 - len(groups[-1]))

    # Maps each group to its corresponding Base64 character
    base64_chars = ""
    for group in groups:
        if group in base64_map:
            base64_chars += base64_map[group]
        else:
            base64_chars += "="

    # Pads with "=" characters if necessary
    while len(base64_chars) % 4 != 0:
        base64_chars += "="
    return base64_chars


def decode_base64(base64_chars):
    """
    It decodes the Base64 encrypted text
    :param base64_chars: It receives the encrypted text that will receive the text to be decrypted
    :return: It returns the decrypted text
    """
    # It opens the text file in which each line consists of a base64 code followed by a space and
    # then the corresponding character.
    # It iterates through each line in the file, splits the line into the base64 code and character.
    # Adds an entry to the base64_map dictionary where the key is the base64 code and the value is the
    # corresponding character.
    # Creates a dictionary that maps Base64 characters into 6-bit groups
    base64_map = {}
    with open('base64code.txt', 'r') as f:
        for line in f:
            code, char = line.strip().split(' ')
            base64_map[char] = code

    # Removes the ('=') padding characters  if needed
    while base64_chars[-1] == '=':
        base64_chars = base64_chars[:-1]

    # Groups up Base64 characters into 4-character sets
    groups = [base64_chars[i:i + 4] for i in range(0, len(base64_chars), 4)]

    # Converts each Base64 group of 4 characters into 3 bytes (ASCII)
    ascii_bytes = b''
    for group in groups:
        if len(group) < 4:
            group += '=' * (4 - len(group))
        binary = ''
        for char in group:
            binary += bin(int(base64_map[char], 2))[2:].zfill(6)
        ascii_bytes += int(binary, 2).to_bytes(3, byteorder='big')

    # Decodes the ASCII bytes into a string
    decoded = ascii_bytes.decode('ascii').replace('\x00', '')
    return decoded


# This function clears the console screen on the terminal
def clear():
    # for Windows computers
    if name == 'nt':
        _ = system('cls')
    # for MAC and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')


# This function displays the initial screen of the program
def init_screen():
    clear()
    print("\033[7;37;1m###########################################################################################################\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#                                                  Base64                                                 #\033[0m")
    print("\033[7;37;1m#                                          Encrypter and Decrypter                                        #\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#---------------------------------------------------------------------------------------------------------#\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#                                             Made by xAlamaos                                            #\033[0m")
    print("\033[7;37;1m#                                              Version 1.0.0                                              #\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m###########################################################################################################\033[0m")
    t.sleep(4)


# This function displays the main menu of the program
def menu():
    clear()
    print("\033[7;37;1m###########################################################################################################\033[0m")
    print("\033[7;37;1m#                                      Base64 - Encrypter & Decrypter                                     #\033[0m")
    print("\033[7;37;1m#                                                Main Menu                                                #\033[0m")
    print("\033[7;37;1m#---------------------------------------------------------------------------------------------------------#\033[0m")
    print("\033[7;49;1m#      1. Encode your text                                                                                #\033[0m")
    print("\033[7;49;1m#      2. Decode your text                                                                                #\033[0m")
    print("\033[7;49;1m#      3. Info about program                                                                              #\033[0m")
    print("\033[7;49;1m#                                                                                                         #\033[0m")
    print("\033[7;49;1m#      0. Exit program                                                                                    #\033[0m")
    print("\033[7;49;1m###########################################################################################################\033[0m")


def info():
    print("\033[7;37;1m###########################################################################################################\033[0m")
    print("\033[7;37;1m#             This program is a personal project related to a project about Base64 Encryption             #\033[0m")
    print("\033[7;37;1m#                                   Computer Science - Azores University                                  #\033[0m")
    print("\033[7;37;1m#                                     Subject: Programming Laboratory                                     #\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#                                          Developed by xAlamaos                                          #\033[0m")
    print("\033[7;37;1m#                                              21 March 2023                                              #\033[0m")
    print("\033[7;37;1m###########################################################################################################\033[0m")


def goodbye():
    print("\033[7;37;1m###########################################################################################################\033[0m")
    print("\033[7;37;1m#                                      THANK YOU FOR USING MY PROGRAM                                     #\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#              Special thanks to:                                                                         #\033[0m")
    print("\033[7;37;1m#                     Jerónimo Nunes (teacher) - for introducing this project to me                       #\033[0m")
    print("\033[7;37;1m#                     João Bulhões (classmate) - for helping me with A-Z, a-z e 0-9 limitation            #\033[0m")
    print("\033[7;37;1m#                                                                                                         #\033[0m")
    print("\033[7;37;1m#                                          Developed by xAlamaos                                          #\033[0m")
    print("\033[7;37;1m#                                              21 March 2023                                              #\033[0m")
    print("\033[7;37;1m###########################################################################################################\033[0m")


def main():
    while True:
        menu()
        choice = input("\n\033[7;49;1mPlease select an option:\033[0m ")

        if choice == "1":
            while True:
                clear()
                usr_input = input("\033[7;37;1m Enter the message to be encoded:\033[0m ")
                if all(48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 for char in usr_input):
                    encoded_txt = encode_base64(usr_input)
                    print(f"\033[7;49;1m The encrypted message is:\033[0m \033[1;31;1m{encoded_txt}\033[0m")
                    input("\n\nPress Enter to continue")
                    break
                else:
                    print("Error: Use ONLY the following characters A-Z, a-z e 0-9.")
                    input("\nPress Enter to continue")

        elif choice == "2":
            clear()
            usr_input = input("\033[7;37;1m Enter the message to be decoded:\033[0m ")
            while True:
                try:
                    decoded_txt = decode_base64(usr_input)
                    print(f"\033[7;49;1m The decrypted message is:\033[0m \033[1;31;1m{decoded_txt}\033[0m")
                    input("\n\nPress Enter to continue")
                    break  # if successful, break out of the loop
                except (FileNotFoundError, ValueError) as e:
                    print("\033[7;49;1m #                                ERROR                                #\033[0m")
                    print("\033[7;49;1m #                 That is not an encrypted Base64 code                #\033[0m")
                    print("\n\033[7;49;1m Error Description\033[0m")
                    print(e)
                    input("\nPress Enter to continue")
                    break

        elif choice == "3":
            clear()
            info()
            input("\nPress Enter to continue")

        elif choice == "0":
            clear()
            goodbye()
            t.sleep(5)
            break

        else:
            print("Invalid input. Please try again.\n")
            t.sleep(2)


if __name__ == '__main__':
    init_screen()
    main()
