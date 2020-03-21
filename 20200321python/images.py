from jinja2 import Template

def imagesHTML():
    with open('images.html') as f:
        s = f.read()
    return s

def main():
    image_list = [
        {'title': 'Fortnite', 'url': 'https://cdn2.unrealengine.com/Fortnite%2Fblog%2Fbatman-glides-to-fortnite-on-batman-day%2F10BR_BlackMonday_Screenshot_NewsHeader-1920x1080-9cc773391193a8f6267461c2a81915bfe5405a57.jpg', 'Desc': 'HA!'},
        {'title': 'Aerobic Dance', 'url': 'https://i.ytimg.com/vi/DCyTijJzEwo/maxresdefault.jpg', 'Desc': 'HA!'},
        {'title': 'Food', 'url': '<img src="https://eatforum.org/content/uploads/2018/05/table_with_food_top_view_900x700.jpg" alt="Image result for food"/>', 'Desc': 'Yum!'}
    ]

    tmpl = Template(imagesHTML())

    print(tmpl.render({'image': image_list}))

main()