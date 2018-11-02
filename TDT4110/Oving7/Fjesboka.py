# Fjesboka, Oving 7 ITGK
# Håvard Hjelmeseth


# Definer funksjoner
def add_data(user):
    return user.split()


def get_person(given_name, facebook):
    list = []
    for person in facebook:
        if given_name == person[0]:
            list.append(person)
    return list


def main():
    facebook = []
    print('''Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status".''')
    while True:
        new_user = input("Add a new user: ")
        if new_user == "done" or new_user == "Done":
            print("OK")
            break
        else:
            facebook.append(add_data(new_user))
    while True:
        search = input("search for a user: ")
        if search == "done" or search == "Done":
            break
        else:
            people = get_person(search, facebook)
            if not people:
                print(people)
            for person in people:
                if person[3] == "Female":
                    print(person[0], person[1], "is", person[2],
                          "years old, her relationship status is", person[4])
                elif person[3] == "Male":
                    print(person[0], person[1], "is", person[2],
                          "years old, his relationship status is", person[4])


# Kall funksjoner
main()
