

zanswer = input("do you want to play hangman?")

if answer == "no":
    print("i gusse you don't have to")



if answer == "yes":
    print("awesome you will get six lives.  everytime you guess a letter wrong you lose a life")


    a = ["l","e","m","o","n"]




    n = 0
    while True:
        guess = input("guess a letter")
        if guess == a[0:5]:
            print(thz)
        if guess != a[0:5]:
            print("try again ")
            n += 1

        if(n > 5):
            break
