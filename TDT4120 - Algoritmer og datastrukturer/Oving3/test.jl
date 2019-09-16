function binaryintervalsearch(x, delta, coordinate)
    if length(x) == 0
        return -1, -1
    end
    middle = div(length(x)+1, 2)
    median = x[middle]
    a = binarysearch(x, 1, length(x), median-delta)
    b = binarysearch(x, 1, length(x), median+delta)
    return a, b
end

function binarysearch(x, p, r, v)
    if p <= r
        q = div(p+r,2)
        if v == x[q]
            return q
        elseif v < x[q] && v > x[q-1] && q != 1
            return q
        elseif v < x[q] && q != 1
            println(p," ", q)
            return binarysearch(x, p, q-1, v)
        elseif v < x[q+1] && v > x[q]
            return q
        elseif v < x[q+1] && v > x[q]
            return q
        else
            return binarysearch(x, q+1, r, v)
        end
    end
    if p <= v
        return p
    else
        return r
    end
    return none
end

x = [1, 2, 3, 5, 8, 12, 20, 21, 32, 40]
#print(binaryintervalsearch(x, 3, 20))
#(binarysearch(x, 1, 9, 20))
print(binaryintervalsearch(x, 13, 1))
