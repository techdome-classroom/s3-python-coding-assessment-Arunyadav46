def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize total to 0
    total = 0
    
    # Traverse through the Roman numeral string
    for i in range(len(s)):
        # If the current value is less than the next one, subtract it
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            # Otherwise, add it to the total
            total += roman_map[s[i]]
    
    return total

# Example usage:
s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

print(romanToInt(s1))  # Output: 3
print(romanToInt(s2))  # Output: 58
print(romanToInt(s3))  # Output: 1994





