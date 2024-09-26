import sys

# TODO: handle decimal points

digits = "0123456789ABCDEF"

def main():
    result = convert_num(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(result)


def convert_num(number, base, newBase):
    if not number: 
        print('no number provided')
        exit

    if not base: 
        print('no base provided')
        exit

    if not newBase: 
        print('no new base provided for the conversion')
        return

    # do nothing if bases are the same
    if base == newBase:
        return number
    
    is_negative = number[0] == "-" 
    
    # throw an error if float or other invalid input entered
    try:
       
        # convert to decimal - split the sign from the number
        if (is_negative):
            base10 = int(number.split("-")[1], base)
        else: 
            base10 = int(number, base)
    except: 
        return "Please enter an integer"

    # convert number to new base
    new = decimal_to_base(base10, newBase)

    if (is_negative):
        return "-" + new
    else: 
        return new


# convert to a base other than 10
def decimal_to_base(base10, newBase):
    if newBase == 10:
        return base10
    
    result = ''
    
    while base10 > 0:
        result += digits[base10 % newBase]
        base10 //= newBase

    # return the result in reverse order
    return result[::-1]


if __name__ == '__main__':  
    main()