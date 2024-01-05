for _ in range(int(input())):
    x1,y1,x2,y2,x3,y3 = map(int, input().split())
    area_trin = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    x_max, x_min = max(x1,x2,x3), min(x1,x2,x3)
    y_max, y_min = max(y1,y2,y3), min(y1,y2,y3)
    n=3
    if [y1<y_max, y2<y_max, y3<y_max].count(True)<2:
        n=4
    print(int(n*area_trin))