function bfs!(nodes, start)
    for node in nodes
        if node != start
            node.color = "white"
            node.distance = length(nodes)+1 #Inf
            node.predecessor = nothing
        else
            node.color = "gray"
            node.distance = 0
            node.predecessor = nothing
        end
    end
    Q = Queue{Node}()
    enqueue!(Q, start)
    while !isempty(Q)
        u = dequeue!(Q)
        for v in u.neighbors
            if v.color == "white"
                v.color = "gray"
                v.distance = u.distance + 1
                v.predecessor = u
                if isgoalnode(v)
                    return v
                end
                enqueue!(Q, v)
            end
        end
        u.color = "black"
    end
    return nothing
end
