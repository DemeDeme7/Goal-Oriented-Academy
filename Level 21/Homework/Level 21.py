# 1)კომენტარებით ახსენით განსხვევება indexing-სა და sliceing-ს შორის.

# Indexing-ი არის ბრძანება,რომელიც გვეხმარება თითოეული სიის ელემენტის მისაწვდომად.
# Sliceing-ი არის ბრძანება,რომელსაც გამოაქნს სიის რომელიმე ან რამნედიმე ნაწილი ცალკე.

# 2)შექმენით სია სადაც გექნებათ 5 ელემენტი და მინუს ინდექსების გამოყენებით გამოიტანეთ ბოლო 3 ელემენტი
list = [20,17,"Hello",0.5,"GOA"]
last_3 = list[-3:]
print(last_3)

# 3)შექმენით სია სადაც გექნებათ 10 რიცხვი, გადაუარეთ ამ სიას და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია ან ტოლია 10ზე
numbers = [5,2,1,4,9,10,8,28,16,28]
for number in numbers:
    if number >= 10:
            print(number)
# 4)კომენტარის სახით ახსენით რა არის ფუქნცია, რაში ვიყენებთ და ჩამოწერეთ ყველა ნასწავლი ფუნქცია (გვერდით მიუწერეთ მათი დანიშნულება)

# ფუნქცია არის კოდის ნაწილი,რომელსაც გააჩნია საკუთარი სახელი და ასრულებს გარკვეულ დავალებას.
# ნაცნობი ფუნქციები:
# 1)print()-გამოაქვს მონაცემი ეკრანზე.
# 2)range()-ციკლის მიმდევნობის მითითება.
# 3)input()-იღებს ინფორმაციას მომხმარებლიდან.
# 4)type()-ამოწმებს მონაცემის ტიპს/კლასს.
# 5)int();str();float();-ცვლის მონაცემის ტიპებს.

# 5)(***BOSS LEVEL***) მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ უნდა თუ არა რომ მისი გვარი გადაიყვანოს დიდ ასოებად, თუ გიპასუხათ "yes" მაშინ დაუბეჭდეთ მისი სახელი დიდი ასოებით, თუ გიპასუხათ "no" დაუბეჭდეთ უბრალოდ მისი სახელი. (მინიშნება: გაკვეთილის ბოლოს განვიხილეთ ზედაპირულად)

surname = input("Please enter your surname:")
print("Would you like your surname to be converted to capital letters?")
choice = input("yes/no:")
yes = True
no = False
if choice == "yes":
      print(surname.upper())
elif choice == "no":
    print(surname)
else:
      print("Error")