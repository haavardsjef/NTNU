using DataStructures: Queue, enqueue!, dequeue!

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
    goalnode = nothing
    Q = Queue{Node}()
    enqueue!(Q, start)
    while !isempty(Q)
        u = dequeue!(Q)
        for v in u.neighbors
            if v.color == "white"
                v.color = "gray"
                v.distance = u.distance + 1
                v.predecessor = u
                enqueue!(Q, v)
                if isgoalnode(v)
                    goalnode = v
                end
            end
        end
        u.color = "black"
    end
    return goalnode
end


# maze = [0 0 0 0 0
#         0 1 1 1 0
#         0 1 0 0 0
#         0 1 1 1 0
#         0 0 0 0 0]

nodelist = [Node(2, 2), Node(3, 2), Node(4, 2), Node(2, 3),
            Node(4, 3), Node(2, 4), Node(4, 4)]

nodelist[1].neighbors = [nodelist[2], nodelist[4]]
nodelist[2].neighbors = [nodelist[1], nodelist[3]]
nodelist[3].neighbors = [nodelist[2], nodelist[5]]
nodelist[4].neighbors = [nodelist[1], nodelist[6]]
nodelist[5].neighbors = [nodelist[3], nodelist[7]]
nodelist[6].neighbors = [nodelist[4]]
nodelist[7].neighbors = [nodelist[5]]


setgoalnode(nodelist[7])
result = bfs!(nodelist, nodelist[1])

println(result!=nothing)
