from aocd.models import Puzzle
data = Puzzle(year=2020, day=19).input_data

"""
    Day 19: Monster Messages

    Puzzle input:
        - List of rules and messages to validate

    Task 1:
        - Determine number of complete matches for the messages
    
    Task 2:

    Strategy (Part 1): 
        - This is a simple grammar, parser problem


    
    Strategy (Part 2): 
"""

"""
Meta-Grammar: 

    start[AST]: rules ENDMARKER

    rules:
        | rule NEWLINE rules { [rule] + rules }
        | rule { [rule] }

    rule: 
        | a=NUMBER ':' b=operations NEWLINE { Tuple(a, b) }
        | a=NUMBER ':' b=atom NEWLINE { Tuple(a, b) }

    operations:
        | operation operations
        | operation

    operation:
        | a=atom b=atom { Operation(a, b, and) }
        | a=atom '|' b=atom { Operation(a, b, or) }

    atom:
        | a=STRING { Constant(a) }
        | a=NUMBER { ruledict[a] }
"""

"""
Parse the Input Data
"""
with open("short.txt", 'r') as f:
    #data = f.read().rstrip()
    pass

rules, text = data.split('\n\n')

def rule_maker(raw_rules):
    rules = {}
    for rule in raw_rules:
        key, value = rule.split(': ')
        if value[0] == '"':
            rules[int(key)] = value[1:-1]
        else:
            values = value.split(' | ')
            temp_v = []
            for v in values:
                temp_v.append([int(vv) for vv in v.split(' ')])
            rules[int(key)] = temp_v
    return rules

def match_rule(expr, stack):
    if len(stack) > len(expr):
        return False
    elif len(stack) == 0 or len(expr) == 0:
        return len(stack) == 0 and len(expr) == 0

    c = stack.pop()
    if isinstance(c, str):
        if expr[0] == c:
            return match_rule(expr[1:], stack.copy())
    else:
        for rule in rules[c]:
            if match_rule(expr, stack + list(reversed(rule))):
                return True
    return False

def count_messages(rules, messages):
    total = 0
    for message in messages:
        if match_rule(message, list(reversed(rules[0][0]))):
            total += 1
    return total

rules = rule_maker(rules.split('\n'))
text = text.split('\n')

print(f"Part 1: {count_messages(rules, text)}")
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print(f"Part 2: {count_messages(rules, text)}")
