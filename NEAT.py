import os
import neat
import Game
import numpy as np


def eval_genomes(genomes, config):
    for _, genome in genomes:
        genome.fitness = 0 if genome.fitness == None else genome.fitness

        game = Game.Game()
        game.train_ai(genome, config)


def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-339')
    # p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10))

    winner = p.run(eval_genomes, 750)

    print(winner)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    run_neat(config)
