# if (do / skip)
if (condition):
  ins_1
  ins_2
ins_outside

## notes
- this is an if conditionn
- ins_1 and ins_2 only executesd if if cond is True
- otherwise it skips to the ins_outside which always executes regardless if it True/False

# if else (do / auto)
if (condition):
  ins_1
  ins_2
else:
  ins_1
  ins_2
ins_outside

## notes
- this is an if else condition
- ins_1 and ins_2 from cond_1 only executes if True
- if False, it automatically skips to else and executes instructions iside else
- if True | Else = NO
- if False | Else = YES
- ins_outside always executed
