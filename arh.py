import tempfile
import zipfile
import os
import shutil
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="name of zip file", type=str)
args = parser.parse_args()
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    filename=f"{args.n}.log")


with tempfile.TemporaryDirectory() as tmpdir:
    with zipfile.ZipFile(f"{args.n}.zip", "r") as zf:
        zf.extractall(path=tmpdir)
        logging.debug(f"{args.n}.zip extracted in tempdir: {tmpdir}")

    try:
        for dirpath, dirnames, files in os.walk(tmpdir):
            if "__init__.py" not in files:
                shutil.rmtree(dirpath)
                logging.debug(f"Have been removed catalog: {dirpath}")
    except OSError as e:
        logging.debug(f"Error: {dirpath} : {e.strerror}")

    with zipfile.ZipFile(f"{args.n}_new.zip", "w") as zf:
        for dirpath, dirnames, files in os.walk(tmpdir):
            for filename in files:
                filepath = os.path.join(dirpath, filename)
                path = filepath.replace(tmpdir, "", 1)
                zf.write(filepath, path)
    logging.debug(f"{args.n}_new.zip have been created")
    logging.debug(f"{tmpdir} have been removed")
