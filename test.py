from parameter_store import ParameterStore

import time

def main():
    print("Starting Test...")

    ps = ParameterStore()

    # Test SET and GET
    ps.set("TEST_INTEGER", 123)
    print("SET integer operation successful")
    
    ps.set("TEST_STRING", "somestring")
    print("SET string operation successful")
    
    ps.set("TEST_FLOAT", 12.3)
    print("SET float operation successful")
    
    ps.set("TEST_BOOL", True)
    print("SET bool operation successful")
    
    ps.set("TEST_LIST", ["a","b","c"])
    print("SET list operation successful")
    print()
    
    assert ps.get("TEST_INTEGER") == 123
    assert ps.get("TEST_STRING") == "somestring"
    assert ps.get("TEST_FLOAT") == 12.3
    assert ps.get("TEST_BOOL") == True
    assert ps.get("TEST_LIST") == ["a","b","c"]
    print("All GET operation successful")
    print()
    
    # Test mget and mset
    
    testDict = {"key1": 123, "key2": "value2", "key3": True, "key4": 12.3}
    ps.mset(testDict)
    print("MSET operation successful")
    
    testList = ["key1","key2","key3","key4"]
    
    assert ps.mget(testList) == testDict
    print("MGET operation successful")

    ps.set("DONE", True)
    while True:
        if ps.get("DONE") == "False":
            break
        else:
            time.sleep(1)

    print("end of program.")
 

if __name__ == "__main__":
    main()