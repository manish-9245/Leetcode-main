class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Calculate the GCD of lengths of str1 and str2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        len_gcd = gcd(len(str1), len(str2))
        gcd_str = str2[:len_gcd]  # Get the potential GCD string
        
        # Check if the potential GCD string divides both str1 and str2
        if gcd_str * (len(str1) // len_gcd) == str1 and gcd_str * (len(str2) // len_gcd) == str2:
            return gcd_str
        
        return ""
