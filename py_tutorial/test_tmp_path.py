#!/usr/bin/python3

CONTENT = "content"

def test_create_file(tmp_path):
	d = tmp_path / "sub"
	d.mkdir()
	p = d / "hello.txt"
	p.write_text(CONTENT)

	assert p.read_text() == CONTENT
	assert len(list(tmp_path.iterdir())) == 1
	assert 0


#def test_needsfiles(tmp_path):
	#print(tmp_path)
	#assert 0
