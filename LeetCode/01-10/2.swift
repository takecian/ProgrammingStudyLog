class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {

        if let l1 = l1, l1.next == nil, l1.val == 0 {
            return l2
        }
        if let l2 = l2, l2.next == nil, l2.val == 0 {
            return l1
        }

        var l1 = l1, l2 = l2

        var needToAddOne = false

        var first: ListNode? = nil
        var current: ListNode? = nil
        while true {
            guard l1 != nil || l2 != nil else {
                if needToAddOne {
                    current?.next = ListNode(1)
                }
                break
            }
            let l1Value = l1?.val ?? 0
            let l2Value = l2?.val ?? 0

            var sum = l1Value + l2Value + (needToAddOne ? 1 : 0)
            needToAddOne = sum > 9
            sum = sum % 10

            if let ne = current {
                let nextNode = ListNode(sum)
                ne.next = nextNode
                current = ne.next
            } else {
                first = ListNode(sum)
                current = first
            }

            l1 = l1?.next
            l2 = l2?.next
        }

        return first
    }
}