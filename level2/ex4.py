import pandas as pd

result = [
    {"id":1,"name":"홍길동"},
    {"id":2,"name":"장보고"},
    {"id":3,"name":"임꺽정"}
]

print(result)

pandas_result = pd.DataFrame(result, index=["first","second","third"])

print(pandas_result)