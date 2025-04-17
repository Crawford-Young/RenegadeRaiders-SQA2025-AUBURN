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
        },
        "key3": {
            "subkey3": {
                "subKey4": "value5"
            }
        }
    }
}

test_dict2 = {
    "config": {
        "settings": {
            "theme": "dark",
            "language": "en"
        },
        "users": [
            {
                "id": 1,
                "name": "Alice"
            },
            {
                "id": 2,
                "name": "Bob"
            }
        ]
    },
    "status": "active",
    "metadata": {
        "created": "2023-01-01",
        "modified": "2023-06-01"
    }
}


def fuzz_keyMiner():
    print()
    print("Running fuzzing for keyMiner")
    result = keyMiner(test_dict, "value1")
    print(result)
    result = keyMiner(test_dict, "nonexistent_value")
    print(result)
    result = keyMiner(test_dict, "value2")
    print(result)
    result = keyMiner(test_dict, "value3")
    print(result)
    result = keyMiner(test_dict, "value4")
    print(result)
    result = keyMiner(test_dict, "value5")
    print(result)
    print()

def fuzz_getKeyRecursively():
   
    print()
    print("Running fuzzing for getKeyRecursively")
    result_list = []
    getKeyRecursively(test_dict, result_list)
    print(result_list)
    result_list = []
    getKeyRecursively(test_dict2, result_list)
    print(result_list)
    print()


def fuzz_getValuesRecursively():
    print()
    print("Running fuzzing for getValuesRecursively")
    result = list(getValuesRecursively(test_dict))
    print(result)
    result = list(getValuesRecursively(test_dict2))
    print(result)
    print()

def fuzz_getValsFromKey():
    print()
    print("Running fuzzing for getValsFromKey")
    result_list = []
    getValsFromKey(test_dict, "key1", result_list)
    print(result_list)
    result_list = []
    getValsFromKey(test_dict2, "id", result_list)
    print(result_list)
    print()

def fuzz_update_json_paths():
    print()
    print("Running fuzzing for update_json_paths")
    result = update_json_paths(["[3].metadata.name", "[5].data[2].value"])
    print(result)
    result = update_json_paths(["[0].data.name"])
    print(result)
    result = update_json_paths(["data.name"])
    print(result)
    result = update_json_paths(["[12]"])
    print(result)
    result = update_json_paths(["[3][4].nested.value"])
    print(result)
    result = update_json_paths(["[9].a[1].b[2].c"])
    print(result)
    print()
    

if __name__ == "__main__":
    fuzz_keyMiner()  # Running the test function
    fuzz_getKeyRecursively()
    fuzz_getValuesRecursively()
    fuzz_getValsFromKey()
    fuzz_update_json_paths()

