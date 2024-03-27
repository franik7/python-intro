##open a file open(path_to_file)


hosts = open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt')
hosts_contents = hosts.read()
print(hosts_contents)

hosts2 = open('C:/Windows/System32/drivers/etc/hosts')
hosts_contents2 = hosts2.read()
print(hosts_contents2)

"""
read() - returns entire file
seek(offset) - change current position to offset
seek(0) - go to beginning
seek(5) - got o 5th bye
tell() - determine the current psoition of the file
"""

hosts3 = open('C:/Windows/System32/drivers/etc/hosts')
hosts_contents3 = hosts3.tell()
print(hosts.read())

print(hosts3.read(3))
print(hosts.tell())

##close the file
hosts.close()

print('Started reading the file')
with open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt') as file:
    print('File closed? {}'.format(file.closed))
    print(file.read())
print('Finished with the file')
print('File closed? {}'.format(file.closed))


with open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt') as file:
    for line in file:
        print(line.rstrip())

##opent to write a file
##open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt', 'w')

with open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt', 'a') as file:
    print(file.mode)
    file.write('More text \n')
    file.write('Even more text \n')

with open('C:/Users/frant/AppData/Local/Programs/Python/Python312/basics/data.txt') as file:
    print(file.read())

##we can import modules to python
import time
print(time.ctime())

import time
dir(time)
