def count_ways(n):
    # Implement this function

    if n<=1:
        return 1
    
    return count_ways(n-1)+count_ways(n-2)
if __name__ == "__main__":
    steps = int(input("Enter the number of steps in the staircase: "))
    result = count_ways(steps)
    print(f"There are {result} ways to climb to the top of a {steps}-step staircase.")