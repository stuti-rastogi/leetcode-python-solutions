# Doing arithmetic operations - faster than string operations
#################################################################
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)


        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num:
            return 'Zero'

        result = ''
        if billion:
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result


# Doing string operations
#################################################################
# class Solution:
#     def convertToWords(self, numStr):
#         tenMultiplesMapping = {
#             '2': "Twenty",
#             '3': "Thirty",
#             '4': "Forty",
#             '5': "Fifty",
#             '6': "Sixty",
#             '7': "Seventy",
#             '8': "Eighty",
#             '9': "Ninety"
#         }

#         digitsMapping = {
#             '1': "One",
#             '2': "Two",
#             '3': "Three",
#             '4': "Four",
#             '5': "Five",
#             '6': "Six",
#             '7': "Seven",
#             '8': "Eight",
#             '9': "Nine"
#         }

#         tensMapping = {
#             "10": "Ten",
#             "11": "Eleven",
#             "12": "Twelve",
#             "13": "Thirteen",
#             "14": "Fourteen",
#             "15": "Fifteen",
#             "16": "Sixteen",
#             "17": "Seventeen",
#             "18": "Eighteen",
#             "19": "Nineteen"
#         }
#         numWord = []
#         if numStr == "000":
#             return None
#         if len(numStr) < 3:
#             numStr = '0'*(3-len(numStr)) + numStr

#         hundredsDigit = numStr[0]
#         if hundredsDigit != '0':
#             numWord += [digitsMapping[hundredsDigit], "Hundred"]

#         tensDigit = numStr[1]
#         if tensDigit == '1':
#             numWord += [tensMapping[numStr[1:]]]
#             return numWord
#         elif tensDigit != '0':
#             numWord += [tenMultiplesMapping[tensDigit]]

#         unitsDigit = numStr[2]
#         if unitsDigit != '0':
#             numWord += [digitsMapping[unitsDigit]]

#         return numWord


#     def numberToWords(self, num: int) -> str:
#         blocks = ["Thousand", "Million", "Billion"]
#         numStr = str(num)
#         if not num:
#             return "Zero"

#         wordsList = []
#         numStrLen = len(numStr)
#         blockCount = 0
#         index = numStrLen
#         while index > 0:
#             if index < 3:
#                 blockWordsList = self.convertToWords(numStr[:index])
#             else:
#                 blockWordsList = self.convertToWords(numStr[index-3:index])
#             if blockWordsList:
#                 if blockCount != 0:
#                     blockWordsList = blockWordsList + [blocks[blockCount-1]]
#                 wordsList = blockWordsList + wordsList
#             blockCount += 1
#             index = index - 3

#         return " ".join(wordsList)
