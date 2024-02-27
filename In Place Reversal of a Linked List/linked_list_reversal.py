def reverse_linked_list(head, k):
	previous, current, next = None, head, None
	for _ in range(k):
		# temporarily store the next node
		next = current.next
		# reverse the current node
		current.next = previous
		# before we move to the next node, point previous to the
        # current node
		previous = current
		# move to the next node 
		current = next
	return previous, current