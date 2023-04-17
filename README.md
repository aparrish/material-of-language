# Material of Language/Computational Letterforms and Layout

Notes and notebooks for [Material of Language](http://mol.decontextualize.com/)
and its newer iteration, [Computational Letterforms and
Layout](https://cll.decontextualize.com/).

If you want to play around with the notebooks or can't get the dependencies
working on your machines, [the repository is available on
Binder](https://mybinder.org/v2/gh/aparrish/material-of-language/master).
Everything should work there, just make sure to download your modified
notebooks and output to your own computer when you're done.

**Please note that many of these notebooks do not display correctly in GitHub's
preview** for some reason. (In particular, the "Concrete compositions" and
"Letters as numbers" notebooks are significantly truncated.) Please download
these and view them locally!

Python intro notebooks:

* [Letters as numbers](letters-as-numbers.ipynb): How text is represented
  (Unicode and other encodings)
* [Interpolating strings](interpolating-strings.ipynb): Strategies for putting
  string together in Python

Concrete composition:

* [Intro to HTML and CSS](documents-with-html-and-css.ipynb)
* [Concrete compositions in HTML](concrete-compositions-html.ipynb): CSS
  absolute positioning and Python to create procedural layouts
* [Re-creating R. L. Draper's "top spin"](top-spin.ipynb) with `for` loops and
  custom `range`s

Asemic writing with procedural geometry:

* [Generative asemic writing with
  vsketch](https://github.com/aparrish/material-of-language/blob/master/lines-and-asemic-vsketch.ipynb):
  Basic tutorial on [vsketch](https://github.com/abey79/vsketch) and some
  techniques for producing asemic writing with procedures
* [Polylines are just
  numbers](https://github.com/aparrish/material-of-language/blob/master/polylines-are-just-numbers.ipynb):
  Transforming polylines with math
* [Strategies for line thickness
  variation](https://github.com/aparrish/material-of-language/blob/master/imitating-line-thickness-variation.ipynb):
  How to imitate variation in line thickness when all you have are polylines
* [K-Means
  glyphs](https://github.com/aparrish/material-of-language/blob/master/kmeans-glyphs-vsketch.ipynb):
  Using K-means clustering to generate evenly-spaced random points (and then
  use those points to make asemic glyphs)
* [Polylines are just data: Hershey
  Fonts](https://github.com/aparrish/material-of-language/blob/master/polylines-data-01-hershey-fonts.ipynb):
  Loading polylines as data and doing things with them

Fonts as data:

* [Manipulating font
  data](https://github.com/aparrish/material-of-language/blob/master/manipulating-font-data-vsketch.ipynb)
  with Freetype-py and vsketch

Interactivity:

* [Interactive widgets with ipywidgets](interactive-widgets-vsketch.ipynb)

I also have a number of older notebooks that use
[Flat](https://xxyxyz.org/flat) as the drawing library, instead of vsketch. For
the most part, the content of these is more or less the same as the
identically-named versions above.

* [Asemic writing with Flat](flat-asemic-writing.ipynb): Basic
  [Flat](https://xxyxyz.org/flat) tutorial plus some simple generative
  techniques for producing asemic writing;
  [Bezmerizing](https://github.com/aparrish/bezmerizing/) in use
* [Lines and asemic writing](lines-and-asemic.ipynb): Another take on using
  polylines, Catmull-Rom splines and Flat to make asemic characters
* [Handwriting remix](handwriting-remix.ipynb): Loading and manipulating data
  from the [Char74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)
* [K-means glyphs](kmeans-glyphs.ipynb)
* [Manipulating font data](manipulating-font-data.ipynb)
* [Quick Hershey text](quick-hershey-text.ipynb)
* [Sampling from Google's SVG VAE](https://colab.research.google.com/drive/1CR5L6eKoiy7M-nt4PLZDZ7xVPHKgzRlG)
* Training DCGAN on glyph images: [part
  1](https://colab.research.google.com/drive/19BR0cccrRIIiWkzWiN3Mg8CCEF7nbli9),
  [part
  2](https://colab.research.google.com/drive/1K5H6FqLNfUnkhkFGdFjnBuhgKEQcBldq)
* [Flat with interactive widgets](interactive-widgets.ipynb)
* [Creating animations with Flat and ffmpeg](creating-animations.ipynb)
* [Standalone scripts and web apps with Glitch](standalone-and-webapps.ipynb)

