def prime_nums(initial, end):
    testing_range = list(range(initial, end))
    prime_num_list = [2, ]
    for num in testing_range:
        is_prime = True
        for i in prime_num_list:
            if num % i == 0:
                is_prime = False      
        if is_prime == False:
            pass
        else:
            prime_num_list.append(num)
    print(prime_num_list)

prime_nums(3, 101)