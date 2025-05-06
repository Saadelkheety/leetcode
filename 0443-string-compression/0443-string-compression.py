class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            current_char = chars[read]
            count = 0
            
            # Count consecutive occurrences
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = current_char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write