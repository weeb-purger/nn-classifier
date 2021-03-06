import os

from weeb_classifier.console_scripts import argument_parser
from weeb_classifier.neural_net.neural_network import NeuralNetwork

os.environ['PYTHONWARNINGS'] = 'ignore'
NEURAL_NETWORK = NeuralNetwork()


def train():
    if not NEURAL_NETWORK.trained:
        NEURAL_NETWORK.train(training_dir=os.environ["TRAINING_DIR"], validation_dir=os.environ[
            "VALIDATION_DIR"])
    else:
        print("Neural network is already trained.")


def solve():
    args = argument_parser.default()
    images = args.images
    results = [str(NEURAL_NETWORK.solve(img, args.confidence_level)) for img in images]
    print(str(args.separator).join(results))


if __name__ == '__main__':
    solve()
