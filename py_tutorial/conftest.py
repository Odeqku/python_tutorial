#!/usr/bin/python3

import pytest

@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
	img = compute_expensive_image()
	fn = tmp_path_factory.mktmp("data") / "img.png"
	img.save(fn)
	return fn
