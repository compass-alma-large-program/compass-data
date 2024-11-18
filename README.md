# COMPASS data reduction

This repository contains the data reduction scripts for
[COMPASS](https://erda.ku.dk/vgrid/COMPASS/) (Complex Organic
Molecules in Protostars with ALMA Spectral Surveys), an [ALMA Large
Program](https://almascience.eso.org/alma-data/lp) to systematically
characterize the presence of complex organic molecules of a sample of
11 deeply embedded low-mass protostars through unbiased spectral
surveys.

The data reduction is done with
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
BHR71-IRS1 setting 1), and move it to `data/calibrated/ms`. Do not
untar the file (it will be untared on-the-fly by the export script).

### Converting the calibrated visibilities to UVFITS

IMAGER cannot work with visibilities in MS format, so they need to be
converted to UVFITS first. This is done with the CASA scripts
`X/export_setXX.py`, where `X` is the name of source and `XX` is the
frequency setting (e.g. [`bhr71/export_set1.py`](scripts/bhr71/export_set1.py)).

The script is run as follows:

```sh
cd scripts/bhr71
casa --nogui --log2term -c export_set1.py
```

It will create one UVFITS file for each spectral windows,
e.g. `data/calibrated/uvfits/bhr71-set1-spw25.uvfits`. It takes around 2
hours to run.

### Running the data reduction script

The data reduction in IMAGER is done with the `X/redu_setXX.ima` scripts,
where `X` is the name of source and `XX` is the frequency setting
(e.g. [`bhr71/redu_set1.ima`](scripts/bhr71/redu_set1.ima)).

The script is run as follows:

```sh
cd scripts/bhr71
imager @ redu_set1
```

It does the self-calibration, extracts the continuum and the lines,
and images the results. It creates four files: two UV tables in
UVFITS format that contain the continuum and line
visibilities, respectively; and two images/cubes in FITS format
for the continuum image and line data cubes, respectively:

* `data/reduced/bhr71/uvtables/bhr71-set1-spw25-cont.uvfits`
* `data/reduced/bhr71/uvtables/bhr71-set1-spw25-lines.uvfits`
* `data/reduced/bhr71/cubes/bhr71-set1-spw25-cont.fits`
* `data/reduced/bhr71/cubes/bhr71-set1-spw25-lines.fits`

The script takes 1.2 hours to run on 36 core server.

## Modifying the scripts

> [!NOTE]
> The scripts in this directory should work without any
> modifications. Modifications the scripts are only needed to fine-tune
> the reduction.

### Export script

Export scripts are fairly straightforward. They usually contains only
one call of the `export()` function:

```py
export(uid = "uid___A002_X1036d05_X4eca", field = "B335", basename ="b335-set6")
```

This function is defined in the [`export.py`](scripts/common/export.py)
module. It has three parameters:

* `uid`: The UID of the dataset. This is the name of the MS file
  (without the `.ms.split.cal.tar` file extension) that contains the
  calibrated visibilities for that source/setting. It also accepts a
  list of UIDs, if the observations were obtained in several execution
  blocks. If a list is given, these UIDs are merged before the export.

* `field`: The name of the field in the MS file. This is typically
  the name of the source in capital letters.
  
* `basename`: The name of the output UVFITS file without the `uvfits` file
   extension, and not leading path. By convention, it should be the
   name of the source name followed by a `-set` and the setting number.

### Reduction script

Reductions scripts are more complex, because they have several
parameters that may need to be adapted to each source and frequency
setting.

All the data reduction steps are implemented in a single IMAGER
procedure `@ redu`, which is defined in
[`redu.ima`](scripts/common/redu.ima).


This procedure has three possible arguments: `init`, `run` and
`clean`, which are use to set the reduction parameter, to run the
reduction, and to clean the variables and intermediate files,
respectively.

#### Setting the reduction parameters

The reduction parameter are defined in a data structure named
`redu%`, which needs to be initialized at the beginning of the script:

```f90
@ ../common/redu init
```

Two parameters are mandatory: the basename of the UVFITS file and the
the frequency setting number. There as set as follows:

```f90
let redu%basename bhr71
let redu%setting 1
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

* `redu%drop_edge_channels`: The number of channels on each edges of
  the spectral band that will be dropped. For example, if it is set to
  5, the 5 first channels and the last 5 channels will be
  dropped. Default is `5`.

* `redu%uv_preview_clip`: The clipping value (in sigma) for the
  line-free channel identification. It corresponds to the value of
  the `clip` parameter of the `uv_preview` command. Default is `3`.
  
* `redu%uv_preview_smooth`: The number of spectral smoothings for the
  line-free channel identification. It corresponds to the value of
  the `smooth` parameter of the `uv_preview` command. Default is `3`.

* `redu%uv_preview_taper`: The number of scale sizes for the
  line-free channel identification. It corresponds to the value of
  the `taper` parameter of the `uv_preview` command. Default is `3`.

* `redu%map_robust`: Robust weighting factor. Default is `1`. It
   corresponds to the `map_robust` parameter of the `uv_map` command
   in IMAGER.
  
* `redu%map_size`: Size of the output maps, in pixels. Default is `0
  0`, which means that it is automatically set. It corresponds to the
  `map_size` parameter of the `uv_map` command.

* `redu%map_cell`: Pixel size, in arcsecs. Default is `0 0`, which
   means that it is automatically set. It corresponds to the
   `map_cell` parameter of the `uv_map` command.

* `redu%uv_restore`: A boolean to toggle the "restore" of the
  clean image/cubes from UV data and clean components. If `.true.`,
  the restore will be performed. Default is `.true.`.

* `redu%jvm_correction`: A boolean to toggle the so-called JvM
  correction during the restore. If `.true.`, the correction will be
  applied. Default is `.false.`.

* `redu%primary_beam_correction`: A boolean to toggle the primary beam
  correction. If `.true.`, primary beam correction will be
  applied. Default is `.true.`.

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
  
* `redu%subdir`: Sub-directory under `data/reduced/` in which the
  reduced data will be stored. It is useful when running tests to
  avoid over writing the original data. Default is `""` (no
  sub-directory).

> [!TIP]
> The parameters which are common to all frequency settings of a given
> source (e.g. the image size) can be defined in the
> [`set_redu_params.ima`](scripts/bhr71/set_redu_params.ima)  file in each source directory.

#### Starting the data reduction

The data reduction itself is started with the `run` argument:

```f90
@ ../common/redu run
```

> [!TIP]
> When developing a reduction script, it is recommenced to set
> `redu%interactive` to `.true`. This will pause the script at each
> step of the data reduction, to allow to check the data, and to adapt
> the reduction if needed (e.g. the clipping value above).

#### Cleaning the intermediate files and variables

At the end of the reduction, the intermediate files and variables can
be deleted with the `clean` argument:

```f90
@ ../common/redu clean
```

This avoids side effects when running the reduction script several
times.
