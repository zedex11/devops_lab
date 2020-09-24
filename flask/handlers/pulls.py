"""Write your code here"""
import requests


def get_pulls(state):
    data = get_content()
    if state == "open" or state == "closed":
        return get_pulls_state(data, state)
    elif state == "accepted" or state == "needs work":
        return get_pulls_label(data, state)


def get_content():
    user = 'user_name'  # enter your git-hub username
    passwd = 'password'  # enter your git-hub password
    params = {'per_page': '100', 'state': 'all'}
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            auth=(user, passwd), params=params)
    data = response.json()
    return data


def get_pulls_state(data, state):
    state_list = []
    for element in data:
        if element["state"] == state:
            diction = {
                "num": "x",
                "title": "x",
                "link": "x"
            }
            diction["num"] = element["number"]
            diction["title"] = element["title"]
            diction["link"] = element["html_url"]
            state_list.append(diction)
    state_list = sorted(state_list, key=lambda x: x['num'])
    return state_list


def get_pulls_label(data, state):
    label_list = []
    for element in data:
        if len(element["labels"]) > 0:
            if element["labels"][0]["name"] == state:
                diction = {
                    "num": "x",
                    "title": "x",
                    "link": "x"
                }
                diction["num"] = element["number"]
                diction["title"] = element["title"]
                diction["link"] = element["html_url"]
                label_list.append(diction)
    label_list = sorted(label_list, key=lambda x: x['num'])
    return label_list
