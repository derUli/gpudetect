#!/usr/bin/env python3
""" Example script """

from . import gpudetect


def main():
    """ Print all gpus """
    for gpu in gpudetect.detect_gpus():
        print(gpu)


if __name__ == "__main__":
    main()
