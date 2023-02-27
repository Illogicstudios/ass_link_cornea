# Asset Linker Cornea

Asset Linker Cornea is a tool that links lights to corneas of a character standin.

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common


You must specify the correct path of the installation folder in the ```template_main.py``` file :
```python
if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/ass_link_cornea'
    # [...]
```
You also must add a file named ```cornea_by_char.py``` (see ```template_cornea_by_char.py```) that contains a
dictionnary of all the cornea name for a character in a project :
```python
CORNEA_CHAR = {
    "<PROJECT_DIR>": {
        "<first_char_name>": ['cornea_L_char', 'cornea_R_char'],
        "<second_char_name>": ['cornea_RcorneaShape', 'cornea_LcorneaShape'],
        "<third_char_name>":['L_irisShape', 'R_irisShape'],
        "<fourth_char_name>": ['corneasShape'],
    }
}
```


---

## Link Lights to Cornea

### First Part

You must select first all the lights that you want to link to the corneas of the asset. Then select in last the 
asset standin. You only have to run to link the corneas automatically.
