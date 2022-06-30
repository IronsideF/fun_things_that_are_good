def fizzbuzz(num):
        if not num % 3 and not num % 5:
            return 'FizzBuzz'
        elif not num % 3:
            return 'Fizz'
        elif not num % 5:
            return 'Buzz'
        else:
            return str(num)

for num in range(1, 101):
    print(fizzbuzz(num))