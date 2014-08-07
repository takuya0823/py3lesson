__author__ = 'ts'
test_file = open('test3.txt','r')
for line in test_file:
    print(line.strip())
test_file.close()


