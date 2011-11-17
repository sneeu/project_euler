DIGITS = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number_to_word(n):
    if n == 1000:
        return 'one thousand'

    if n < 10:
        return DIGITS[n]
    elif n < 20:
        return TEENS[n - 10]
    elif n < 100:
        remainder = number_to_word(n % 10)
        if remainder:
            remainder = ' ' + remainder
        else:
            remainder = ''
        return '%s%s' % (TENS[n / 10], remainder)
    elif n < 1000:
        remainder = number_to_word(n % 100)
        if remainder:
            remainder = ' and ' + remainder
        else:
            remainder = ''
        return ('%s hundred' % (DIGITS[n / 100])) + remainder


print len(''.join([number_to_word(i).replace(' ', '') for i in range(1, 1001)]))
print len(''.join([number_to_word(i).replace(' ', '') for i in range(1, 1001)]))
