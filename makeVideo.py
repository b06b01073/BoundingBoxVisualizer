import os

from argparse import ArgumentParser
from VideoMaker import VideoMaker

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--image_dir', '-i', type=str)
    parser.add_argument('--label_dir', '-l', type=str)
    parser.add_argument('--save_dir', '-s', type=str)

    args = parser.parse_args()

    if not os.path.exists(args.image_dir):
        print(f'{args.image_dir} does not exist.')
        exit()

    if not os.path.exists(args.label_dir):
        print(f'{args.label_dir} does not exist.')

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)


    maker = VideoMaker()
    maker.make(args.image_dir, args.label_dir, args.save_dir)