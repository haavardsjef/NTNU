
function mazetonodelist(maze)
    # Vi lager en matrise nodearray med størrelse tilsvarende maze,
    # men med Node-objekter isteden
    nodearray = Array{Node}(undef, size(maze, 1), size(maze, 2))

    for i in 1:size(maze, 1)
        for j in 1:size(maze, 2)
            # Fyll inn kode for å oppdatere nodearray
            if maze[i,j]==1
                nodearray[i,j] = Node(i, j)
            end
        end
    end

    for i in 1:size(maze, 1)
        for j in 1:size(maze, 2)
            # Fyll inn kode for å oppdatere neighbors til hver node
            # (Husk at naboene alltid er rett over, rett under,
            #  rett til venstre og/eller rett til høyre)
            if isdefined(nodearray[i,j])
                println(nodearray[i,j])
            end
        end
    end

    # Fyll inn kode for å returnere en nodeliste ut ifra nodearray
end






maze = [0 0 0 0 0 0 0
        1 1 0 1 1 1 0
        0 1 0 1 0 0 0
        0 1 0 1 1 1 0
        0 1 1 1 0 1 0
        0 1 0 1 0 1 1
        0 0 0 0 0 0 0]

mazetonodelist(maze)
