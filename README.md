# house_of_dust

This is a generative poetry program!

Arguments:
`count` is the number of repeated stanzas you would like
`template` is the python string template for the stanzas
`input-files` is the files with newline separated choices to populate the template in order

Note! Please have the same number of spaces in your template as you have input files.

i.e. python .\HouseOfDust.py --template "A tree with {} leaves, unburdened by {}" --input-files .\SecondLight.txt .\ThirdTenant.txt --count 5