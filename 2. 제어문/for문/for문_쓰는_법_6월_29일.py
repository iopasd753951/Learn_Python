mark = [90, 25, 67, 45, 80]
i = 0

for i in mark:    # C언어하고 다르게 mark리스트의 값들이 i에 복사되는 듯
    if i >= 60:
        print("합격")
    else:
        print("불합격")
    i += 1
