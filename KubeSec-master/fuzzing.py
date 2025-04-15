# test_scanner.py
from parser import keyMiner
from parser import getKeyRecursively
from parser import getValuesRecursively
from parser import getValsFromKey
from parser import update_json_paths


test_dict = {
    "root": {
        "key1": {
            "subkey1": "value1",
            "subkey2": "value2"
        },
        "key2": "value3",
        "key3": {
            "subkey3": "value4"
        }
    }
}

def fuzz_keyMiner():
    print("Running fuzzing for keyMiner")
    result = keyMiner(test_dict, "value1")
    print(result)
    result = keyMiner(test_dict, "nonexistent_value")
    print(result)

def fuzz_getKeyRecursively():
    result_list = []
    print("Running fuzzing for getKeyRecursively")
    getKeyRecursively(test_dict, result_list)
    print(result_list)

def fuzz_getValuesRecursively():
    print("Running fuzzing for getValuesRecursively")
    result = list(getValuesRecursively(test_dict))
    print(result)

def fuzz_getValsFromKey():
    result_list = []
    print("Running fuzzing for getValsFromKey")
    getValsFromKey(test_dict, "key1", result_list)
    print(result_list)

def fuzz_update_json_paths():
    print("Running fuzzing for update_json_paths")
    result = update_json_paths(["[3].metadata.name", "[5].data[2].value"])
    print(result)
    

if __name__ == "__main__":
    fuzz_keyMiner()  # Running the test function
    fuzz_getKeyRecursively()
    fuzz_getValuesRecursively()
    fuzz_getValsFromKey()
    fuzz_update_json_paths()

