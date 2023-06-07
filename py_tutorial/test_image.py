#!/usr/bin/python3

import pytest

def test_histogram(image_file):
    img = load_image(image_file)
	# compute and test histogram
