#!/usr/bin/env bash

VENVNAME=frille-vis
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME