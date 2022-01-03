# https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defang = list(address)
        for i in range(len(defang)-1):
            if defang[i] == ".":
                defang[i] = "[.]"
        return "".join(defang)