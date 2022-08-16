def knapsack(Capacity, weight, profits, n):
    if(n == 0 or Capacity == 0):
        return 0
    if(weight[n-1] > Capacity):
        return knapsack(Capacity, weight, profits, n-1)
    else:
        return max(profits[n-1]+knapsack(Capacity-weight[n-1], weight, profits, n-1), knapsack(Capacity, weight, profits, n-1))

if __name__ == '__main__':
    print('Enter the profit : ')
    profit = list(map(int, input().split(' ')))
    print('Enter the weight : ')
    weight = list(map(int, input().split(' ')))
    Capacity = int(input('Enter the capacity : '))
    n = len(weight)
    print(knapsack(Capacity, weight, profit, n))
