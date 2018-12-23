import os
    
def runSample():
    os.listdir()
    os.mkdir('dir')
    
    f = open('dir/data.txt', 'w')
    f.write('dataSample')
    f.close()
    
    f = open('dir/data.txt')
    f.read()
    f.close()
    
    os.remove('dir/data.txt')
    # removing only empty directory
    os.rmdir('dir')
    os.listdir()