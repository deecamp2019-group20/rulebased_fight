import os

WORK_DIR, _ = os.path.split(os.path.abspath(__file__))

CARDS = range(3, 18)
STR = [str(i) for i in range(3, 11)] + ['J', 'Q', 'K', 'A', '2', '小', '大']
DICT = dict(zip(CARDS, STR))
ENV_DIR = os.path.join(WORK_DIR, 'precompiled')
