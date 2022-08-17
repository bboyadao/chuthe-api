#!/bin/bash
eval $(grep -v -e '^#' local.env | xargs -I {} echo export \'{}\')