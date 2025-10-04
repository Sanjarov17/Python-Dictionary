def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\n1: Qo‘shish\n2: Barchasini ko‘rish\n3: Qidirish\n4: Chiqish")
        choice = input("Tanlov: ")
        
        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            phonebook[name] = phone
        elif choice == "2":
            for n, p in phonebook.items():
                print(n, "→", p)
        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            print(phonebook.get(name, "Topilmadi"))
        elif choice == "4":
            break
        else:
            print("Noto‘g‘ri tanlov")
            

phonebook_menu({})
