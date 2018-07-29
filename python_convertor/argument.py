# coding=utf-8
import sys
import argparse
import os

print(sys.argv)
print(sys.argv[1])
path = '/home/yuzhikina/programms/'+ sys.argv[1]
os.mkdir(path)
