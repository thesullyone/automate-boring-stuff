import time, sys
indent = 0 # how many spaces to indent line of buttholes
indentIncrease = True # whether line is moving left or right (right is True)
try:
    while True: # main loop
        print(' ' * indent, end ='')
        print('*****')
        time.sleep(0.01) # 1/10 sec pause
        if indentIncrease:
            # increase number of spaces
            indent = indent + 1
            if indent == 10:
                # change indent direction
                indentIncrease = False
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # change direction
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()