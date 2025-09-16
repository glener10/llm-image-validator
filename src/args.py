import argparse


def get_args():
    parser = argparse.ArgumentParser(description="image validator")
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="path to the input image file",
    )
    parser.add_argument(
        "-n",
        "--name",
        required=False,
        default="sequence diagram",
        help="name of the type of image",
    )
    args = parser.parse_args()
    return args
