n, m = map(int, input().split())
stage_list = list(map(int, input().split()))
result_list = []

for i in range(1, n+1):
    main_list = [a for a in stage_list if a < i ]
    main_list2 = [a for a in stage_list if a >= i]
    result_list.append([i, stage_list.count(i)/len(main_list2)]) if stage_list.count(i) != 0 else result_list.append([i, 0])
print(result_list)

sort_list = sorted(result_list, key=lambda x: -x[1])

result = [r for r, n in sort_list]
print(result)

'''
def solution(N, stages):
    ans = []
    p = len(stages)
    for i in range(1,N+1):
        q = stages.count(i)
        t = q/p if q != 0 else 0
        ans.append((i, t))
        p -= q

    return [ i for i, v in sorted(ans, key=lambda x: -x[1])]
'''