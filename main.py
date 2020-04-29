import yaml

print("This is a test.")

# dummy comment

with open("example.yaml", 'r') as stream:
    try:
        # waiting for sonarqube
        print(yaml.load(stream))
        # print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

# code smells

DATA = ['a', 'b', 'c']

for i in range(len(DATA)):
    print(DATA[i])

def foo(a):  # NonCompliant
    b = 12
    if a == 1:
        return b
    return b