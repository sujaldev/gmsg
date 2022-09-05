import os
import sys
import argparse
from mathematical_backend import ease, ease_in, ease_out

parser = argparse.ArgumentParser(
    prog="gmsg", description="Utility to create slideshows for GitHub markdown."
)

parser.add_argument(
    "-i", "--input", required=True,
    help="A directory containing all the input images and nothing else."
)
parser.add_argument("-f", "--fps", default=30, help="Frames per second")
parser.add_argument("-d", "--delay", default=3.0, help="How long for each picture to stay on screen")
parser.add_argument("-t", "--transition-duration", default=1, help="Duration for transition animation")
parser.add_argument("-p", "--padding", default=50, help="Distance between sliding images")
parser.add_argument("-b", "--bezier-curve", default="ease", help="Choose from: [ease, ease-in, ease-out]")


def get_args():
    args = parser.parse_args(sys.argv[1:])

    args.input = [(str(args.input).removesuffix("/") + "/" + filename) for filename in os.listdir(str(args.input))]

    try:
        args.fps = int(args.fps)
    except ValueError:
        raise Exception("FPS must be an integer")

    try:
        args.delay = float(args.delay)
    except ValueError:
        raise Exception("Delay must be an integer or a float")

    try:
        args.transition_duration = int(args.transition_duration)
    except ValueError:
        raise Exception("Transition Duration must be an integer")

    try:
        args.padding = int(args.padding)
    except ValueError:
        raise Exception("Padding must be an integer")

    if args.bezier_curve not in ["ease", "ease-in", "ease-out"]:
        raise Exception("Bezier Curve must be one of: [ease, ease-in , ease-out]")
    else:
        if args.bezier_curve == "ease":
            args.bezier_curve = ease
        elif args.bezier_curve == "ease-in":
            args.bezier_curve = ease_in
        elif args.bezier_curve == "ease-out":
            args.bezier_curve = ease_out

    return args
