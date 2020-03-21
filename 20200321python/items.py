from jinja2 import Template

def itemsHTML():
    with open('items.html') as f:
        s = f.read()
    return s

def main():
    item_list = [
        {'name': 'apple', 'count': 188},
        {'name': 'Chicken', 'count': 888},
        {'name': 'Dodo', 'count': 20000}
    ]

    tmpl = Template(itemsHTML())

    print(tmpl.render({'items': item_list}))

main()