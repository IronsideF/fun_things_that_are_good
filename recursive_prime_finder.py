def prime_nums(end):
    testing_range = range(1, end+1)
    prime_num_list = [2, ]
    for num in testing_range:
        is_prime = True
        for i in prime_num_list:
            if num % i == 0:
                is_prime = False   
            elif num == 1:
                is_prime = False   
        if is_prime == False:
            pass
        else:
            prime_num_list.append(num)
    print(prime_num_list)

prime_nums(int(input("This program will give you a list of all the prime numbers between 1 and whatever number you choose. Enter the number you want to list up to below. \n")))