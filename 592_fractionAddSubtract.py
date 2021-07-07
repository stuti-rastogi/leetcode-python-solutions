class Fraction:
    def __init__(self, num, denom, isNegative):
        self.numerator = num
        self.denominator = denom
        self.negative = isNegative

    def convertToString(self):
        '''
            Convert a fraction object to string format like -1/3 or 3/1
        '''
        result = []
        if self.negative:
            result.append('-')
        result.append(str(self.numerator))
        result.append('/')
        result.append(str(self.denominator))
        return "".join(result)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expr_it = 0
        expr_len = len(expression)
        # will store all fraction objects
        fractions = []

        while (expr_it < expr_len):
            # store the sign for this fraction
            if expression[expr_it] == '-':
                isNegative = True
                expr_it += 1
            elif expression[expr_it] == '+':
                isNegative = False
                expr_it += 1
            else:
                # in the beginning we can have nothing at the beginning of this fraction
                isNegative = False

            numerator = 0
            while (expression[expr_it] != '/'):
                numerator = (numerator * 10) + int(expression[expr_it])
                expr_it += 1

            denominator = 0
            # to skip over the '/'
            expr_it += 1
            while (expr_it < expr_len and expression[expr_it] != '+' and expression[expr_it] != '-'):
                denominator = (denominator * 10) + int(expression[expr_it])
                expr_it += 1

            fractions.append(Fraction(numerator, denominator, isNegative))

        commonDenominator = 1
        # product of all denominators
        for fraction in fractions:
            commonDenominator *= fraction.denominator

        commonNumerator = 0
        for fraction in fractions:
            scaleFactor = commonDenominator // fraction.denominator
            if fraction.negative:
                sign = -1
            else:
                sign = 1
            # add/subtract the numerator scaled by the product of all other denominators
            commonNumerator += (scaleFactor * fraction.numerator * sign)

        if commonNumerator < 0:
            negativeAns = True
        else:
            negativeAns = False
        # reduce fraction to simplest form
        scaleDown = math.gcd(abs(commonNumerator), commonDenominator)
        resultNumerator = abs(commonNumerator) // scaleDown
        resultDenominator = commonDenominator // scaleDown

        resultFraction = Fraction(resultNumerator, resultDenominator, negativeAns)
        return resultFraction.convertToString()
