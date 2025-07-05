print("==================")
print("Area Calculator 📐")
print("==================")
print()
choice_Tri = "1) Triangle"
print(choice_Tri)

choice_Rect= "2) Rectangle"
print(choice_Rect)

choice_sq= "3) Square"
print(choice_sq)

choice_Cir = "4) Circle"
print(choice_Cir)
choice_quit = "5) Quit"
print(choice_quit)

print()
choice = int(input("Which shape: "))

if choice == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))
    area = int((height * base)/2)
    print(f'The area is {area}')
elif choice == 2:
    length = int(input("Length: "))
    width = int(input("Width: "))
    area = int(length * width)
    print(f'The area is {area}')
elif choice == 3:
    side = int(input("Side: "))
    area = int(side**2)
    print(f'The area is {area}')
elif choice ==  4:
    pi = 3.14
    radius = int(input("Radius: "))
    area = int(pi*radius**2)
    print(f'The area is {area}')
elif choice == 5:
    print("Goodbye!")
else:
    print("Invalid choice. Please select a number between 1 and 5.")

