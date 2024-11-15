import binascii

def ascii_to_hex(message):
    message_bytes = message.encode('ascii')
    encoded = binascii.hexlify(message_bytes).decode('ascii')
    return encoded

def hex_to_ascii(message):
    decoded = binascii.unhexlify(message).decode()
    return decoded