n = int(input())
victories =[]
for i in range(n):
    player_win_lose = input().split()
    if player_win_lose[1] == "win":
        victories.append(player_win_lose[0])
print(victories)
print(len(victories))
