# CSV separa os dados por virgula
with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]}-{row[1]}")
        language, category = line.rstrip().split(",")
        print(f"{language} -{category}")
