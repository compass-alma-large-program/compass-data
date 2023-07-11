# Data reduction scripts for IMAGER

This directory contains data reduction scripts for
[IMAGER](https://imager.oasu.u-bordeaux.fr), an interferometric
imaging package.

## Prerequisites

* IMAGER (>= 3.6.0)
* CASA (>= 6.2.0)

IMAGER is part of the Gildas suite. If you have a recent version of
Gildas installed on your machine, you probably have IMAGER installed
already.

## Running the scripts

### Getting the calibrated visibilities

The scripts expect to find the calibrated visibilities (in MS format),
into the `data/calibrated/ms` directory, at the root of this
repository. If you have cloned this repository on your computer, this
directory structure should have been created already.

These calibrated visibilities can be found on ERDA, under the
`COMPASS/CalibratedMS` directory. Download the MS file that
corresponds to the source and frequency setting that you want to
reduce, (e.g. `uid___A002_X101c3b2_Xbcf0.ms.split.cal.tar` for
BHR71-IRS1 setting A), and move it to `data/calibrated/ms`. Do not
untar the file (it will be untared on-the-fly by the export script).

### Converting the calibrated visibilities to UVFITS

IMAGER cannot work with visibilities in MS format, so they need to be
converted to UVFITS first. This is done with the CASA scripts
`X/export_XX.py`, where `X` is the name of source and `XX` is the
frequency setting (e.g. `bhr71/export_a.py`).

The script is run as follows:

```sh
cd datareduction/scripts/imager/bhr71
casa --nogui --log2term -c export_a.py
```

It will create one UVFITS file for each spectral windows,
e.g. `data/calibrated/uvfits/bhr71-a-spw25.uvfits`. It takes around 2
hours to run.

## Running the data reduction IMAGER script

The data reduction in IMAGER is done with the `X/redu_XX.ima` scripts,
where `X` is the name of source and `XX` is the frequency setting
(e.g. `bhr71/redu_a.ima`).

The script is run as follows:

```sh
cd datareduction/scripts/imager/bhr71
imager @ redu_a
```

It does the self-calibration, extracts the continuum and the lines,
and images the results. It creates four files: two UV tables in
compressed UVFITS format that contain the continuum and line
visibilities, respectively; and two images/cubes in compressed FITS
for the continuum image and line data cubes, respectively:

* `data/reduced/bhr71/bhr71-a-spw25-cont.uvfits.gz`
* `data/reduced/bhr71/bhr71-a-spw25-lines.uvfits.gz`
* `data/reduced/bhr71/bhr71-a-spw25-cont.fits.gz`
* `data/reduced/bhr71/bhr71-a-spw25-lines.fits.gz`

The script takes 1.2 hours to run on 36 core server.
