def encode_base64(message):
    with open('base64code.txt') as f:
        base64_map = {}
        for line in f:
            code, char = line.strip().split()
            base64_map[code] = char
    # Convert message to binary
    binary = ""
    for char in message:
        binary += bin(ord(char))[2:].zfill(8)
    # Split binary into groups of 6 bits
    groups = [binary[i:i + 6] for i in range(0, len(binary), 6)]
    # Pad last group with zeros if necessary
    if len(groups[-1]) < 6:
        groups[-1] += "0" * (6 - len(groups[-1]))
    # Map each group to its corresponding Base64 character
    base64_chars = ""
    for group in groups:
        if group in base64_map:
            base64_chars += base64_map[group]
        else:
            base64_chars += "="
    # Pad with "=" characters if necessary
    while len(base64_chars) % 4 != 0:
        base64_chars += "="
    return base64_chars


def decode_base64(base64_chars):
    # Criar um dicionário que mapeia os caracteres Base64 para grupos de 6 bits
    base64_map = {}
    with open('base64code.txt', 'r') as f:
        for linha in f:
            (valor, caractere) = linha.strip().split(' ')
            base64_map[caractere] = valor

    # Remover os caracteres de preenchimento, conforme necessário
    while base64_chars[-1] == '=':
        base64_chars = base64_chars[:-1]

    # Agrupar os caracteres Base64 em conjuntos de 4 caracteres
    grupos = [base64_chars[i:i+4] for i in range(0, len(base64_chars), 4)]

    # Converter cada grupo de 4 caracteres Base64 em 3 ‘bytes’ (ASCII)
    ascii_bytes = b''
    for group in grupos:
        if len(group) < 4:
            group += '=' * (4 - len(group))
        binario = ''
        for char in group:
            binario += bin(int(base64_map[char], 2))[2:].zfill(6)
        ascii_bytes += int(binario, 2).to_bytes(3, byteorder='big')

    # Descodificar os ‘bytes’ (ASCII) em uma ‘string’
    decoded = ascii_bytes.decode('ascii').replace('\x00', '')
    return decoded


def main():
    usr_input = input("Insira uma frase a ser codificada: ")
    encoded_txt = encode_base64(usr_input)
    print(f"Encrypted message: {encoded_txt}")
    decoded_txt = decode_base64(encoded_txt)
    print(f"Decrypted message: {decoded_txt}")


if __name__ == '__main__':
    main()
