from jinja2 import Template

def welcomeHTML():
    s = ''
    s += '<!DOCTYPE html>'
    s += '<html>'
    s += '  <head>'
    s += '      <title>Welcome, {{user.name}} </title>'
    s += '      <meta charset="utf-8">'
    s += '  </head>'
    s += '  <body>'
    s += '      <h1>Welcome, {{user.name}} </h1>'
    s += '      <p>You have {{user.likes}} likes.</p>'
    s += '      <p>Come here everyday...</p>'
    s += '  </body>'
    s += '</html>'
    return s

def main():
    user1 = { 'name': 'Alice', 'likes': 666 }
    user2 = { 'name': 'Rocketfeller', 'likes': 999999 }

    tmpl = Template(welcomeHTML())

    print(tmpl.render({'user': user1}))
    print(tmpl.render({'user': user2}))

main()