from convert import convert_num

# standard cases
print("converts binary to base 10", convert_num("0101", 2, 10 ) == 5)
print("converts binary to base 10", convert_num("101111100", 2, 10 ) == 380)

print("converts number to any base", convert_num("101111100", 2, 8 ) == "574" )
print("converts number to any base", convert_num("101111100", 2, 7 ) == "1052"  )
print("converts number to any base", convert_num("101111100", 2, 13 ) == "233"  )

# edge cases
print("handles hex with letter codes", convert_num("FF", 16, 10 ) == 255  )
print("handles error with invalid input", convert_num("40.456", 10, 2) == "Please enter an integer" )
print('handles negative numbers', convert_num("-90", 10, 2) == "-1011010")