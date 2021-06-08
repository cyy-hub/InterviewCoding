class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def merge_list(l1,l2):
    dummpy = ListNode(0)
    cur_node = dummpy
    while(l1 and l2):
        if l1.val < l2.val:
            cur_node.next = ListNode(l1.val)
            cur_node = cur_node.next
            l1 = l1.next
        else:
            cur_node.next = ListNode(l2.val)
            cur_node = cur_node.next
            l2 = l2.next
    cur_node.next = l1 if l1 else l2
    return dummpy.next