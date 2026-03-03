def number_manipulation(*numbers):
    if len(numbers) == 0:
        print("No numbers provided")
        return

    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    for i in numbers:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
        total += i

    avg = total / len(numbers)

    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Average:", avg)

number_manipulation(2, 5, 3, 8, 1)

    # def number_manipulation(*numbers) :
    #
    #     largest = numbers[0]
    #     for i in numbers :
    #         if i > largest :
    #             largest = i
    #     print(largest)
    #
    #     smallest = numbers[0]
    #     for i in numbers:
    #         if i < smallest:
    #             smallest = i
    #     print(smallest)
    #
    #     num = 0
    #     for i in numbers:
    #         num = num + i
    #
    #     avg = num / len(numbers)
    #     print(avg)
