# @param {String[]} sentences
# @return {Integer}

# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

def most_words_found(sentences)
    max = 0
    for i in 0..(sentences.length()-1)
        spaces = sentences[i].count(" ")
        if spaces > max
            max = spaces
        end
    end
    max + 1
end