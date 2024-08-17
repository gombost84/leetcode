class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        x = 0
        y = list(range(0, n * n))
        array = []
        coords: [0, 0]

        while x < len(y):
            array.append(y[x: x + n])
            x = x + n

        for command in commands:
            match command:
                case "UP":
                    coords[0] -= 1
                case "RIGHT":
                    coords[1] += 1
                case "DOWN":
                    coords[0] += 1
                case "LEFT":
                    coords[1] -= 1

        return array[coords[0]][coords[1]]


a = Solution()

a.finalPositionOfSnake(4, ["RIGHT", "DOWN"])
