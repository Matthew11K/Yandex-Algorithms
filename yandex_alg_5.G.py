def steps(x,y,p): #определяем, победят ли наши солдаты, если уничтожить казарму сейчас, и считаем требуемое кол-во ходов
    cnt=0
    while x>0 and p > 0:
        cnt+=1
        p -= x - y
        x -= p
        y=0
        if x<=0:
            return False,cnt
        if p<=0:
            return True,cnt
def calculate_minimum_rounds(x, y, p):
    # Функция для вычисления минимального количества раундов, необходимых для победы.

    # Словарь для хранения результатов по каждому возможному "здоровью" казармы, с которым можно победить.
    possible_wins = {}

    # Основной цикл: проходимся по каждому возможному уровню здоровья казармы от y до 0.
    for health in range(y, -1, -1):
        rounds_to_destroy = 0
        enemy_soldiers = p
        my_soldiers = x
        barrack_health = health
        if my_soldiers>0 and barrack_health>0:
            if my_soldiers-barrack_health>=enemy_soldiers:
                possible_wins[health] = 1
                continue
        if my_soldiers>barrack_health:
            isPossible,rounds_to_destroy=steps(my_soldiers,barrack_health,enemy_soldiers)
            if isPossible:
                possible_wins[health]=rounds_to_destroy
                continue
    return possible_wins

x,y,p=int(input()),int(input()),int(input())
m,_=steps(x,y-x,p)
if ((x==p and not(m)) or (x<p and not(m))) and x<y:
    print(-1)
    exit()
cnt_rounds = 0
opponents = 0
everY=calculate_minimum_rounds(x,y,p)
rounds=[]
isAlive=1
def ySum(y,everY,cnt):
    if y in everY:
        return cnt + everY[y]
    else:
        return -1

while x > 0 and y>0:
    if cnt_rounds == 0: #первый ход всегда бьем казарму
        if x >= y:
            print(1)
            exit()
        else:
            y -= x
        cnt_rounds += 1
        curRounds=ySum(y,everY,cnt_rounds)
        if curRounds!=-1:
            rounds.append(curRounds)
        continue
    cnt_rounds += 1
    if y > 0:
        opponents += p
    if x>opponents and y>0:
        y-=x-opponents
        opponents=0
        curRounds = ySum(y, everY, cnt_rounds)
        if curRounds != -1:
            rounds.append(curRounds)
    if x<=opponents and y>0:
        if x>=y:
            opponents-=x-y
            y=0
            x-=opponents
    if x<opponents and y<0:
        break
    if y <= 0 and opponents <= 0: #казарма и враги уничтожены, победа
        rounds.append(cnt_rounds)
        break
    if x <= 0: #наши солдаты уничтожены, поражение

        break
if isAlive!=0 and len(rounds)>0:
    print(min(rounds))
else:
    print(-1)
# print(rounds)
# print(everY)

