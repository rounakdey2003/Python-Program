def romanToInt(s):
  values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  result = 0
  for i in range(len(s)):
    value = values[s[i]]
    if i < len(s) - 1 and values[s[i + 1]] > value:
      result -= value
    else:
      result += value
  return result

s = "III"
print(romanToInt(s))