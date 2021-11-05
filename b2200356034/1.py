N = int(input("enter a number: "))

sum_of_odds = 0
sum_of_evens = 0
number_of_evens = 0

for i in range(1,N+1):
    if i % 2:
        sum_of_odds = sum_of_odds + i
    else:
        sum_of_evens = sum_of_evens + i
        number_of_evens += 1

print("sum of odd numbers is", sum_of_odds)
print("average of even numbers", sum_of_evens/number_of_evens)