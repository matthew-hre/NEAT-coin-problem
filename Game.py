import neat

global highest
highest = 0


class Game:
    def __init__(self):
        self.game = [1] * 5
        self.moves = []

    def switch(self, row: int):
        if row < len(self.game) - 2 and self.game[row] != 0:
            temp = self.game[row + 2]
            self.game[row + 2] = self.game[row + 1]
            self.game[row + 1] = temp
            self.game[row] -= 1
            self.moves.append([*self.game])
            return True
        else:
            self.moves.append([*self.game])
            return False

    def promote(self, row: int):
        if row < len(self.game) - 1 and self.game[row] != 0:
            self.game[row + 1] += 2
            self.game[row] -= 1
            self.moves.append([*self.game])
            return True
        else:
            self.moves.append([*self.game])
            return False

    def test_end(self):
        return (self.game[0] == 0 and self.game[1] == 0 and self.game[2] == 0 and self.game[3] == 0)

    def train_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        while not self.test_end():
            output = net.activate(self.game)
            move = output.index(max(output))

            if move in (0, 1, 2):
                self.switch(move)
            elif move in (3, 4, 5, 6):
                self.promote(move - 3)

            if len(self.moves) > 2 and self.moves[-1] == self.moves[-2] == self.moves[-3]:
                self.calculate_fitness(genome, config)
                break

        if self.test_end():
            self.calculate_fitness(genome, config)

        global highest
        if self.game[-1] > highest:
            highest = self.game[-1]
            print("New highest score: " + str(highest))
            # for move in self.moves:
            #     print(*move)

            pattern = ""

            for move in self.moves:
                pattern += str(move) + "\n"

            with (open("highest.txt", "w")) as f:
                f.write("--- SCORE PATTERN FOR " +
                        str(highest) + "---" + "\n" + pattern)

    def calculate_fitness(self, genome, config):
        genome.fitness = self.game[-1]
