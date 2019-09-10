function findindexinlist(linkedlist, index)
    node = linkedlist
    for i = 1:index-1
        if node.next == nothing
            return -1
        end
        node = node.next
    end
    return node.value
end
