# Suggest a solution to find the number of adults by name in a database

# create table persons (id int UNIQUE , name varchar NOT NULL , date_of_birth date);
# create primary key id;
# select count(*) from persons where name = "" and ( current_date - interval '18 years') >= date_of_birth

# Suppose we have an array of integers.
# We have to return the indices of two integers,
# such that if we add them up, we will reach to a specific target.


# [ 1 2 3 4 5] 5 -> (0 3) (1 2)
# [] 1  -> ()
# [1] 3 -> ()
# [1 2 3] 10 -> ()
# [-1 1 2 3 4 5] 0 -> (0 1)
# None -> ()


def find_target(nums: list, target: int) -> list:
    seen = {}

    for index, element in enumerate(nums):
        print(index, element)
        diff = target - element

        second_index = seen.get(element)
        print(second_index)

        if second_index is not None:
            return [second_index, index]

        seen[diff] = index
        print(seen)

    return None


# 3: 0 2: 1

# print(find_target([ 1,2, 3, 4, 5], 5))

# assert find_target([2,8,12,15], 20) == [1, 2], find_target([2,8,12,15], 20)
assert find_target([1, 2, 3], 4) == [0, 2], find_target([1, 2, 3], 4)
assert find_target([2, 2, 3], 4) in [[0, 1], [1, 0]]
assert find_target([2, 2], 4) in [[0, 1], [1, 0]]
assert find_target([8, 7, 2, 5, 3, 1], 10) in [[0, 2], [2, 0], [1, 4], [4, 1]]
assert find_target([1234, 5678, 9012], 14690) == [1, 2]
assert find_target([2, 7, 11, 15], 9) == [0, 1]
assert find_target([3, 2, 4], 6) == [1, 2]
assert find_target([3, 3], 6) == [0, 1]
assert find_target([1, 4, 45, 6, 10, 8], 16) == [3, 4]
assert find_target([0, 6], 6) == [0, 1]
assert find_target([6], 6) is None
