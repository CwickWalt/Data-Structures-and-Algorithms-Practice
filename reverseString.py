def stringReversal(string):
    indexReversed = len(string) - 1
    stringReversed = ''
    for i in string:
        if not string or len(string) < 2 or isinstance(string, str) not True:
            print('This is not a valid input')
        else:
            stringReversed = stringReversed + string[indexReversed]
            indexReversed = indexReversed - 1
            if indexReversed == -1:
                return stringReversed

string = 'It shall be reversed!'

stringReversal(string)
