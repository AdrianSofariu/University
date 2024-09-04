# backtracking problem 10, dp problem 3

# A group of n (n<=10) persons, numbered from 1 to n are placed on a row of chairs,
# but between every two neighbor persons (e.g. persons 3 and 4, or persons 7 and 8)
# some conflicts appeared. Display all the possible modalities to replace the persons,
# such that between any two persons in conflict stay one or at most two other persons.


def consistent(placement: list) -> bool:
    """
    Function to check if the current progress can lead to a valid solution
    :param placement:
    :return:
    """
    # check if elements on adjacent positions are neighbours
    for i in range(1, len(placement)):
        if abs(placement[i] - placement[i-1]) == 1:
            return False
    # check if the array contains duplicates
    if len(set(placement)) != len(placement):
        return False
    return True


def recursive_backtracking(placement: list, n: int):
    """
    Recursive procedure to generate all possible methods to place the n persons
    such that no 2 neighbours are adjacent
    :param placement:
    :param n:
    :return:
    """
    if len(placement) == n:
        print(placement)
    if len(placement) > n:
        return
    placement.append(0)
    for i in range(1, n + 1):
        placement[-1] = i
        if consistent(placement):
            recursive_backtracking(placement, n)
            placement.pop()


def iterative_backtracking(n: int):
    """
    Iterative procedure to generate all possible methods to place the n persons
    such that no 2 neighbours are adjacent
    :param n: 
    :return:
    """
    placement = [0]
    while len(placement) > 0:
        valid = False
        while not valid and placement[-1] < n:
            placement[-1] = placement[-1] + 1
            valid = consistent(placement)
        if valid:
            if len(placement) == n:
                print(placement)
            placement.append(0)
        else:
            # placement = placement[:-1]
            placement.pop()


if __name__ == "__main__":
    try:
        row = []
        nr_persons = int(input("Choose a number of persons: "))
        print("Recursive solution")
        recursive_backtracking(row, nr_persons)
        print("\nIterative solutions")
        iterative_backtracking(nr_persons)
    except ValueError:
        print("n should be a number")
