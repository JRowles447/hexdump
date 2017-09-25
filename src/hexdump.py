import sys

def hexify(byte_seq):
    """
    Transform a byte sequence into a list strings representing each byte, in hex.
    :param byte_seq: a sequence of byte values
    :return: a list of bytes as hex strings, without the leading '0x'

    >>> hexify(b'abc') # note the leading b; this is a "bytes literal"
    ['61', '62', '63']

    >>> hexify(bytes.fromhex('2Ef0 F1f2  '))  # bytes.fromhex is another way to write bytes literals
    ['2e', 'f0', 'f1', 'f2']
    """

    result = []
    for b in byte_seq:  # we can iterate over the bytes, since they're a sequence
        h = hex(b) # hex() is a built-in that transforms a numerical value to its hex equivalent as a string
        result.append((h[2:]).zfill(2))  # slice off the first two characters (0x); take character 2 through the end;
    return result

def dump_file_hex(filename):
    '''
    Transform a file into byte representation with format of Unix hex dump command line tool.
    :param filename: file to be hex dumped
    :return: printed byte representation of file
    '''
    with open(filename, 'rb') as f:  # when opened in binary mode, you can read() the entire file, or
                                     # read(16) some number of bytes at a time as an immutable sequence of bytes
        chunk = f.read(16)
        line_number = 0
        while chunk:  # empty sequences (that is, of length 0) evaluate to false
            line_num = hex(line_number)[2:]
            print(str(line_num).zfill(8), end = '')

            hex_list = hexify(chunk)
            ret_hex = hex_list
            if(len(hex_list) > 0):
                ret_hex[0] = "  " + ret_hex[0]
            if(len(hex_list) > 8):
                ret_hex[8] = " " + ret_hex[8]

            line = ' '.join(ret_hex)  # join() joins the list of strings, using the string it's called on
                                       # as the separator character
            byte_list = hex_list
            asc = ""
            for x in byte_list:
                val = int(x, base = 16)
                if (val >= 32 and val <= 126):
                    asc += chr(int(x, base = 16))
                else:
                    asc += "."

            line = '{0: <50}'.format(line)
            line = line + "  |" + asc + "|"

            print(line)
            chunk = f.read(16)
            line_number += len(hex_list)

        if line_number != 0:
            line_num = hex(line_number)[2:]
            print(str(line_num).zfill(8))

def main():
    dump_file_hex(sys.argv[1])

if __name__ == '__main__':
    main()
