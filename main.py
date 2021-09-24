# Run with eg:
# python main.py --coords 1,2 3,4 5,6 --rounds 2
# python .\main.py --coords 1,2 3,4 5,6 --rounds 2

import argparse
from Abgaben.* import c

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    def coords(s):
        try:
            x, y= map(int, s.split(','))
            return x, y
        except:
            raise argparse.ArgumentTypeError("Coordinates must be x,y")

    parser.add_argument('--coords', help="Coordinates", dest="coords", type=coords, nargs='+')
    parser.add_argument('--rounds', type=int, dest="rounds")
    args = parser.parse_args()
    tuples = c(args.coords, args.rounds)
    print(tuples) #[(0,0), (1,1), (2,2)]

if __name__ == "__main__":
    main()