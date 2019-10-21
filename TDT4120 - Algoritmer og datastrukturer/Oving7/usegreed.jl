function usegreed(coins)
    # Din kode her
    for i=2:length(coins)
        if coins[i-1]%coins[i] > 0
            return false
        end
    end
    return true
end
