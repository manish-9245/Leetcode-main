class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_types = 3
        
        if any('a' <= c <= 'z' for c in password):
            missing_types -= 1
        if any('A' <= c <= 'Z' for c in password):
            missing_types -= 1
        if any(c.isdigit() for c in password):
            missing_types -= 1
        
        replacements = 0
        ones = 0
        twos = 0
        i = 2
        changes = 0
        
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                
                changes += length // 3
                if length % 3 == 0:
                    ones += 1
                elif length % 3 == 1:
                    twos += 1
            i += 1
        
        if n < 6:
            return max(missing_types, 6 - n)
        
        deletions = max(n - 20, 0)
        changes -= min(deletions, ones * 1) // 1
        changes -= min(max(deletions - ones, 0), twos * 2) // 2
        changes -= max(deletions - ones - 2 * twos, 0) // 3
        
        return deletions + max(missing_types, changes)