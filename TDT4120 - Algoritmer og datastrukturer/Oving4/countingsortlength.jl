## Du skal implementere denne funksjonen
function countingsortlength(A)
    A = reverse(A)
    output = Array{String}(undef, length(A))
    count = zeros(Int64, 10)

    for i = 1: length(A)
        pos = length(A[i])+1
        count[pos] += 1
    end

    sum = 0
    # Make each index at count keep the sum of all previous counts
    for i = 1: length(count)
        sum += count[i]
        count[i] = sum
    end

    for i = 1: length(A)
        pos = count[length(A[i])+1]
        count[length(A[i])+1] += -1
        output[pos] = A[i]
    end
    return output
end
