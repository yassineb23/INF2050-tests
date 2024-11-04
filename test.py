import subprocess
import json
import time
from pprint import pprint
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pip
import sys




def runtest(i):
    out = open("output.json","w")
    args =  ['tests/test{}.json'.format(i), 'output.json']
    o, e = run_java_program(args)
    if e:
        print("Erreur JAVA : {}".format(e))

def dumpjson(i):
    with open("output.json") as out, open("tests/OUTtest{}.json".format(i)) as expected: 
        o = json.load(out)
        e = json.load(expected)
    return o , e

def assertequals(i):
    o, e = dumpjson(i)
    return o == e

def runtests():
    for i in range(7):
        print(" - Test {} : ".format(i+1), end=" ")
        time.sleep(1)
        runtest(i)
        if assertequals(i):
            print(f"{Fore.GREEN}Passed{Style.RESET_ALL}")
        else:
            o, e = dumpjson(i)
            print(f"{Fore.RED}Failed{Style.RESET_ALL}")
            print("Output : ", end=" ")
            pprint(o,indent=4)
            print("Expected : ", end=" ")
            pprint(e,indent=4)
        print("======================================================================================")
        


        


def run_java_program(args):
    command = ['java','-jar','Formation.jar'] + args

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output, error = process.communicate()


    return output, error

if __name__ == "__main__":
    pack = "colorama"
    if not pack in sys.modules:
        pip.main(["install ",pack])
    colorama_init()
    runtests()



