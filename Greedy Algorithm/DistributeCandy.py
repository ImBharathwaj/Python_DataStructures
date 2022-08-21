class DistributeCandy:
    # @param A: list of integers
    # @return an integer
    @classmethod
    def candy(cls, A):
        # Length of an array
        n = len(A)
        data = sorted((x, i) for i, x in enumerate(A))

        # Assigning atleast one candy to each kid
        candies = [1]*n

        # Method to distribute candies to the kids
        for _, i in data:
            # Check the kid which is not standing at first at line
            # And checks the kid left side kid's rating
            if i > 0 and A[i] > A[i-1]:
                candies[i] = max(candies[i], candies[i-1]+1)
            # Check the kid which is not standing at last at line
            # And checks the kid right side kid's rating
            if i < n-1 and A[i] > A[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)        
        return sum(candies)

if __name__ == '__main__':
    dc = DistributeCandy()
    arr = [1,3,7,1]
    print(dc.candy(arr))
