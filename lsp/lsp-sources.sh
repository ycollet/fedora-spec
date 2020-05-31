#!/bin/bash

VERSION=1.1.22

git clone https://github.com/sadko4u/lsp-plugins
cd lsp-plugins
git checkout lsp-plugins-$VERSION
git submodule init
git submodule update
find . -name .git --exec rm -rf {} \;
cd ..
tar cvfz lsp-plugins.tar.gz lsp-plugins/*
rm -rf lsp-plugins
