print("Welcome to the manhua/manhwa Recommender")
print("Answer a few question to find your next manhua/manhwa to read.")
genre_want = str(input("What genre you want to read? (action, romance, cultivation): "))
if genre_want == "action":
    genre = "action"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the manhua/manhwa be? (short, medium, long): "))
    if how_long == "short":
        decade = str(input("Which type do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend: The Breaker!!")
        elif decade == "historical":
            print("We recommend: Red Storm!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = str(input("Which type do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend:  Solo Leveling!!")
        elif decade == "historical":
            print("We recommend: Ruler of the Land!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = str(input("Which type do you want to watch? (modern, historical): "))
        if decade == "modern":
                print("We recommend: lookism!!")
        elif decade == "historical":
                print("We recommend: Kingdom!!")
        else:
                print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")
   

elif genre_want == "romance":
    genre = "romance"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the manhua/manhwa be? (short, medium, long): "))
    if how_long == "short":
        decade = str(input("Which type do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend: What's wrong with secretary Kim!!")
        elif decade == "modern":
            print("We recommend: Winter Wolf!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = str(input("Which type do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend: A good day to be a dog!!")
        elif decade == "historical":
            print("We recommend: Chang Ze Xhing!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = str(input("Which year do you want to watch? (modern, historical): "))
        if decade == "modern":
                print("We recommend: Daytime Star!!")
        elif decade == "historical":
                print("We recommend: Under the oak tree!!")
        else:
            print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")
   

elif genre_want == "cultivation":
    genre = "cultivation"
    print("your prefer genre is:", genre)
    how_long = str(input("How long should the manhua/manhwa be? (short, medium, long): "))
    if how_long == "short":
        decade = str(input("Which year do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend: I'm really not the demon God's lackey!!")
        elif decade == "historical":
            print("We recommend: Spare me, great lord!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "medium":
        decade = str(input("Which year do you want to watch? (modern, historical): "))
        if decade == "modern":
            print("We recommend: Tales of demons and Gods!!")
        elif decade == "historical":
            print("We recommend: Martial Peak!!")
        else:
            print("maybe there's something wrong?")
    elif how_long == "long":
        decade = str(input("Which year do you want to watch? (modern", "historical): "))
        if decade == "modern":
                print("We recommend: Versatile Mage!!")
        elif decade == "historical":
                print("We recommend: Magic Emperor!!")
        else:
                print("maybe there's something wrong?")
    else:
        print("maybe there's something wrong")

else:
     print("Maybe you type something wrong?")   