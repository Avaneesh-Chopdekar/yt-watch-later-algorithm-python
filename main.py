class VideoNode:
    def __init__(self, video_id, title):
        self.video_id = video_id
        self.title = title
        self.prev = None
        self.next = None

class WatchLaterList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.video_map = {}  # video_id -> node
        self.size = 0

    def _remove_node(self, node):
        # Remove from linked list
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next  # node was head

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # node was tail

        node.prev = node.next = None
        self.size -= 1

    def _insert_at_top(self, node):
        # Insert at front of list
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:  # first node
            self.tail = node
        self.size += 1

    def add(self, video_id, title):
        if video_id in self.video_map:
            # Move existing node to top
            node = self.video_map[video_id]
            self._remove_node(node)
            self._insert_at_top(node)
        else:
            # Add new node to top
            node = VideoNode(video_id, title)
            self._insert_at_top(node)
            self.video_map[video_id] = node

    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index.")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        self._remove_node(current)
        del self.video_map[current.video_id]

    def print_list(self):
        current = self.head
        index = 0
        print("Watch Later List:")
        while current:
            print(f"{index}: [{current.video_id}] {current.title}")
            current = current.next
            index += 1
        print("-" * 30)
