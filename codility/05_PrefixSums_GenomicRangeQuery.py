# https://app.codility.com/demo/results/trainingJFME6E-2H3/

def solution(S, P, Q):
    pref = []
    
    for i, v in enumerate(S):
        total = [0,0,0,0] if i == 0 else pref[i-1][:]
        if v == "A": total[0] += 1
        elif v == "C": total[1] += 1
        elif v == "G": total[2] += 1
        elif v == "T": total[3] += 1
        pref.append(total)

    result = []
    for i, v in enumerate(P):
        x = pref[P[i]-1]
        y = pref[Q[i]]

        if P[i]-1 < 0: x = [0,0,0,0]

        if (x[0] != y[0]): result.append(1)
        elif (x[1] != y[1]): result.append(2)
        elif (x[2] != y[2]): result.append(3)
        elif (x[3] != y[3]): result.append(4)
    
    return result