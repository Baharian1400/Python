def tower(numRings):
    result = []
    stk = []
    def tower1(numRings):
        In, To = 0, 1
        stk.append((In,numRings,0,1,2))
        while stk:
            state,numRings,fromPeg,toPeg,usePeg = stk.pop()
            if state == In:
                if numRings != 0: 
                    stk.append((To,numRings,fromPeg,toPeg,usePeg)) 
                    stk.append((In,numRings-1,fromPeg,usePeg,toPeg)) 
            elif state == To:
                result.append((fromPeg,toPeg)) 
                stk.append((In,numRings-1,usePeg,toPeg,fromPeg))
            else:
                print ('Error: logic')
                return result
    tower1(numRings)
    return result

a = [1,2,3,4]
for n in a:
    print ('rings',n)
    print (tower(n))