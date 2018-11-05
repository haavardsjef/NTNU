# Generelt om filbehandling, Oving 9 ITGK
# Håvard Hjelmeseth


# Definer funksjoner
def write_to_file(data):
    f = open("my_file.txt", "w")
    f.write(data)
    return


def read_from_file(filename):
    f = open(filename)
    print(f.read())
    return


def main():
    while True:
        do = input("Hva vil du gjøre? (w/r) ")
        if do == "w":
            w = input("Hva vil du skrive? ")
            write_to_file(w)
        elif do == "r":
            read_from_file("my_file.txt")
        elif do == "done":
            print("Du er ferdig.")
            break


# Kjør funksjoner
main()

# python Generelt_om_filbehandling.py
