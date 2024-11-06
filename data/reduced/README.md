# Reduced data

This directory contains reduced data for the COMPASS large
program. The reduction was done with IMAGER, using the scripts in the
[COMPASS
repository](https://github.com/adeleplunkett/compass/tree/imager).

Data for each source are stored in a separate directory, e.g. `bhr71`.

Within each source directory, the continuum images and line datacubes
are stored in the `cubes/` sub-directory. There are two FITS files for
each frequency setting (1-9) and each spectral windows (spw25, spw27,
spw29 and spw31): one image for the continuum, and one cube for the
lines, e.g.:

- `bhr71-set1-spw25-cont.fits`
- `bhr71-set1-spw25-lines.fits`

The UV tables are stored in the `uvtables` sub-directory. Likewise
there are two UVFITS files for each frequency setting and spectral
window, e.g.:

- `bhr71-set1-spw25-cont.uvfits`
- `bhr71-set1-spw25-lines.uvfits`

See the `CHANGELOG.md` file in each source directory for a change log.

