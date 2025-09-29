from quickhash import sha256_file
import pathlib, tempfile

def test_hash_roundtrip():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"hello")
        p = pathlib.Path(f.name)
    digest, total = sha256_file(p)
    assert total == 5
    assert len(digest) == 64
