#!/usr/bin/env python3

from . import gpudetect


def main():
     for gpu in gpudetect.detect_gpus():
          print(gpu)

if __name__ == "__main__":
    main()