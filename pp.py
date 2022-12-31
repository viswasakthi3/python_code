from unicodedata import name
import pandas as pd

column = ["hari", "vs", "sath"]
abc = {"name": column,
        "height":[8,9,10],
        "weight":[1,2,3]}
a = pd.DataFrame(abc)
i=a["name"][2]
print(i)
