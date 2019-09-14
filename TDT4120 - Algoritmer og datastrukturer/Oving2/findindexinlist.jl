function findindexinlist(linkedlist, index)
    node = linkedlist.next
    for i = 0:index
        next = node.next
    end

    return node.value
end
