# -*- coding: utf-8 -*-
import os
import pypandoc


f = open('README.txt', 'w+')

f.write(pypandoc.convert('README.md', 'rst'))
f.close()
os.system("python setup.py sdist upload -r https://pypi.python.org/pypi")
os.system("python setup.py sdist")
os.remove('README.txt')
