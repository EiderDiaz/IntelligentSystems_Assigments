def printStateMatrix(state):
    temp = dict(test)
    
    for i in range(1, 8):
        for j in range(1, 8):
            if i == 1:
                if j == 1:
                    print('+ ', end = '')
                elif j == 7:
                    print('+')
                else:
                    print(str(j - 1) + ' ', end = '')
            
            elif i == 7:
                if j == 1:
                    print('+ ', end = '')
                elif j == 7:
                    print('+')
                else:
                    print(str(j - 1) + ' ', end = '')
            
            else:
                if j == 1:
                    print(str(i - 1) + ' ', end = '')
                elif j == 7:
                    print(str(i - 1))
                else:
                    if temp['A'] == (i - 1, j - 1):
                        print('A ', end = '')
                    elif temp['T'] == (i - 1, j - 1):
                        print('T ', end = '')
                    elif [locus for locus in list(temp['M']) if locus == (i - 1, j - 1)]:
                        print ('M ', end = '')
                    elif [locus for locus in list(temp['O']) if locus == (i - 1, j - 1)]:
                        print ('O ', end = '')
                    else:
                        print('- ', end = '')
                        
test_state = (('A', (5,1)), ('T', (2, 3)), ('M', ((3, 2), (3, 3), (3, 4))), ('O', ((3, 1), (3, 5))))
printStateMatrix(test_state)
