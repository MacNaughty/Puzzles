

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    } else if l2 == nil {
        return l1
    }
    
    var head *ListNode
    if l1.Val <= l2.Val {
        head = l1
        l1 = l1.Next
    } else {
        head = l2
        l2 = l2.Next
    }
    currNode := head
    
    for l1 != nil && l2 != nil {
        if l1.Val <= l2.Val {
            currNode.Next = l1
            l1 = l1.Next
            currNode = currNode.Next
        } else {
            currNode.Next = l2
            l2 = l2.Next
            currNode = currNode.Next
        }
    }
    
    if l1 != nil {
        currNode.Next = l1
    }
    if l2 != nil {
        currNode.Next = l2
    }
    
    
    
    return head
}


func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    res := &ListNode{}
    fakeHead := res
    
    for l1!=nil && l2!=nil {
        if l1.Val < l2.Val {
            res.Next = l1
            l1 = l1.Next
        } else {
            res.Next = l2
            l2 = l2.Next
        }
        res = res.Next
    }
    
    if l1!=nil {
        res.Next = l1
    } else if l2!=nil {
        res.Next = l2
    }
    
    return fakeHead.Next
}
