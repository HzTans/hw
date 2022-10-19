from trader import Trader
from model import Model
import sys
import argparse

if __name__ == "__main__":
    #
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--training", default="training_data.csv", help="input training data file name")
    parser.add_argument("--testing", default="testing_data.csv", help="input testing data file name")
    parser.add_argument("--output", default="output.csv", help="output file name")
    args = parser.parse_args()

    #
    trader = Trader(args)
    trader.main()
    with open(args.output, 'w') as f:
        f.writelines(trader.OutputTxt)
        f.close()

