import re

def filter_characters(input_str):
    # Regular expression to match Korean and English characters
    pattern = re.compile('[가-힣a-zA-Z\s]')
    # Filtered string containing only Korean and English characters
    filtered_str = ''.join(pattern.findall(input_str))
    return filtered_str

# Test the function
input_str = "String -> Python###CookBook$@@@HotAir1234"
filtered_str = filter_characters(input_str)
print("Original string:", input_str)
print("Filtered string:", filtered_str)
