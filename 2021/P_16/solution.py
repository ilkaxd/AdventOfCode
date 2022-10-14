hexToBin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

binToHex = {
    value: key
    for key, value in hexToBin.items()
    }


def load_data():
    with open((r'2021\P_16\input.txt')) as f:
        return f.readline()


def convert_hex_to_binary(data):
    result = ''
    for ch in data:
        result += hexToBin[ch]
    return result


def convert_binary_to_hex(data):
    data = data.rjust(4, '0')
    return binToHex[data]


def get_header(data):
    version = data[:3]
    typeID = data[3:6]
    return version, typeID


def parse_body(data):
    value = ''
    while len(data) > 0:
        substring = data[:5]
        data = data[5:]
        value += substring[1:]
        if substring[0] == '0':
            break
    return data, int(value, 2)


def _packet_decoder(binary):
    version, idx = get_header(binary)
    idx = convert_binary_to_hex(idx)
    versioin = convert_binary_to_hex(version)
    binary = binary[6:]
    if idx == '4':
        binary, value = parse_body(binary)
        print(value)
    else:
        length_type = binary.pop(0)
        if length_type == '0':
            subpacket_len = int(binary[:15], 2)
            binary = binary[15:]
        else:
            subpacket_count = int(binary[:11], 2)
            binary = binary[11:]


def packet_decoder(message):
    binary = convert_hex_to_binary(message)
    _packet_decoder(binary)


if __name__ == '__main__':
    data = load_data()
    data = 'D2FE28'
    print(packet_decoder(data))
