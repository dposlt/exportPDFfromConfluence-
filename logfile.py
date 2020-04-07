def loggin(s):
    with open('log.out', 'a') as log:
        log.writelines(s + '\n')


