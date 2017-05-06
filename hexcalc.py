def main():
    while(True):
        print(">>")
        text = str(input("Enter cmd: ")).upper()
        return get_new_hex(text)

def get_new_hex(text):
    result = get_checksum(text).upper()
    if (result[-2:] == text[-2:]):
        return "Checksum correct"
    else:
        return "Line with new checksum: " + text[:-2] + result[-2:]

def get_checksum(text):
    byte_count = int(text[1:3], 16)

    address = str(text[3:9 + byte_count*2])
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
