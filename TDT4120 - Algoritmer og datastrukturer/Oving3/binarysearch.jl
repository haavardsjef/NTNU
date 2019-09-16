function binaryintervalsearch(x, delta, coordinate)
    println(x)
    p = 1
    r = div(length(x),2)
    median = 8 #x[div(r, 2),1:2]
    if p <= r
        q = div(p+r,2)
        if median-delta <= x[q, coordinate] &&  x[q, coordinate] <= median+delta
            print("FIRST")
            return binaryintervalsearch(x[p:q,1:2], delta, coordinate)
        elseif median-delta <= x[q, coordinate]
            print("SECOND")
            return binaryintervalsearch(x[p:q,1:2], delta, coordinate)
        else
            print("THIRD")
            return binaryintervalsearch(x[q+1:r,1:2], delta, coordinate)
        end

    end
    return none
end

x = [1 1; 2 1; 3 1; 5 1; 8 1; 12 1; 20 1; 21 1; 32 1]
print(binaryintervalsearch(x, 4, 1))
