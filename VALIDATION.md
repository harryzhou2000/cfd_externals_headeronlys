# CCCL bundle validation (2026-11-17)

- The complete extraction script succeeds, including all existing modules.
- The focused extraction test checks libcu++ `cuda/fpmp`, CUB, Thrust, source
  version metadata and licenses against the same pinned source; no Git or
  benchmark directories enter the extracted CCCL package.
- A CUDA consumer including `cuda/fpmp`, `cuda/std/array`, CUB and Thrust
  compiles for SM80 with both CUDA 12.6 and CUDA 13.2, using GCC 12 and all
  three packaged include roots. It is a compile check, not a numerical
  float-float or GPU performance qualification.
- Installed CCCL headers occupy about 28 MB. No CCCL library compilation,
  runtime GPU use or DNDSR source changes are needed for extraction.
