def main():
    while(True):
        print(">>")
        text = str(input("Enter cmd: ")).upper()
        text = get_new_hex(text)
        print(text)

def add_colon(text):
    text = text.strip()
    if(text[0] != ':'):
        text = ':' + text
    return text

def get_new_hex(text):
    try:
        text = add_colon(text)
        result = get_checksum(text)
        if (result == "Too short" or result == "Too long"):
            return result
        result = result.upper()
        if (result[-2:] == text[-2:]):
            return "Checksum correct"
        else:
            return text[:-2] + result[-2:]
    except Exception:
        return "Bad input"

def get_checksum(text):
    byte_count = int(text[1:3], 16)
    part_length = byte_count*2
    length = str(text).__len__()
    if(length < 9 + part_length):
        return "Too short"
    if(length > 11 + part_length):
        return "Too long"
    address = str(text[3:9 + part_length])
    i = 0
    sum = byte_count
    while(i < len(address)):
        byte_hex = address[i:i+2]
        byte_value = int(byte_hex, 16)
        sum += byte_value
        i+=2
    result = compliment(sum)
    return hex(result)

def compliment(value):
    return (value ^ 0xFFFF) + 1

if  __name__ =='__main__':main()
