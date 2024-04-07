def solution(park, routes):
    op = {"N":[-1, 0], "S":[1, 0], "W":[0, -1], "E":[0, 1]}
    W = len(park[0])
    H = len(park)
    test = [0, 0]
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                start = [i, j]
    
    for route in routes:
        dir, distance = route.split()
        distance = int(distance)
        
        test = list(start)
        print("시작 test : ", test)
        for i in range(distance):
            test[0] = test[0] + op[dir][0]
            test[1] = test[1] + op[dir][1]
            print(i,"번째 test : ", test)
            print(start)
            
            if test[0]>=H or test[0]<0 or test[1]<0 or test[1]>=W:
                break
            elif park[test[0]][test[1]] == "X":
                print("X만남")
                break
            elif i==distance-1:
                start = test
                print("움직임", start)

                
    return start
            
