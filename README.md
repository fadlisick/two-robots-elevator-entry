# Two Robots in an Elevator

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

One line of awkward small talk that one robot says to another while they ride an elevator together. Entry for the make.fun competition "Two Robots in an Elevator" (pot $10, top 10).

## The line

> We have been riding together for three floors and neither of us has pressed a button. I respect the commitment to nowhere.

## How it works

`main.py` writes exactly that line (122 characters) to `/output/entry.txt`. It validates the gate first: 1-200 UTF-8 characters, a single line, no leading or trailing whitespace. Deterministic: the same bytes on every run.

Run locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
