import datetime as dt

DEBUG = False;

def wholesums_recursive(numbers, n):
    if DEBUG:
        print("wholesums_recursive: " + str(numbers) + ", " + str(n))

    # Create list of numbers left that can be used
    usable_numbers = [x for x in numbers if x <= n]

    # If we have exactly zero then this is the end of the line for this combination
    if n == 0:
        if DEBUG:
            print("[[0]]")
        return [[0]]
    # If non-zero and no usable numbers then this line will not work
    if len(usable_numbers) == 0:
        if DEBUG:
            print("None")
        return None

    # Define an empty solution at this level
    sols = []
    for each in usable_numbers:
        list_of_sols = wholesums_recursive(usable_numbers, n-each)
        # None means a failed line, so ignore
        if list_of_sols is not None:
            # zero list means terminated line, so set as the value each
            if list_of_sols == [[0]]:
                list_of_sols = [[each]]
            else:
                for sol in list_of_sols:
                    sol = sol.append(each)
            sols = combine_solutions(sols, list_of_sols)

    if DEBUG:
        print(str(sols))
    return sols


def combine_solutions(list1, list2):
    if list1 == []:
        return list2
    else:
        # order each of my sub lists, then take set
        return clean_solutions(list1 + list2)

def clean_solutions(list):
    if len(list) == 0:
        return list

    for each in list:
        each.sort()

    final_sols = []
    for each in list:
        if each not in final_sols:
            final_sols.append(each)

    return final_sols


if __name__ == "__main__":
    print(dt.datetime.now())

    ans = wholesums_recursive([3, 4, 5, 6, 7], 45)
    print(str(len(ans)) + "\n")
    print("\n\n\n" + str(ans))

    print(dt.datetime.now())
