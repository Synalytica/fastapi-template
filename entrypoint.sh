#!/bin/sh
# coding: utf-8

# if $DEBUG is set to 1, run the script in debug mode
# elif $DEBUG is set to 0, run the script in prod mode
# else run the script in debug mode

if [ "$DEBUG" = "1" ]; then
    uv run --active fastapi dev main.py --host 0.0.0.0 --port 8080 --reload
elif [ "$DEBUG" = "0" ]; then
    uv run --active fastapi run main.py --host 0.0.0.0 --port 8080 --workers 4
else
    uv run --active fastapi dev main.py --host 0.0.0.0 --port 8080 --reload
fi
