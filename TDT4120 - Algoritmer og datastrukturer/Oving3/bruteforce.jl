# Hvis du fortsatt er med, godt jobbet! Som et lite pust i bakken skal du nå implementere en bruteforce løsning på problemet med å finne den minste avstanden mellom to punkter. Likevel skal du ikke være helt naiv og bruke n^2 sammenligninger, men heller n(n-1)/2.
#
# Grunnen til at du skal implementere denne naive løsningen nå er at den skal brukes i basistilfellet i vår rekursive splitt og hersk løsning som vi skal implementere i siste oppgave.
function bruteforce(x)
    shortest = 9999
    for i=1:div(length(x),2)-1
        j = i
        while j < div(length(x),2)
            j = j + 1
            println("i: ", i, " j: ", j)
            if shortest > calculateDistance(x[i,1:2],x[j,1:2])
                shortest = calculateDistance(x[i, 1:2], x[j, 1:2])
            end

        end
    end
    return shortest
end

function calculateDistance(x,y)
    return (abs2(x[1]-y[1])+abs2(x[2]-y[2]))^0.5
end

x = [1 1; 10 0; 2 2; 5 5]
print(bruteforce(x))
