#Boolean Operator Precedence Rules

#and -> both of them needs to be true
if 1 == 1 and 2 == 2:
    print("True")
    
if 1 == 3 and 2 == 2:
    print("True")
    
#or -> needs at least one
if 1 == 1 or 2 == 3:
    print("True - or")

if 1 == 4 or 5 == 5:
    print("True - or")
    
#not = flips them around (must be false in order to be true)

if not 1 == 4:
    print("True - not")
    
    
# Parenthesis -> Not -> And -> Or

# not = False -> or True ! -> Executed
if not 1 == 1 or 5 == 5:
    print("True Prec")

# and = True = or True -> Executed
if 1 == 6 or 2 == 2 and 5 == 5:
    print("True Prec II")
    
    
