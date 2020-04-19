while 1:

    answ = raw_input('Are you feeling depressed? (y/n)')
    if answ == 'y':
        print('Goodbye, world!')
        break
    elif answ == 'n':
        print('Hello, world')
        break
    else:
        print('Not a valid anwser')
