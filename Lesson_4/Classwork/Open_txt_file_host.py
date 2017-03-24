filename = 'hosts.txt'
f = open('/etc/hosts')
count = 0
for line in f:
    count += 1
print u'There are {} lines in {} file'.format(count,filename)


f = open('/etc/hosts')
print u'There are {} lines in {} file'.format(len(f.readlines()),filename)


f = open('/etc/hosts')
num_lines = sum(1 for line in open('/etc/hosts'))
print u'There are {} lines in {} file'.format(num_lines,filename)


non_blank_count = 0
with open('/etc/hosts') as file:
    for line in file:
       if line.strip():
          non_blank_count += 1

print u'There are {} unique lines in {} file'.format(non_blank_count, filename)





