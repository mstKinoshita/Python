i = input()
s = 1
w = 1

if i<3:
    print 'Please input a number larger than 3!'
    i = input()

if i>=3:
    print s
    print w
    for i in range(1,i-1):
        e = s+w
        print e
        s = w
        w = e
    
