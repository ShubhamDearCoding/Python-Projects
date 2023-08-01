num_of_terms = int(input("enter number of terms "))
i = 0
first_term = 0
second_term = 1
print(first_term, second_term, end=" ")
while i < num_of_terms - 2:
    third_term = first_term + second_term 
    first_term = second_term 
    second_term = third_term
    print(third_term, end=" ")
    i += 1