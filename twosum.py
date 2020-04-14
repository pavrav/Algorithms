# Complexity Analysis:

# Time complexity : O(n)O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the look up time to O(1)O(1), the time complexity is O(n)O(n).

# Space complexity : O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.

def twoSum1( nums, target ):

        dictionary = {}
        length = len( nums )
        
        for i in range( length ):
            dictionary[nums[i]] = i
            
        for i in range( length ):
            x = nums[i]
            difference = target - x
            j = dictionary[difference]
            if i != j:
                return i, j


# Complexity Analysis:

# Time complexity : O(n)O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1)O(1) time.

# Space complexity : O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.

def twoSum( nums, target ):

        dictionary = {}
        length = len( nums )
        
        for i in range( length ):
            difference = target - nums[i]
            if difference in dictionary:
                return dictionary[difference], i 
            dictionary[nums[i]] = i
            
        
print( twoSum( [2, 7, 22, 11, 15, 17], 22 ) )