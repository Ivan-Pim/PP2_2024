import json
import pprint

f = open('data.json')

data = json.load(f)

print("Interface Status")
print("=" * 100)
print(f"{'DN' :<50}{'Description' :<25}{'Speed' :<15}{'MTU' :<10}")
print("-" * 49, "-" * 24, "-" * 14, "-" * 10)
for i in data['imdata']:
    print(f"{i["l1PhysIf"]['attributes']['dn'] :<75}{i["l1PhysIf"]['attributes']['speed'] :<15}{i["l1PhysIf"]['attributes']['mtu'] :<10}")