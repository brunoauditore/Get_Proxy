#!/bin/bash

cd git_repos
git clone https://github.com/monosans/proxy-list
mkdir -p proxies_anonymous
cp  -r proxy-list/proxies_anonymous/ proxies_anonymous/
rm -rf proxy-list
