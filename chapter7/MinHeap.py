class MaxHeap:
    def __init__(self):
        self.heap_list = []

    def get_heap_data_string(self):
        return str(self.heap_list)

    def get_length(self):
        return len(self.heap_list)

    def insert(self, value):
        print(f"insert({value}):")
        self.heap_list.append(value)

        self.percolate_up(len(self.heap_list) - 1)

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_list[node_index]
        heap_size = len(self.heap_list)
        while child_index < heap_size:
            max_value = value
            max_index = -1
            for i in range(min(2, heap_size - child_index)):
                if self.heap_list[i + child_index] > max_value:
                    max_value = self.heap_list[i + child_index]
                    max_index = i + child_index
            if max_value == value:
                return
            else:
                print(f"   percolate_down() swap: ", end="")
                print(f"{self.heap_list[node_index]} <-> ", end="")
                print(f"{self.heap_list[max_index]}")
                temp = self.heap_list[node_index]
                self.heap_list[node_index] = self.heap_list[max_index]
                self.heap_list[max_index] = temp
                node_index = max_index
                child_index = 2 * node_index + 1

    def percolate_up(self, node_index):
        while node_index > 0:
            parent_index = (node_index - 1) // 2
            if self.heap_list[node_index] <= self.heap_list[parent_index]:
                return
            else:
                print("   percolate_up() swap: ", end="")
                print(f"{self.heap_list[parent_index]} <-> ", end="")
                print(self.heap_list[node_index])
                temp = self.heap_list[node_index]
                self.heap_list[node_index] = self.heap_list[parent_index]
                self.heap_list[parent_index] = temp
                node_index = parent_index

    def remove(self):
        print("remove():")
        max_value = self.heap_list[0]

        replace_value = self.heap_list.pop()
        if len(self.heap_list) > 0:
            self.heap_list[0] = replace_value
            self.percolate_down(0)

        return max_value