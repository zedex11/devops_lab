"""Write your code here"""
import requests


def get_pulls(state):
    data = get_content()
    if state == "open" or state == "closed":
        return get_pulls_state(data, state)
    elif state == "accepted" or state == "needs work":
        return get_pulls_label(data, state)
    else:
        return get_pulls_full(data)


def get_content():
    user = 'user_name'  # enter your git-hub username
    passwd = 'password'  # enter your git-hub password
    params = {'per_page': '100', 'state': 'all'}
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            auth=(user, passwd), params=params)
    data = response.json()
    return data


def get_pulls_full(data):
    full_list = []
    for e in data:
        full_list.append({"num": e["number"], "link": e["html_url"], "title": e["title"]})
    full_list = sorted(full_list, key=lambda x: x['num'])
    return full_list


def get_pulls_state(data, state):
    state_list = []
    for e in data:
        if e["state"] == state:
            state_list.append({"num": e["number"], "link": e["html_url"], "title": e["title"]})
    state_list = sorted(state_list, key=lambda x: x['num'])
    return state_list


def get_pulls_label(data, state):
    label_list = []
    for e in data:
        if len(e["labels"]) > 0:
            if e["labels"][0]["name"] == state:
                label_list.append({"num": e["number"], "link": e["html_url"], "title": e["title"]})
    label_list = sorted(label_list, key=lambda x: x['num'])
    return label_list
