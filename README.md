# Weather-Sinoptik
This is a weather program that can help you understand what the weather is in your city. Instead of using a normal Browser-client, etc., I've made software that can automatically tell you what the weather is for each city. It is an API program that uses **[sinoptik.bg](https://www.sinoptik.bg)** 
- - -\Further updates will be introduced
Countries added:

| Country     | Cities                                                   |
| ----------- | -------------------------------------------------------- |
| Bulgaria    | Shumen, Varna, Sofia, Plovdiv, Ruse, Stara Zagora, Vidin |


*New stuff added, you can now implement it in an other software and can be used easily, by using the **"vreme.py"** program.*<br>
Instance usage: 
```python
from vreme import * 
def main():
    act = CheckSNVR(region=("Ruse", "Varna", "Sofia"), output="html", warnings="strict") 
    act.rnm = True
    act.return_ogdoc = False
    act.verbose = True
    all_ = act.getrs
    # you can here use the print function, in order you to see the OUTPUT and all the actual values. You can see an instance below.
    """
    print("".join(item for item in all_))
    """
if __name__ == "__main__":
    main()
```
