import json
from pathlib import Path
import tempfile
import unittest

from install import install_cccl

ROOT = Path(__file__).resolve().parents[1]


class CCCLExtractionTest(unittest.TestCase):
    def test_extracts_coherent_family_and_licenses(self):
        version = json.loads((ROOT / "version_table.json").read_text())["cccl"]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "cccl"
            install_cccl(str(ROOT / "cccl"), str(output), version)
            for name in ("libcudacxx/include/cuda/fpmp", "cub/cub/cub.cuh", "thrust/thrust/version.h", "LICENSE", "cccl-version.json"):
                self.assertEqual((output / name).read_bytes(), (ROOT / "cccl" / name).read_bytes())
            self.assertEqual((output / "__cfd_externals_version").read_text(), version)
            self.assertFalse((output / ".git").exists())
            self.assertFalse((output / "benchmarks").exists())


if __name__ == "__main__":
    unittest.main()
