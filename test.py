import subprocess
import json
import time
from pprint import pprint

def runtest(i):
    out = open("output.json")
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
    for i in range(1):
        print(" - Test {} : ".format(i+1))
        time.sleep(1)
        runtest(i)
        time.sleep(1)
        if assertequals(i):
            print("Passed")
        else:
            o, e = dumpjson(i)
            print("Failed")
            print("Output :")
            pprint(o,indent=4)
            print("Expected : ")
            pprint(e,indent=4)
        print("======================================================================================")
        


        


def run_java_program(args):
    command = ['java','-jar','Formation.jar'] + args
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

   
    output, error = process.communicate()

    output = output.decode('utf-8')
    error = error.decode('utf-8')

    return output, error

if __name__ == "__main__":
    runtests()



