statement = True
anime_list = []

while statement is True:
    anime_title = input('Enter the title of an anime (or type "exit" to finish): ')

    if anime_title.lower() == "exit":
        break
    else:
        anime_list.append(anime_title)
        continue
print("You have exited the anime entry program")
print("Your anime list include:")

for i in anime_list:
    print(f"- {i}")