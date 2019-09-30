function dnasimilarity(s1, s2)
    sum = 0
    for i = 1: length(s1)
        if (s1[i] == s2[i])
            sum += 1
        end
    end
    return sum
end
