class Solution(object):

    def myAtoi( self, string ):
        """
        :type str: str
        :rtype: int
        """
        # We need to handle:
        # 1. trailing white spaces
        # 2. +/- sign
        # 3. invalid input
        # 4. oferflow
        
        result = i = 0
        sign = 1
        
        # 1. trailing white spaces
        while i < len( string ) and string[i] == ' ':
            i += 1
        
        # 2. +/- sign
        if i < len( string ) and ( string[i] == '-' or string[i] == '+' ):
            sign = 1-2 * ( string[i] == '-' )
            i += 1
            
        # 3. invalid input
        while i < len( string ) and string[i] >= '0' and string[i] <= '9':
            result = result * 10 + int( string[i] )
            
            # 4. oferflow
            if sign * result >= 2**31-1:
                return sign * ( 2**31-1 )
            if sign * result <= -2**31:
                return -2**31
            
            i += 1
            
        return sign * result


obj = Solution()
print( obj.myAtoi( '42' ) )