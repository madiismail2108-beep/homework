def number_trans(n):
    ones=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens=[ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens=['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if 0 <= n < 10: 
        return ones[n]
    elif 10 <= n <20:
        return teens[n]
    elif 20 <= n <100:
       d = (n // 10) - 2
       r = n % 10
       if r == 0:
           return tens[d]
       return f'{tens[d]} {ones[r]}'
    elif n == 100:
        return 'one hundred'
    else:
        return 'out of range'
    

number=int(input('reqam kiriting: '))
print(number_trans(number))

