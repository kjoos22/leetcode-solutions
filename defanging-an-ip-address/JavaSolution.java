// https://leetcode.com/problems/defanging-an-ip-address/

class Solution {
    public String defangIPaddr(String address) {
        String defang = "";
        for(int i = 0; i < address.length(); i++) {
            if (address.charAt(i) == '.') {
                defang += "[";
                defang += address.charAt(i);
                defang += "]";                
            } else {
                defang += address.charAt(i);
            }         
        }
        return defang;
    }
}