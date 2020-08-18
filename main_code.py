try:
    a = int(input("Enter the Number of Test Cases: "))
    main_list = []
    for i in range(a):
        case = input(f"Enter the Number {i + 1} to Find it's next Palindrome: ")
        if case.isnumeric() is False:
            print("Invalid Input! You can Only Use Numbers ")
            exit()
        else:
            case = list(case.split(" "))
            main_list.append(case)
    print("\n")
    for j in range(a):
        item = main_list[j]
        ref = item[0]
        item_0 = item[0]
        x = -1
        while True:
            item_0 = int(item_0)
            item_0 += 1
            item_0 = str(item_0)
            comp1 = list(item_0)
            comp2 = comp1.copy()
            comp2.reverse()
            if comp1 == comp2:
                comp2[:] = [''.join(comp2[:])]
                comp2 = comp2[0]
                comp2 = int(comp2)
                print(f"For {ref} --- {comp2} is the Next Palindrome")
                break
            elif comp1 != comp2:
                pass

except ValueError:
    print("Invalid Input! You can Only Use Numbers ")