# cfd_externals_headeronlys

The project [DNDSR](https://github.com/harryzhou2000/DNDSR) relies on several splendid header-only or CMake-nested libraries.

In other words, these libraries are used as **source code** in [DNDSR](https://github.com/harryzhou2000/DNDSR).

To ease the process of setting up these dependencies, git submodule would be a great tool to directly nest the source code into DNDSR.

However, only shallow cloning all the necessary repos would cost 2GB space and 100k+ files, so this repo provides a script to only extract the source code we need.

## Boost

We only use the header-only part for now.

DNDSR is not planning to heavily rely on Boost in the future.

## CCCL (optional CUDA consumers)

The bundle includes a pinned CCCL development snapshot with `cuda/fpmp` for
experimental float-float arithmetic. It is source headers, not a compiled CUDA
library, and does not make CPU consumers require a CUDA installation. The exact
commit is in `version_table.json` and `install/cccl/__cfd_externals_version`.

Select all three include roots from this same installation, before toolkit
CCCL paths; do not mix header families:

```text
cccl/libcudacxx/include
cccl/cub
cccl/thrust
```

This extraction supports direct header consumption. It does not include the
full CCCL build, tests, benchmarks, or its CMake package installation. CUDA
12.6/13.2 consumer compatibility remains subject to each application's checks.

## Licenses

| Project             | License |
| ------------------- | ------- |
| CGAL                | GPLv3   |
| CCCL                | Apache-2.0 WITH LLVM-exception (see packaged licenses) |
| argparse            | MIT     |
| boost               | BSL-1.0 |
| cppcodec            | MIT     |
| cpptrace            | MIT     |
| doctest             | MIT     |
| doxygen-awesome-css | MIT     |
| eigen               | MPL 2.0 |
| exprtk              | MIT     |
| fmt                 | MIT     |
| nanoflann           | BSD-2   |
| nlohmann            | MIT     |
| pybind11            | BSD-3   |
| pybind11_json       | BSD-3   |
| spdlog              | MIT     |
