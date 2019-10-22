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
    while front(Q) != nothing
        u = dequeue!(Q)
        for v in u.neighbors
            if v.color == "white"
                v.color = "gray"
                v.distance = u.distance + 1
                v.predeecessor = u
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

x1 = Node(1,1)
x2 = Node(2,1)
x3 = Node(3,1)

nodearray = [x1, x2, x3]

bfs!(nodearray, x2)
