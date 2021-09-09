#!/bin/python3.8
import json
import requests
import os

os.system("./git_get.sh")

## http
with open('git_repos/proxies_anonymous/proxies_anonymous/http.txt') as http_file:
    proxy_http_text = http_file.read()

## socks5
with open('git_repos/proxies_anonymous/proxies_anonymous/http.txt') as socks5_file:
    proxy_socks5_text = socks5_file.read()

def _parse_proxy(text):
    proxy_list = []
    s = ''
    ip = ''
    for el in text:
        if el == '\n':
            proxy_list.append([ip,int(s)])
            s = ''
        elif el == ':':
            ip = s
            s = ''
        else:
            s += el

    return proxy_list


def get_http_proxy():
    return _parse_proxy(proxy_http_text)

def get_socks5_proxy():
    return _parse_proxy(proxy_socks5_text)
