# MSAT - Multimedia Storage Analysis Toolkit

A toolkit to analyze the changes in storage requirements of multimedia objects as different
parameters are changed by up/down sizing/scaling/etc.

This project is being created as a part of my Master's thesis' preparation work.

## How to run

1. Install [pipenv](https://pipenv.pypa.io/en/latest/index.html) on your system.
2. Run `$ pipenv install` to install dependencies in your virtual env.
3. Create a directory of source media you want to analyze, put your files in there.
4. In the root of the repository, run: `$ PYTHONPATH=$pwd pipenv run python src/main.py`
5. There are some optional parameters to consider, use `--help` for more details.

## Dependencies

* `pillow` for image manipulation tasks
* `matplotlib` and `numpy` for reports

In any case, check the `Pipfile` for details!
