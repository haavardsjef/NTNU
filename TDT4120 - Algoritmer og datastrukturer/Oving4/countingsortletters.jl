function countingsortletters(A, position)
    A = reverse(A)
    output = Array{String}(undef, length(A))
    count = zeros(Int64, 26)

    for i = 1: length(A)
        num = chartodigit(A[i][position])
        count[num] +=1
    end

    sum = 0
    # Make each index at count keep the sum of all previous counts
    for i = 1: length(count)
        sum += count[i]
        count[i] = sum
    end

    #
    for i = 1: length(A)
        pos = count[chartodigit(A[i][position])]
        count[chartodigit(A[i][position])] += -1
        output[pos] = A[i]
    end
    return output
end

function chartodigit(character)
    #Dette er en hjelpefunksjon for å få omgjort en char til tall
    #Den konverterer 'a' til 1, 'b' til 2 osv.
    #Eksempel: chartodigit("hei"[2]) gir 5 siden 'e' er den femte bokstaven i alfabetet.

    return character - '`'
end
