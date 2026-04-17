# AGENTS.md

Dependency extraction repo for [DNDSR](https://github.com/harryzhou2000/DNDSR). Extracts header-only C++ libraries from git submodules to avoid 2GB+ shallow clones.

## Architecture

- **14 git submodules**: third-party C++ libraries (argparse, boost, CGAL, doctest, eigen, fmt, nlohmann json, pybind11, etc.)
- **version_table.json**: pins each submodule to a tag or commit hash
- **checkout.py**: fetches pinned versions (depth=1) into submodule dirs
- **install.py**: extracts headers/source to `install/<module>/` using per-module installer functions

Submodules are **not** checked in with code. They exist as empty dirs until `checkout.py` runs.

## Workflow

### Setup and extract headers
```bash
git submodule update --init --recursive --depth=1
python checkout.py  # fetches exact versions from version_table.json
python install.py   # copies headers to install/
```

### Update a dependency version
1. Edit `version_table.json` (use `tag:vX.Y.Z` format for tags)
2. Run `python checkout.py` to fetch new version
3. Run `python install.py` to extract updated headers
4. Commit changed files

### Version format in version_table.json
- Tags: `"tag:v3.2"` or `"tag:boost-1.87.0"`
- Commit hashes: `"a4b17d543f072d2e3ba564e4bc5c3a0d2b05c338"` (exprtk uses this)

## Per-module install functions

Each library has a custom installer in `install.py` (e.g., `install_argparse`, `install_eigen`). Some copy full repos (`install_full_repo`), others extract specific subdirs:

- **boost**: walks `libs/*/include/boost` and merges headers
- **CGAL**: finds all `include/CGAL` dirs recursively
- **doctest**: copies `doctest/` subdir (contains `doctest.h` and extensions)
- **eigen**: copies `Eigen/`, `unsupported/`, license files
- **argparse, nanoflann, nlohmann**: copy `include/` trees
- **cpptrace, doxygen-awesome-css, exprtk, fmt, pybind11, pybind11_json**: full repo copy

All installers write `__cfd_externals_version` file to track installed version.

## CI release

`.github/workflows/release.yml` triggers on `v*` tags:
1. Shallow clone submodules
2. Run `install.py`
3. Package `install/` as `.tar.gz` and `.zip`
4. Create draft GitHub release with artifacts

## Gotchas

- **Submodule dirs are empty** until `checkout.py` runs
- **checkout.py must run before install.py** (hard dependency)
- **Don't commit submodule content** (repo purpose is to extract, not vendor)
- **version_table.json is the source of truth** for dependency versions
- **exprtk has no tagged releases**, pinned to commit hash
