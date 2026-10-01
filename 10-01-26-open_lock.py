from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        q = deque(["0000"])
        levels = 0
        visited = {"0000"}

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node in deadends:
                    continue

                if node == target:
                    return levels

                for i in range(4):
                    for dr in [-1, 1]:
                        new_node = list(node)
                        new_node[i] = str((int(new_node[i]) + dr) % 10)
                        new_node = "".join(new_node)

                        if new_node not in visited:
                            visited.add(new_node)
                            q.append(new_node)

            levels += 1

        return -1
