import argparse, hashlib, pathlib, sys

def sha256_file(path: pathlib.Path, chunk_size=8192):
    h = hashlib.sha256()
    total = 0
    with path.open('rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk: break
            total += len(chunk)
            h.update(chunk)
    return h.hexdigest(), total

def main():
    p = argparse.ArgumentParser(description="Hash files with SHA256")
    p.add_argument("paths", nargs="+", help="file paths")
    args = p.parse_args()
    for pth in args.paths:
        pth = pathlib.Path(pth)
        if not pth.exists():
            print(f"Not found: {pth}", file=sys.stderr)
            continue
        digest, total = sha256_file(pth)
        print(f"{digest}  {pth}  ({total} bytes)")

if __name__ == "__main__":
    main()
