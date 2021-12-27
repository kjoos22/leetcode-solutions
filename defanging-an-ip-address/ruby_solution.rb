# @param {String} address
# @return {String}

#https://leetcode.com/problems/defanging-an-ip-address

def defang_i_paddr(address)
    defang = address.split("")
    for i in 0..(defang.length()-1)
        if defang[i] == "."
            defang[i] = "[.]"
        end
    end
    defang.join
end