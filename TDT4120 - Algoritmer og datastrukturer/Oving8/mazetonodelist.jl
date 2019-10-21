function mazetonodelist(maze)
    # Vi lager en matrise nodearray med størrelse tilsvarende maze,
    # men med Node-objekter isteden
    nodearray = Array{Node}(undef, size(maze, 1), size(maze, 2))

    for i in 1:size(maze, 1)
        for j in 1:size(maze, 2)
            # Fyll inn kode for å oppdatere nodearray
            if maze[i,j]==1
                nodearray[i,j] = Node(i, j, true)
            else
                nodearray[i,j] = Node(i, j, false)
            end

        end
    end

    for i=1:size(maze, 1)
        for j=1:size(maze, 2)
            # Fyll inn kode for å oppdatere neighbors til hver node
            # (Husk at naboene alltid er rett over, rett under,
            #  rett til venstre og/eller rett til høyre)
            neighbors = []

            try
                if nodearray[i-1,j].floor == true
                    push!(neighbors, nodearray[i-1,j])
                end
            catch
            end

            try
                if nodearray[i+1,j].floor == true
                    push!(neighbors, nodearray[i+1,j])
                end
            catch
            end

            try
                if nodearray[i,j-1].floor == true
                    push!(neighbors, nodearray[i,j-1])
                end
            catch
            end

            try
                if nodearray[i,j+1].floor == true
                    push!(neighbors, nodearray[i,j+1])
                end
            catch
            end
            nodearray[i,j].neighbors = neighbors

        end
    end
    # Fyll inn kode for å returnere en nodeliste ut ifra nodearray
    nodeliste = []
    for Node in nodearray
        if Node.floor == true
            push!(nodeliste, Node)
        end
    end
    return nodeliste
end






maze = [0 0 0 0 0 0 0
        1 1 0 1 1 1 0
        0 1 0 1 0 0 0
        0 1 0 1 1 1 0
        0 1 1 1 0 1 0
        0 1 0 1 0 1 1
        0 0 0 0 0 0 0]

mazetonodelist(maze)
