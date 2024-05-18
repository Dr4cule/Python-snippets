import random
#import using import RockPaperScissors or from RockPaperScissors import RCP or as Rsp
def RCP(mc, *others):
    mc = mc.lower()
    user = 0
    comp = 0
    print("Rock ⚫, Paper 📄, Scissors ✂️\n")
    if mc not in ["rock", "paper", "scissors"]:
        print("Invalid input, choose between rock ⚫, paper 📄 or scissors ✂️\n\nTry again\n")
        RCP(input("Choose between rock ⚫, paper 📄 or scissors ✂️  : "))
    cc = random.choice(["rock", "paper", "scissors"])
    if mc == "rock" and cc == "scissors":
        user += 1
    elif mc == "paper" and cc == "rock":
        user += 1
    elif mc == "scissors" and cc == "paper":
        user += 1
    else:
        comp += 1    
    if mc == cc:
        print(f"Tie 🙃\nYour choice was: {mc}\nComputer's choice was: {cc}")
    elif mc == "rock":
        if cc == "scissors":
            print(f"You win 🎉\nYour choice was: {mc}\nComputer's choice was: {cc}")
        else:
            print(f"You lose 😞\nYour choice was: {mc}\nComputer's choice was: {cc}")
        print(f"\nYour score: {user}\nComputer's score: {comp}")    
    elif mc == "paper":
        if cc == "rock":
            print(f"You win 🎉\nYour choice was: {mc}\nComputer's choice was: {cc}")
        else:
            print(f"You lose 😞\nYour choice was: {mc}\nComputer's choice was: {cc}")
        print(f"\nYour score: {user}\nComputer's score: {comp}")    
    elif mc == "scissors":
        if cc == "paper":
            print(f"You win 🎉\nYour choice was: {mc}\nComputer's choice was: {cc}")
        else:
            print(f"You lose 😞\nYour choice was: {mc}\nComputer's choice was: {cc}")
        print(f"\nYour score: {user}\nComputer's score: {comp}")    
    else:
        print("")
        print(f"\nComputer's choice was: {cc}")

    choice = ["yes", "no"]
    ans = input("\nDo you want to play again? 🤔\n:")
    if ans.lower() not in choice:
        print("Invalid input, try again")
        ans = input("\nDo you want to play again? 🤔\n:")
    if ans.lower() == "yes":
        mc = input("Choose between rock ⚫, paper 📄 or scissors ✂️ : ")
        RCP(mc)
    else:
        print("\nBye 👋, thanks for playing!")
        exit()

RCP(input("Choose between rock 🪨, paper 📄 or scissors ✂️  : "))
