import collections

number_of_shoes = int(input())
count_of_shoe_sizes = collections.Counter(map(int, input().split()))

number_of_customers = int(input())


total_earned = 0
shoe_size_desired_and_price_willing_to_pay = []
for _ in range(number_of_customers):
    (size_desired, price_willing_to_pay) = (map(int, input().split()))
    

    if count_of_shoe_sizes[size_desired] > 0:
        total_earned += price_willing_to_pay
        count_of_shoe_sizes[size_desired] -= 1

print(total_earned)
