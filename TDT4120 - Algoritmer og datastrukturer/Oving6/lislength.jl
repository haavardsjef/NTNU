function lislength(s)
    mls = zeros(Int, size(s))
    mls[1] = 1

    for i = 2:length(s)
        # Din kode her
        mls[i] = 1
        for j = 1:i
            if s[i] > s[j] && mls[i] < mls[j] + 1
                mls[i] = mls[j]+1
            end
        end
    end
    return maximum(mls) # Returnerer det største tallet i listen
end
