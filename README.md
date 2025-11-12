# cfd_externals_headeronlys

The project [DNDSR](https://github.com/harryzhou2000/DNDSR) relies on several splendid header-only or CMake-nested libraries.

In other words, these libraries are used as **source code** in [DNDSR](https://github.com/harryzhou2000/DNDSR).

To ease the process of setting up these dependencies, git submodule would be a great tool to directly nest the source code into DNDSR.

However, only shallow cloning all the necessary repos would cost 2GB space and 100k+ files, so this repo provides a script to only extract the source code we need.

## Boost

We only use the header-only part for now.

DNDSR is not planning to heavily rely on Boost in the future.

## Licenses

| Project             | License |
| ------------------- | ------- |
| CGAL                | GPLv3   |
| argparse            | MIT     |
| boost               | BSL-1.0 |
| cppcodec            | MIT     |
| cpptrace            | MIT     |
| doxygen-awesome-css | MIT     |
| eigen               | MPL 2.0 |
| exprtk              | MIT     |
| fmt                 | MIT     |
| nanoflann           | BSD-2   |
| nlohmann            | MIT     |
| pybind11            | BSD-3   |
| pybind11_json       | BSD-3   |
