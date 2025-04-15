# test_scanner.py
from parser import keyMiner  # Import the keyMiner function

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
    print("Running fuzzing for keyMiner...")
    result = keyMiner(test_dict, "value1")
    print(result)
    result = keyMiner(test_dict, "nonexistent_value")
    print(result)

#

if __name__ == "__main__":
    fuzz_keyMiner()  # Running the test function
