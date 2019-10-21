function mincoinsgreedy(coins, value)
    # Din kode her
    i = 1
    nr_coins = 0
    while value > 0
        println(value, " / ", coins[i])
        num = div(value, coins[i])
        println(num)
        value -= num * coins[i]
        nr_coins += num
        i += 1
        println("value", value)
    end
    return nr_coins
end

coins= [1000, 500, 100, 5, 1]
value=199
println(mincoinsgreedy(coins, value))
