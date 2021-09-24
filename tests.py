import random
import subprocess
import time
import sys

sys.setrecursionlimit(10000)

def test_all():
    std = subprocess.check_output(['python', 'main.py', "--coords", "1,2", "3,4", "5,6", '--rounds', '2'])
    assert std.decode('utf-8').strip() == "[]" or std.decode('utf-8').strip() == "None"

    block = subprocess.check_output(
        ['python', 'main.py', "--coords", "1,0", "2,1", "4,1", "0,2", "2,3", "3,3", "5,3", '--rounds', '240'])
    assert "(0, 0)" in block.decode('utf-8').strip()
    assert "(0, 1)" in block.decode('utf-8').strip()
    assert "(1, 0)" in block.decode('utf-8').strip()
    assert "(1, 1)" in block.decode('utf-8').strip()

    if True:
        no_input = subprocess.check_output(['python', 'main.py', '--rounds', '100'])
        assert no_input.decode('utf-8').strip() == "[]" or no_input.decode('utf-8').strip() == "None"

    schiff = subprocess.check_output(
        ['python', 'main.py', "--coords", "1,0", "2,1", "0,2", "1,2", "2,2", '--rounds', '100'])  # 2204
    assert "(1, 0)" in schiff.decode('utf-8').strip()
    assert "(2, 1)" in schiff.decode('utf-8').strip()
    assert "(0, 2)" in schiff.decode('utf-8').strip()
    assert "(1, 2)" in schiff.decode('utf-8').strip()
    assert "(2, 2)" in schiff.decode('utf-8').strip()

    block = subprocess.check_output(
        ['python', 'main.py', "--coords", "0,0", "1,1", "0,1", "1,0", '--rounds', "100"])
    assert "(0, 0)" in block.decode('utf-8').strip()
    assert "(0, 1)" in block.decode('utf-8').strip()
    assert "(1, 0)" in block.decode('utf-8').strip()
    assert "(1, 1)" in block.decode('utf-8').strip()

    clock = subprocess.check_output(
        ['python', 'main.py', "--coords", "2,0", "1,1", "0,1", "2,2", "3,2", "1,3", '--rounds', "100"])
    assert "(2, 0)" in clock.decode('utf-8').strip()
    assert "(1, 1)" in clock.decode('utf-8').strip()
    assert "(0, 1)" in clock.decode('utf-8').strip()
    assert "(2, 2)" in clock.decode('utf-8').strip()
    assert "(3, 2)" in clock.decode('utf-8').strip()
    assert "(1, 3)" in clock.decode('utf-8').strip()

    eight = subprocess.check_output(
        ['python', 'main.py', "--coords", "0,0", "0,1", "1,1", "1,0", "2,0", "2,1", "2,2", "0,2", "1,2",
                                          "3,3", "3,4", "4,4", "4,3", "5,3", "5,4", "5,5", "3,5", "4,5", '--rounds', "623"])
    assert "(0, 0)" in eight.decode('utf-8').strip()
    assert "(1, 1)" in eight.decode('utf-8').strip()
    assert "(0, 1)" in eight.decode('utf-8').strip()
    assert "(1, 0)" in eight.decode('utf-8').strip()
    assert "(3, 1)" in eight.decode('utf-8').strip()
    assert "(4, 2)" in eight.decode('utf-8').strip()
    assert "(1, 3)" in eight.decode('utf-8').strip()
    assert "(2, 4)" in eight.decode('utf-8').strip()
    assert "(4, 4)" in eight.decode('utf-8').strip()
    assert "(5, 5)" in eight.decode('utf-8').strip()
    assert "(4, 5)" in eight.decode('utf-8').strip()
    assert "(5, 4)" in eight.decode('utf-8').strip()

    eight_to_eight = subprocess.check_output(
        ['python', 'main.py', "--coords", "0,0", "0,1", "1,1", "1,0", "2,0", "2,1", "2,2", "0,2", "1,2",
                                          "3,3", "3,4", "4,4", "4,3", "5,3", "5,4", "5,5", "3,5", "4,5", '--rounds', "624"])
    assert "(0, 0)" in eight_to_eight.decode('utf-8').strip()
    assert "(1, 1)" in eight_to_eight.decode('utf-8').strip()
    assert "(0, 1)" in eight_to_eight.decode('utf-8').strip()
    assert "(1, 0)" in eight_to_eight.decode('utf-8').strip()
    assert "(2, 0)" in eight_to_eight.decode('utf-8').strip()
    assert "(2, 1)" in eight_to_eight.decode('utf-8').strip()
    assert "(2, 2)" in eight_to_eight.decode('utf-8').strip()
    assert "(0, 2)" in eight_to_eight.decode('utf-8').strip()
    assert "(1, 2)" in eight_to_eight.decode('utf-8').strip()
    assert "(3, 3)" in eight_to_eight.decode('utf-8').strip()
    assert "(3, 4)" in eight_to_eight.decode('utf-8').strip()
    assert "(4, 4)" in eight_to_eight.decode('utf-8').strip()
    assert "(4, 3)" in eight_to_eight.decode('utf-8').strip()
    assert "(5, 3)" in eight_to_eight.decode('utf-8').strip()
    assert "(5, 4)" in eight_to_eight.decode('utf-8').strip()
    assert "(5, 5)" in eight_to_eight.decode('utf-8').strip()
    assert "(3, 5)" in eight_to_eight.decode('utf-8').strip()
    assert "(4, 5)" in eight_to_eight.decode('utf-8').strip()

    blinkerfuse = subprocess.check_output(
        ['python', 'main.py', "--coords", "0,0", "0,1", "1,0", "2,0", "2,1", "2,2", "0,2", "1,2",
                                          "7,0", "7,1", "7,2", "13,0", "13,1", "13,2", "19,0", "19,1", "19,2", '--rounds', "67"])
    assert "(1, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(7, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 7)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 1)" in blinkerfuse.decode('utf-8').strip()
    assert "(6, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(8, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 0)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 6)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 8)" in blinkerfuse.decode('utf-8').strip()
    assert "(0, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(2, 4)" in blinkerfuse.decode('utf-8').strip()
    assert "(4, 2)" in blinkerfuse.decode('utf-8').strip()

before = time.time()
for _ in range(20):
    test_all()
after = time.time()
print((after - before)/20)
#Elo_def: 2.1636388182640074
#Gabriel: 2.7670257687568665