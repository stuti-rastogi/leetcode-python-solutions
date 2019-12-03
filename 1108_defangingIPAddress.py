class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

        # i = 0
        # while (i < len(address)):
        #     index = address[i:].find('.')
        #     if (index != -1):
        #         address = address[:index+i] + "[.]" + address[i+index+1:]
        #     i = i+index+2
        # return address