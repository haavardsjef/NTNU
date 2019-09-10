function maxofdoublelinkedlist(linkedlist)
    element = linkedlist
    while element.next != nothing
        element = element.next
    end
    max = element.value
    while element.prev != nothing
        element = element.prev
        if element.value > max && element.value != nothing
            max = element.value
        end
    end
    return max
end
