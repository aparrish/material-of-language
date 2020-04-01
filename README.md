# Material of Language

Notes and notebooks for [Material of Language](http://mol.decontextualize.com/).

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

* [Re-creating R. L. Draper's "top spin"](top-spin.ipynb) with `for` loops and
  custom `range`s
* [Concrete compositions in HTML](concrete-compositions-html.ipynb): CSS
  absolute positioning and Python to create procedural layouts

Asemic writing with procedural geometry:

* [Asemic writing with Flat](flat-asemic-writing.ipynb): Basic
  [Flat](https://xxyxyz.org/flat) tutorial plus some simple generative
  techniques for producing asemic writing;
  [Bezmerizing](https://github.com/aparrish/bezmerizing/) in use
* [Lines and asemic writing](lines-and-asemic.ipynb): Another take on using
  polylines, Catmull-Rom splines and Flat to make asemic characters
* [Handwriting remix](handwriting-remix.ipynb): Loading and manipulating data
  from the [Char74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/)
* [K-means glyphs](kmeans-glyphs.ipynb): Using K-means clustering to generate
  evenly-spaced random points (and then use those points to make asemic glyphs)

Fonts as data:

* [Manipulating font data](manipulating-font-data.ipynb): Introduction to font
  files and how to do stuff with them
* [Quick Hershey text](quick-hershey-text.ipynb): Loading and displaying
  Hershey font data as paths with Flat

