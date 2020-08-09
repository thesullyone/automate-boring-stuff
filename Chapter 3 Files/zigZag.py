import time, sys
indent = 0 # how many spaces to indent line of buttholes
indentIncreasing = True # whether line is moving left or right (right is True)
try:
    while True: # main loop
        print(' ' * indent, end ='')
        print('********')
        time.sleep(0.1) # 1/10 sec pause
        if indentIncreasing:
            # increase number of spaces
            indent = indent + 1
            if indent == 20:
                # change indent direction
                indentIncreasing = False
        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()