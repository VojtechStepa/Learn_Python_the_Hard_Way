def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print(f"Man that's enough for a party.")
    print(f"Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(30, 20)

print("OR, we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can evan do math inside too:")
cheese_and_crackers(5+6, 10 / 5)

print("And we can even combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers - 1000)