#!/bin/bash
git -C argparse fetch --depth=1 origin tag v3.2
git -C argparse checkout v3.2
git -C fmt fetch --depth=1 origin tag 11.1.4
git -C fmt checkout 11.1.4
git -C boost fetch --depth=1 origin tag boost-1.87.0
git -C boost checkout boost-1.87.0
git -C nanoflann fetch --depth=1 origin tag v1.7.1
git -C nanoflann checkout v1.7.1
git -C nlohmann fetch --depth=1 origin tag v3.11.3
git -C nlohmann checkout v3.11.3