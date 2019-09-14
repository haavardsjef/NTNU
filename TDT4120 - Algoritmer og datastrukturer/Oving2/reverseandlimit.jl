function reverseandlimit(array, maxnumber)
    reversed = []
    for i=0:length(array)-1
        push!(reversed, array[length(array)-i])
    end
    for i=1:length(reversed)
        if reversed[i] > maxnumber
            reversed[i] = maxnumber
        end
    end
    return reversed
end
