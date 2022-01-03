/**
 * @param {string} address
 * @return {string}
 */

// https://leetcode.com/problems/defanging-an-ip-address

var defangIPaddr = function(address) {
    defang = address.split("")
    for (let i = 0; i < defang.length; i++) {
        if (defang[i] == ".") {
            defang[i] = "[.]"            
        }
    }
    return defang.join("")
};