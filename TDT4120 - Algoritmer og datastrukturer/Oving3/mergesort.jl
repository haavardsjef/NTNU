#x og y er to sorterte arrays, coordinate angir koordinat akse
function mergearrays(x,y,coordinate)
    temp = []
    i = 1
    j = 1
    while i <= (length(x)/2) && j <= (length(y)/2)
        if x[i,coordinate] == y[j, coordinate]
            if x[i,(coordinate%2)+1] < y[j, (coordinate%2)+1]
                if length(temp) == 0
                    temp = x[i:i,1:2]
                else
                    temp = vcat(temp, x[i:i,1:2])
                end
                i = i + 1
            else
                if length(temp) == 0
                    temp = y[j:j,1:2]
                else
                    temp = vcat(temp, y[j:j,1:2])
                end
                j = j + 1
            end
        elseif x[i,coordinate] < y[j, coordinate]
            if length(temp) == 0
                temp = x[i:i,1:2]
            else
                temp = vcat(temp, x[i:i,1:2])
            end
            i = i + 1
        else
            if length(temp) == 0
                temp = y[j:j,1:2]
            else
                temp = vcat(temp, y[j:j,1:2])
            end
            j = j + 1
        end
    end
        while i <= (length(x)/2)
            if length(temp) == 0
                temp = x[i:i,1:2]
            else
                temp = vcat(temp, x[i:i,1:2])
            end
            i = i + 1
        end
        while j <= (length(y)/2)
            if length(temp) == 0
                temp = y[j:j,1:2]
            else
                temp = vcat(temp, y[j:j,1:2])
            end
            j = j + 1
        end
        return temp
end

#x usortert array, coordinate angir koordinat akse vi skal sortere langs
function mergesort(x, coordinate)
    p = 1
    r = div(length(x),2)
    if p < r
        q = div(p+r,2)
        a = x[p:q,1:2]
        b = x[q+1:r,1:2]
        a = mergesort(a, coordinate)
        b = mergesort(b, coordinate)
        result = mergearrays(a,b,coordinate)
    else
        result = x
    end
    return result
end

x = [3.0 1.0; 2.0 2.0; 3.0 3.0]
y = [5 2; 7 6; 12 1; 17 5]
print("----")
print(mergesort(x, 1))
