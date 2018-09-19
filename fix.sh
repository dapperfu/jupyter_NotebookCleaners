#!/bin/sh

LINE_LENGTH=320

black --py36 --line-length=${LINE_LENGTH} $1
isort --line-width ${LINE_LENGTH} --multi-line 3 --dont-skip __init__.py $1
