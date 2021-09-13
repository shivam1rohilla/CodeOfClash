call_1, call_2 = input().split()
r=[("ROCK","SCISSORS"),("SCISSORS","PAPER"),("PAPER","ROCK")]
if call_1==call_2:
    print("DRAW")
elif (call_1,call_2) in r:
    print("PLAYER1")
else:
    print("PLAYER2")
