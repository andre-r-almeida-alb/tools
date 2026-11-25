import argparse
import base64
import binascii

def encode_base64(input_string):
    return base64.b64encode(input_string.encode('utf-8')).decode('utf-8')

def decode_base64(encoded_string):
    return base64.b64decode(encoded_string.encode('utf-8'), validate=True).decode('utf-8')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode or decode a UTF-8 string using Base64.")
    parser.add_argument("operation", choices=("e", "d"), help="Operation: 'e' for encode, 'd' for decode")
    parser.add_argument("input_string")
    args = parser.parse_args()

    try:
        result = encode_base64(args.input_string) if args.operation == "e" else decode_base64(args.input_string)
    except (binascii.Error, UnicodeError, ValueError) as error:
        parser.error(str(error))
    print("\n" + result)