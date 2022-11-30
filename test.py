import subprocess
import os

def test_one(file_name: str):
    cwd = os.getcwd()
    compile_process = subprocess.Popen(
        "python3 main.py {} 1000 512 {}/test {}/test/0.in {}/test/0.out".format(file_name, cwd, cwd, cwd), shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    a = compile_process.communicate(30)
    print(a[0])


tests = os.listdir('./test')
for test in tests:
    if test.endswith('.py'):
        print(test)
        test_one(test)