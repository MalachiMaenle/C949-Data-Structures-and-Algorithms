class AVLPrint:
    @staticmethod
    def indent_lines(lines, number_of_spaces):
        if number_of_spaces <= 0:
            return
        indent = " " * number_of_spaces
        for i in range(len(lines)):
            lines[i] = indent + lines[i]

    @staticmethod
    def tree_to_lines(subtree_root):
        result = []
        if subtree_root is None:
            return result

        root_string = f"[{subtree_root.get_key()}]"
        root_str_len = len(root_string)

        if subtree_root.get_left() is None and subtree_root.get_right() is None:
            result.append(root_string)
            return result

        left_lines = AVLPrint.tree_to_lines(subtree_root.get_left())
        right_lines = AVLPrint.tree_to_lines(subtree_root.get_right())

        line_count = max(len(left_lines), len(right_lines))
        all_lines = [""] * (line_count + 2)

        if subtree_root.get_left() is None:
            all_lines[0] = root_string
            all_lines[1] = (" " * root_str_len) + "\\"

            right_child_indent = right_lines[0].find("[")

            if right_child_indent <= root_str_len:
                num_spaces = root_str_len - right_child_indent
                AVLPrint.indent_lines(right_lines, num_spaces)
            else:
                indent = " " * (right_child_indent - root_str_len)
                all_lines[0] = indent + all_lines[0]
                all_lines[1] = indent + all_lines[1]

            for i in range(len(right_lines)):
                all_lines[i + 2] = right_lines[i]

            return all_lines

        if subtree_root.get_right() is None:
            indent = " " * left_lines[0].find("]")
            all_lines[0] = indent + " " + root_string
            all_lines[1] = indent + "/"

            for i in range(len(left_lines)):
                all_lines[i + 2] = left_lines[i]

            return all_lines

        indent_needed = 0
        if len(right_lines) > 0:
            indent_needed = max(0,
                                (len(left_lines[0]) + len(root_string)) -
                                right_lines[0].find("["))
        for i in range(0, min(len(left_lines), len(right_lines)), 2):
            right_begin = right_lines[i].find("[")

            for_this_line = len(left_lines[i]) + 3 - right_begin
            indent_needed = max(indent_needed, for_this_line)

        absolute_indent = " " * indent_needed
        for i in range(max(len(left_lines), len(right_lines))):
            if i >= len(right_lines):
                all_lines[2 + i] = left_lines[i]
            else:
                left = ""
                if i < len(left_lines):
                    left = left_lines[i]
                right = absolute_indent + right_lines[i]
                all_lines[2 + i] = left + right[len(left):]

        left_index = all_lines[2].find("]")
        right_index = all_lines[2].rfind("[")
        all_lines[1] = (" " * left_index) + "/" + (" " * (right_index - left_index - 1)) + "\\"

        root_str_len = right_index - left_index - 1
        if len(root_string) < root_str_len:
            difference = root_str_len - len(root_string)
            underscores = "_" * (difference // 2)
            if 0 == difference % 2:
                root_string = underscores + root_string + underscores
            else:
                root_string = underscores + root_string + underscores + "_"

        all_lines[0] = (" " * (left_index + 1)) + root_string
        return all_lines

    @staticmethod
    def tree_to_string(subtree_root):
        if subtree_root is None:
            return "(empty tree)"

        lines = AVLPrint.tree_to_lines(subtree_root)

        tree_string = lines[0]
        for i in range(1, len(lines)):
            tree_string += ("\n" + lines[i])

        return tree_string
