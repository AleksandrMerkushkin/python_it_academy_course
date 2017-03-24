import sys
import struct

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file = open('cat.bmp', 'rb')
data = input_file.read()
file_header = struct.unpack("<ccihhi", data[:14])
print("file_header is {}".format(file_header))

print("INFO: file size from header is {}".format(file_header[2]))
print("INFO: file size in memory is {}".format(len(data)))
headers_size = file_header[4]
print("INFO: headers size is {}".format(headers_size))

pixel_size = len(data) - headers_size
changed_data = data[:headers_size] + pixel_size*'\xff'
open('dsa.bmp', 'wb').write(changed_data)