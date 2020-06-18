ADAblock for ImageJ
--------------------
***Automated Defect Analysis of Block Copolymers***


*Jeffrey N. Muprhy*
[@MurphysLab](https://twitter.com/MurphysLab)

---------------------

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.19644.svg)](http://dx.doi.org/10.5281/zenodo.19644)

---------------------

\* *Modified by Z. Sun in May 2020*

## About

Code written for the analysis of defects in line patterns produced from the domains of block copolymer thin films.
Sample SEM images can be obtained from [https://hdl.handle.net/10402/era.41438](https://hdl.handle.net/10402/era.41438).

The code is made available for use and modification under the "[MIT License](https://opensource.org/licenses/MIT)".

If you have any questions, or wish to contribute to the code, please contact the author.

## Bug fixes and improvements

Here is the list of commits and their corresponding issues/enhancement <a href="#n1" id="n1r"><sup>[1]</sup></a> since [MurphysLab/ADAblock@e6df7b0](https://github.com/MurphysLab/ADAblock/tree/e6df7b027637d15a99530148dc54e8d3c5d89452). **The updates are compatible for all versions greater than 1.49o (either <1.52 or >=1.52)**

![](https://img.shields.io/badge/Bug-P1-important?style=plastic) If you use ImageJ **core** version <a href="#n2" id="n2r"><sup>[2]</sup></a> >= 1.52, you would meet the following error message: `'[' or '.' expected` <a href="#n3" id="n3r"><sup>[3]</sup></a>
* Mentioned in [MurphysLab/ADAblock#2](https://github.com/MurphysLab/ADAblock/issues/2)
* Solved in [Z-H-Sun/ADAblock@4ffb037](https://github.com/Z-H-Sun/ADAblock/commit/4ffb037954a2afd5f8b2c84ffee2b1b02ae065fc)

![](https://img.shields.io/badge/Bug-P1-important?style=plastic) **(I).** The macro lacked support for non-8-bit images, and you would be prompted `Not a viable image!` <a href="#n4" id="n4r"><sup>[4]</sup></a>; **(II).** If you use ImageJ 1.53 downloaded from the official website, you would meet the following error message: `Unrecognized command: "Auto Local Threshold"` though the plugin has been built-in <a href="#n5" id="n5r"><sup>[5]</sup></a>
* Solved in [Z-H-Sun/ADAblock@b560cc6](https://github.com/Z-H-Sun/ADAblock/commit/b560cc6f2aa282fdd6267ea4fa5eae72d680bdf1)

![](https://img.shields.io/badge/Bug-P1-important?style=plastic) If you use ImageJ >= 1.52, the skeleton would be wrongly dyed, leading to wrong results of Herman's OP as well as the correlation length <a href="#n6" id="n6r"><sup>[6]</sup></a>
* Solved in [Z-H-Sun/ADAblock@549b89f](https://github.com/Z-H-Sun/ADAblock/commit/549b89fba6895f4e01d5b46fe0bc94641e9b9f28)
<p align="center"><img src="/demo/positive_skeleton_correlation.png" width="90%" height="90%"></p>

![](https://img.shields.io/badge/Bug-P1-important?style=plastic) If you use ImageJ >= 1.52, the domain map would not display correctly <a href="#n7" id="n7r"><sup>[7]</sup></a>
* Solved in [Z-H-Sun/ADAblock@edfe93e](https://github.com/Z-H-Sun/ADAblock/commit/edfe93e118653aca4dc6ebe76041937cd7b13741)
<p align="center"><img src="/demo/DomainMap.png" width="90%" height="90%"></p>

![](https://img.shields.io/badge/Bug-P0-critical?style=plastic) The algorithm of linear regression for calculation of correlation length was wrong. If your data fit well with the exponential decay model, it might induce very little error and might be hardly noticeable; nevertheless, it was still a critical bug and could lead to large deviations in some cases <a href="#n8" id="n8r"><sup>[8]</sup></a>
* Solved in [Z-H-Sun/ADAblock@0b1185e](https://github.com/Z-H-Sun/ADAblock/commit/0b1185e4f0ad3e06167bf8b8e13cb01f22888380)

![](https://img.shields.io/badge/Bug-P0-critical?style=plastic) The result presentation of LER and LWR was confusing: Some were misclassified <a href="#n9" id="n9r"><sup>[9]</sup></a>, some were clearly wrong <a href="#n10" id="n10r"><sup>[10]</sup></a>, and most of them were shown in pixels, but we care more about results in nanometers. In addition, the code did not produce length-averaged LWR results
* Solved in [Z-H-Sun/ADAblock@cd2fada](https://github.com/Z-H-Sun/ADAblock/commit/cd2fada080cbc091843669f9070e463cb56479f6)
<p align="center"><img src="/demo/LER_LWR_results.png" width="90%" height="90%"></p>

![](https://img.shields.io/badge/Bug-P2-yellow?style=plastic) **(I).** The process of drawing defect features was too slow and error-prone in non-batch mode <a href="#n11" id="n11r"><sup>[11]</sup></a>; **(II).** It is desirable to paint “terminals” at edges as paler colors, since they should not be counted as “defects,” but rather cut-off of “field of vision,” as in `image_regions_defects.png`. However, this feature was not implemented for other figures, *i.e.* `image_regions_defects.png`, `image_figure_4_b.png`, and `image_figure_4_c.png`; **(III).** There was no option to opt out of drawing certain pictures that might be unnecessary for batch analysis
* Solved in [Z-H-Sun/ADAblock@8f65309](https://github.com/Z-H-Sun/ADAblock/commit/8f653095ca70a0f8375a1df51ee0790453c8162b)
<p align="center"><img src="/demo/image_figure_4_b.png" width="90%" height="90%"></p>

![](https://img.shields.io/badge/Enhancement-P4-informational?style=plastic) The preferences set in the dialogs would not be saved for next start-up, which was inconvenient.
* Starting from [Z-H-Sun/ADAblock@7a4dd79](https://github.com/Z-H-Sun/ADAblock/commit/7a4dd799a312c5ef1e70f0b143d844e0e6f56b96), you can change the default settings in the dialogs by editing the first few lines of [ADAblock.ijm](/ADAblock.ijm)

![](https://img.shields.io/badge/Enhancement-P4-informational?style=plastic) I have been using Zeiss SEM to capture images, so I added one more option to extract scalebar information for Zeiss SEM in addition to the original NINT one
* Starting from [Z-H-Sun/ADAblock@73d5f8c](https://github.com/Z-H-Sun/ADAblock/commit/73d5f8c341b3ca70921078bd4c9281187f3fbed0), resolution information can be automatically extracted for Zeiss SEM, but you have to make sure the input image must be 1024x768

![](https://img.shields.io/badge/Bug-P2-yellow?style=plastic) **(I).** The correlation lengths were shown in pixels, but we care more about results in nanometers; **(II).** Very often, the unusual defects (4-way or 5-way junctions) identified by the macro were actually artefacts due to wrongly converted skeleton graph.
* Starting from [Z-H-Sun/ADAblock@f2e8d4d
](https://github.com/Z-H-Sun/ADAblock/commit/f2e8d4da94b2208a35f9ac522d3352d9f9670fec), correlation lengths will be shown in nanometers rather than pixels, and defect densities without taking into account unusual defects will be given at the end of the output file in addition to the conventional way of calculation.

---------------------

\#|Notes
---|---
[1]|<b id="n1">Bugs by Priority:</b><br>**P0**: They lead to confusing results or even wrong conclusions; **P1**: They lead to wrong results if you use ImageJ **core** versions <a href="#n2"><sup>[2]</sup></a> >= 1.52, though you can avoid them by downgrading to lower versions as suggested in [MurphysLab/ADAblock#2](https://github.com/MurphysLab/ADAblock/issues/2); **P2**: Known bugs that are minor; **P4**: Enhancement issues. [⏎](#n1r)
[2]|<span id="n2">The Version 2 of ImageJ/Fiji can be viewed as a wrapper of its version one counterpart--although the *apparent* version is “v2.0.0,” the **core** version is still 1.4x or 1.5x. For example, core version 1.52 corresponds to apparent version around 2.0.0 rc50; the newest release, Fiji v2.0.0 rc69 uses v1.52p core; the latest ImageJ core version is 1.53a.</span> [⏎](#n2r)
[3]|<span id="n3">Higher versions of ImageJ does not allow comparison between an array (ArrayB / ArrayC) and a number (1). This bug only affects the `arraySumP3` function, so the code has been modified accordingly.</span> [⏎](#n3r)
[4]|<span id="n4">The exclusion of RGB images of the original macro is unnecessary, since even colored 8-bit images can also be processed after conversion to 8-bit grayscale.</span> [⏎](#n4r)
[5]|<span id="n5">That is because the plugin has been renamed as `Auto Local Threshold...` (with ellipsis dots). The code has been modified to be compatible to both nomenclatures.</span> [⏎](#n5r)
[6]|<span id="n6">The figure, `positive_skeleton_correlation` (see the figure above), should be correctly dyed prior to correlation analysis. For ImageJ core version >= 1.52, calling `setForegroundColor` after `setColor` does not take effect, which will cause flood-filling with the color previously set by `setColor` rather than that set by `setForegroundColor` and cause bugs. One solution is to call `setForegroundColor` twice which will then override `setColor`, but finally I decided to replace every `setForegroundIndex` in the macro with `setColor` instead, because for one, this will also do the job correctly; for another, it is said to perform faster than the other according to the official documentation. </span> [⏎](#n6r)
[7]|<span id="n7">For ImageJ core version >= 1.52d, the program will not automatically set the minimum and maximum pixel values after `changeValues` is called, unless you manually open the “Brightness/Contrast” window. In addition, there are pixels whose values are `NaN`, which should also be removed. In this regard, `setMinAndMax` is called subsequently to solve the issue perfectly. </span> [⏎](#n7r)
[8]|<span id="n8"> There are plus signs missing in [Line 4101-4103 of the original code](https://github.com/MurphysLab/ADAblock/blob/e6df7b027637d15a99530148dc54e8d3c5d89452/ADAblock.ijm#L4101-L4103), *i.e.* they should be cumulation (+=) rather than assignment (=). As a result, the wrongly fitted slope, ![k={(xy)}_{\rm{last}}/x^2_{\rm{last}](https://render.githubusercontent.com/render/math?math=k={(xy)}_{\rm{last}}/x^2_{\rm{last}}), just used two points--the original point and the last data point. Although the value will be around the true value if your data fit well with the exponential decay model, the true equation should be ![k=\frac{\overline{xy}}{\overline{x^2}}](https://render.githubusercontent.com/render/math?math=k=\frac{\overline{xy}}{\overline{x^2}}). Moreover, the calculation for *R*<sup>2</sup> is also erroneous: Instead of ![r=\frac{\overline{xy}}{\sqrt{\overline{x^2}\ \overline{y^2}}}](https://render.githubusercontent.com/render/math?math=r=\frac{\overline{xy}}{\sqrt{\overline{x^2}\%20\overline{y^2}}}), it should be ![r=\frac{\overline{xy}-\bar x\bar y}{\sqrt{\left(\overline{x^2}-\bar x^2\right)\left(\overline{y^2}-\bar y^2\right)}}](https://render.githubusercontent.com/render/math?math=r=\frac{\overline{xy}-\bar%20x\bar%20y}{\sqrt{\left(\overline{x^2}-\bar%20x^2\right)\left(\overline{y^2}-\bar%20y^2\right)}})</span> [⏎](#n8r)
[9]|<span id="n9">Note that `P` and `N` here in LER and LWR analysis do not refer to positive or negative pattern features as before. According to the most recent code as of [MurphysLab/ADAblock@e6df7b0](https://github.com/MurphysLab/ADAblock/tree/e6df7b027637d15a99530148dc54e8d3c5d89452), it seems the new classification function has not been completed yet, so all `V` (for “valid”) data will go to the `N` (for “negative”) category while the `P` (for “positive”) one remains empty (that's why you see Infinity's and NaN's in the figure above). Previously, according to the comments, it seems the author wanted to classify them according to the sign of the cross product, ![\vec{v}\cross\vec{t}](https://render.githubusercontent.com/render/math?math=\vec{v}\times\vec{t}) (please see Figure 10B of the original article for definitions). At first glance, I thought the author desired to distinguish one side of the edges from the other; however, I found the sign of the slope of vector ***t*** messed things up: As a result, I observed that a point would go to the `P` category if it is on the right-hand side and the slope is negative, or if it is on the left-hand side and the slope is positive. I think this old classification, too, is of little physical meaning, so finally I instead combined these two categories into one to avoid confusion. </span> [⏎](#n9r)
[10]|<span id="n10">There are plus signs missing in [Line 4975 of the original code](https://github.com/MurphysLab/ADAblock/blob/e6df7b027637d15a99530148dc54e8d3c5d89452/ADAblock.ijm#L4975), *i.e.* they should be cumulation (+=) rather than assignment (=). As a result, the obtained mean widths were apparently too small to seem correct. </span> [⏎](#n10r)
[11]|<span id="n11">The original method was to paint R, G, and B channels separately. This requires frequently switching among image windows, which is slow and may cause bugs (see the figure above) or will even save the wrong image. The code was re-written to avoid that. </span> [⏎](#n11r)

## Instructions

A walk-through of the ImageJ code as run is available in the supporting information section of our 2015 PLoS ONE paper, *"Automated Defect and Correlation Length Analysis of Block Copolymer Thin Film Nanopatterns"* which is freely available at DOI: [10.1371/journal.pone.0133088](https://doi.org/10.1371/journal.pone.0133088). The walk-through is also available as a Google Document at: [https://goo.gl/Gncg2Y](https://goo.gl/Gncg2Y). 

### Changes
* The latest ImageJ with **core** version <a href="#n2"><sup>[2]</sup></a> 1.53a can be downloaded [here if you have Java environment installed](http://wsr.imagej.net/distros/cross-platform/ij153.zip), or [visit the official website](https://imagej.net/download.html) for more options. **Nevertheless, the updates above also works for older versions of ImageJ** (at least >=1.49o) in case you do not want to upgrade your existing one
* For these high versions, the `Auto Local Threshold` plugin has been built-in, and *there is no more need to download yourself*
* The latest version of modified ADAblock ImageJ macro can be [downloaded here (by *right-click and save-as*)](https://github.com/Z-H-Sun/ADAblock/raw/master/ADAblock.ijm)
* You can customize the default settings by editing the first few lines of [ADAblock.ijm](/ADAblock.ijm)
* If your images were captured by Zeiss SEM, **and the image resolution is exactly 1024x768**, you can use the “Zeiss (Experimental)” option, so that the nm-to-pixel scale will be automatically detected by the macro, and the white edges containing the scale bar will be automatically cropped

### Caveats
![](https://img.shields.io/badge/Bug-P2-yellow?style=plastic) In addition to the settings you specify in the dialogs, you have to pay attention to other parameters assigned in the macro, [ADAblock.ijm](/ADAblock.ijm). For example, `period_range_max_nm` and `period_limits_nm` define the behaviors of automatic FFT (used for period calculation) and smoothing processes. Typically the default values are fine; however, if you work with block copolymers exhibiting extremely large spacings, say bottlebrush BCPs for photonic crystal applications, you may want to turn up the maximum values accordingly

![](https://img.shields.io/badge/Bug-P2-yellow?style=plastic) For correlation length calculation, the current settings are fine if your data fit well with the exponential decay model; otherwise, the selection of data range for fitting can impact the final result a lot. In that case, either the whole range or zero to twice the stepwise correlation length, as written in the macro, may not be a wise choice, and you may want to manually adjust the range to obtain a more physically meaningful result by using the table saved at `correlation_data_CL_0.xls`. 

---------------------

**Scripts:**

* **ADAblock.ijm** — The algorithm is designed to perform analysis of images of BCP thin films or surfaces structured by BCP thin films. It is run as a macro within ImageJ. 
* **Data_Amalgamation_Script.py** — Collects data from each of the output files produced by ADAblock.ijm, in the directories produced by ADAblock, and collects them into a single CSV file.

---------------------

Download ImageJ: https://rsbweb.nih.gov/ij

Download Python: https://www.python.org

