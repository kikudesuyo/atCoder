n = int(input())
h_s = list(map(int, input().split()))

t_count = 0
attack_reminder = 0
for i in range(n):
    hp = h_s[i]
    if attack_reminder == 0:
        pass
    elif attack_reminder == 1:
        if hp == 1:
            t_count += 1
            attack_reminder = 2
            continue
        if hp <= 4:
            t_count += 2
            attack_reminder = 0
            continue
        else:
            t_count += 2
            attack_reminder = 0
            hp -= 4
    else:
        if hp <= 3:
            t_count += 1
            attack_reminder = 0
            continue
        else:
            t_count += 1
            attack_reminder = 0
            hp -= 3
    tmp_reiminder = hp % 5
    if tmp_reiminder == 0:
        t_count += (hp // 5) * 3
        attack_reminder = 0
    elif tmp_reiminder == 1:
        t_count += (hp // 5) * 3 + 1
        attack_reminder = 1
    elif tmp_reiminder == 2:
        t_count += (hp // 5) * 3 + 2
        attack_reminder = 2
    else:
        t_count += (hp // 5) * 3 + 3
        attack_reminder = 0


print(t_count)
