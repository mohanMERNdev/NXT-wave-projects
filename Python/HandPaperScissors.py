abinav = input()
anjali = input()
if abinav == anjali:
    print("Tie")
elif abinav == "Paper" and anjali == "Rock":
    print("Abhinav Wins")
elif abinav == "Rock" and anjali == "Paper":
    print("Anjali Wins")
elif abinav == "Scissors" and anjali == "Paper":
    print("Abhinav Wins")
elif abinav == "Paper" and anjali == "Scissors":
    print("Anjali Wins")
elif abinav == "Rock" and anjali == "Scissors":
    print("Abhinav Wins")
elif abinav == "Scissors" and anjali == "Rock":
    print("Anjali Wins")
