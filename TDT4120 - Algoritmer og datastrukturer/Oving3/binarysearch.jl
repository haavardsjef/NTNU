function binaryintervalsearch(x,delta, coordinate)
    middle = div(div(length(x),2)+1, 2)
    if div(length(x),2) % 2 == 1
        median = x[middle, coordinate]
    else
        median = (x[middle, coordinate] + x[middle+1, coordinate]) / 2
    end
    a = median - delta
    b = median + delta
    println("a: ", a, " b: ", b)
    start = binarylowest(x[:, coordinate], a)
    finish = binaryhighest(x[:, coordinate], b)
    if finish < start
        return -1, -1
    else
        return start, finish
    end
end

function binarylowest(x, v)
    low = 1
    high = length(x)
    if x[low] >= v
        return low
    end
    while low < high
        middle = div(low+high, 2)
        if x[middle] == v
            return middle
        elseif x[middle] < v && low != middle
            low = middle
        elseif x[middle] > v && middle != high
            high = middle
        else
            high = low = low + 1
        end
    end
    return low
end

function binaryhighest(x, v)

    low = 1
    high = length(x)
    if x[high] <= v
        return high
    end
    while low < high
        middle = div(low+high, 2)
         if x[middle] == v
            return middle
        elseif x[middle] < v && low != middle
            low = middle
        elseif x[middle] > v && middle != high
            high = middle
        else
            low = high = high - 1
        end
    end
    return low
end



x = [1.0, 2.0,3.0,4.0]
y = [1 2; 2 6; 4 1; 5 2]
z = [1.0 -1.0; 2.0 2.0; 3.0 3.0; 4.0 5.0; 5.0 5.0]
delta = 1.0
print(binaryintervalsearch(z, delta, 1))
#print(binarylowest(x, 2.4))
#print(binaryhighest(x, 2.6))
