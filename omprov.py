#Author: Tobias Blom
#Date 2023-11-27

tal = input("Vilka tabeller vill du beräkna? ")

my_list = []
prod = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = tal.split(" ")

if tal == "":
    print("Inga tal")

else:
    for num in my_list:
        for i in prod:
            print(f"{int(num)} * {int(i)} = {int(num) * int(i)}" )
        print("\n")

