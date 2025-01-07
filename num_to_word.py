def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def convert_hundreds(n):
        if n == 0:
            return ""
        elif n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])
        else:
            return ones[n // 100] + " hundred" + ('' if n % 100 == 0 else ' ' + convert_hundreds(n % 100))

    if n == 0:
        return "zero"
    result = []
    thousands = ["", "thousand", "million", "billion"]
    i = 0
    while n > 0:
        if n % 1000 != 0:
            result.append(convert_hundreds(n % 1000) + ('' if thousands[i] == "" else ' ' + thousands[i]))
        n //= 1000
        i += 1

    return ' '.join(result[::-1])

# Example usage:
print(number_to_words(2456))  # Output: "two thousand four hundred fifty-six"
