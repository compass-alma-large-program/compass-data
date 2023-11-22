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

## Writing scripts for a new source or a new frequency setting

To develop reduction scripts for a new source or a new frequency
setting, follow the following steps:

### Initial setup

 1. Create a directory named `datareduction/imager/X/` where `X`
    is the name of the source, e.g. `b335`. This directory will
    contain the reduction export and reduction scripts for that
    source.

 2. Create an export script and a reduction script in that directory,
    using one of the scripts for BHR71 as a template:

    ```sh
    cp datareduction/imager/bhr71/redu_XX.ima datareduction/imager/X/
    cp datareduction/imager/bhr71/export_XX.ima datareduction/imager/X/
    ```

    where `XX` is the frequency setting (e.g. `f`)

 3. Create a directory named `data/reduced/X` where `X`
    is the name of the source, e.g. `b335`. This directory will
    contain the reduced data.

### Writing an export script

Writing an export script is fairly straightforward: simply edit the
last line of script:

```py
export(uid = "uid___A002_X1036d05_X4eca", field = "B335", basename ="b335-f")
```

to set the three parameters of the `export` function:

* `uid`: The UID of the dataset. This is the name of the MS file
  (without the `.ms.split.cal.tar` file extension) that contains the
  calibrated visibilities for that source/setting.

* `field`: The name of the field in the MS file. This is typically
  the name of the source in capital letters.
  
* `basename`: The name of the output UVFITS file without the `uvfits` file
   extension, and not leading path. By convention, it should be the
   name of the source name followed by a `-` and the name of the
   setting.

### Writing a reduction script

Writing a reduction script is a bit more complex, because the script
parameters may need to be adapted to each source and frequency
setting. These parameters are defined in a data structure name
`redu%`, which is initialized at the beginning of the script:

```f90
@ ../lib/redu init
```

Two parameters are mandatory: the basename of the UVFITS file and the
name of the frequency setting. There as set as follows:

```f90
let redu%basename bhr71
let redu%setting a
```

Other parameters are optional and have reasonable default values (but they
may be also set if needed). Here is a full list:

* `redu%spws` An array containing the spectral windows to
  reduce. Default is `25 27 29 31` (i.e. all COMPASS windows). This
  may be set to a single number for debugging purposes, e.g. with

 ```f90
 let redu%spws 25 /resize
 ```

 Note the `/resize` option to adapt the size of the array.

* `redu%uv_preview_clip`: The clipping value (in sigma) for the
  line-free channel identification. It corresponds to the value of
  the `clip` parameter of the `uv_preview` command. Default is `3`.
  
* `redu%map_robust`: Robust weighting factor. Default is `1`. It
   corresponds to the `map_robust` parameter of the `uv_map` command
   in IMAGER.
  
* `redu%map_size`: Size of the output maps, in pixels. Default is `0
  0`, which means that it is automatically set. It corresponds to the
  `map_size` parameter of the `uv_map` command.

* `redu%map_cell`: Pixel size, in arcsecs. Default is `0 0`, which
   means that it is automatically set. It corresponds to the
   `map_cell` parameter of the `uv_map` command.

* `redu%primary_truncate`: Truncation level of the primary beam, in
  fraction of the peak. Default is `0.2`. It corresponds to the
  `truncate` parameter of the `primary` command.

* `redu%extract_continuum`: A boolean to toggle the continuum
  extraction.  If `.true.`, the script will produce UV tables and
  images for the continuum. If `.false.`, only UV tables and cubes for
  the line emission will be created. Default is `.true.`

* `redu%self_calibrate`: A boolean to toggle the self-calibration. If
   `.true.` self calibration will be performed. Default is `.true.`

* `redu%delete_intermediate_files`: A boolean to toggle the deletion
   of intermediate files at the end. If `.true.` only the final
   products (UV tables and cubes/images) will be kept. Default is
   `.true.`

* `redu%interactive`:  A boolean to toggle the interactive mode.
  If `.true.` the script will pause at each reduction step to give a
  chance to the user to check the data (see below). Default is
  `.false.`
  
* `redu%uv_preview_clip`: The clipping value (in sigma) for the
  line-free channel identification. It corresponds to the value of
  the `clip` parameter of the `uv_preview` command. Default is `3`.
  
For developing a script, `redu%interactive` is typically set to
`.true`. This will pause the script at each step of the data
reduction, to allow to check the data, and to adapt the reduction if
needed (e.g. the clipping value above). In production, this should be
set to `.false.`.
