
from repositories.user_repository import user_repository
from repositories.result_repository import result_repository

# For testing purposes only

while True:
    print("x: end, 1:add user, 2:list users, 3:find, 4:add result, 5:list_results")
    OUTPUT = input("Command: ")

    if OUTPUT == "x":
        break

    if OUTPUT == "1":
        USERNAME = input("username: ")
        PASSWORD = input("password: ")
        user_repository.create(USERNAME, PASSWORD)
        print("Added!")

    if OUTPUT == "2":
        USERS = user_repository.find_all_users()
        for u in USERS:
            print(u)

    if OUTPUT == "3":
        FIND = input("Who?: ")
        print(user_repository.find_user_by_username(FIND))

    if OUTPUT == "4":
        FIND = input("Who?: ")
        WHO = user_repository.find_user_by_username(FIND)
        print(WHO)
        result_repository.create(WHO.user_id, 100)

    if OUTPUT == "5":
        POINTS = result_repository.find_all_results()
        for p in POINTS:
            print(p)
