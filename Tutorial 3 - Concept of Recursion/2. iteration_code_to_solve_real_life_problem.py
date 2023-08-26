#This is using the iteration approach (by looping) to solve our real life problem explained
#in '1. What_is_Recursion_(explained_with_real_life_problem).txt'
def find_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == '__main__':
    print(find_sum(5))