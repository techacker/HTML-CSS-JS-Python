#---------------------------------------------------P R O B L E M------------------------------------------------------------
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

N, M = map(int,input().split())

def checkinput(fNum, sNum):
    if fNum % 2 == 0:
        print('First number must be an odd number.')
        exit()
    elif sNum != 3 * fNum:
        print('Second number must be 3 times the first number.')
        exit()
    else:
        pass

def createPattern(N,M):
    for i in range(N):
        pattern = '.|.'
        if i < (N-1)/2:
            print((pattern * (2 * i + 1)).center(M, '-'))
        elif i == (N - 1)/2:
            print('WELCOME'.center(M, '-'))
        else:
            print((pattern * (2 * (N-1-i)+1)).center(M, '-'))


checkinput(N, M)
createPattern(N, M)