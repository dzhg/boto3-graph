========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/boto3-graph/badge/?style=flat
    :target: https://readthedocs.org/projects/boto3-graph
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/boto3-graph.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/boto3-graph

.. |commits-since| image:: https://img.shields.io/github/commits-since/dzhg/boto3-graph/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/dzhg/boto3-graph/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/boto3-graph.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/boto3-graph

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/boto3-graph.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/boto3-graph

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/boto3-graph.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/boto3-graph


.. end-badges

GraphQL with boto3

* Free software: MIT license

Installation
============

::

    pip install boto3-graph

Documentation
=============

https://boto3-graph.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
