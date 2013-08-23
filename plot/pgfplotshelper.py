#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains useful functions to create pgfplots code (latex
code using the pdfplots package) from python data.

One example of tex code for a plot using pgfplots is show below

.. code-block:: latex
    \begin{tikzpicture}
      \begin{axis}[axis options]
        \addplot[plot options"
        plot [options]
        coordinates {
          (0, 0)
          (1, 1)
          (2, 4)
          (3, 9)};
        \addlegendentry{Legend of the last line};
      \end{axis}
    \end{tikzpicture}

"""

__revision__ = "$Revision$"


def generate_pgfplots_plotline(x, y, errors=None, options=None):
    """

    Parameters
    ----------
    x : Iterable (numpy array or a list)
        The data for the 'x' axis in the plot.
    y : Iterable (numpy array or a list)
        The data for the 'x' axis in the plot
    errors : Iterable (numpy array or a list) or None
        The error for plotting the errorbars.
    options : str
        pgfplot options for the plot line.
        Ex: "color=red,
        solid,
        mark=square,
        mark options={solid}"
    """
    import itertools

    # xxxxxxxxxx Creates the coordinates part of the plot line xxxxxxxxxxxx
    points = zip(x, y)
    num_points = len(points)
    if errors is None:
        points_string = "\n".join([str(p) for p in points])
        plot_line = "plot[]\ncoordinates{{{0}}};".format(points_string)
    else:
        error_points = zip(itertools.repeat(0.0, num_points), errors / 2.0)
        points_and_errors_list = [
            "{0} +- {1}".format(a, b) for a, b in zip(points, error_points)]
        points_string = "\n".join(points_and_errors_list)
        plot_line = "plot[error bars/.cd, y dir = both, y explicit]\ncoordinates{{{0}}};".format(points_string)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    # xxxxxxxxxx Get the whole addplot line xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    if options is None:
        addplot_line = "\\addplot[]\n{0}".format(plot_line)
    else:
        addplot_line = "\\addplot[{1}]\n{0}".format(plot_line, options)
    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    return addplot_line

    # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx