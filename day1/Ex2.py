j_data1={
    "key1":"data1",
    "key2":"data2",
    "key3":"data3",
    "key4":[100,"data"]
}
j_data2={
    "key4":"data1",
    "key5":"data2",
    "key6":"data3",
    "key7":100
}
import json
with open("data.json",'w') as f:
    json.dump(j_data1,f)

