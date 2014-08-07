__author__ = 'ts'
data = ['1,2,3\n','4,5,6\n','7,8,9\n']
test_file = open('test3.txt','w')
test_file.writelines(data)
test_file.flush()
test_file.close()
