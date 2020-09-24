"""Write your code here"""
import requests


def get_pulls(state):
    if state == "open":
        return get_pulls_open()
    elif state == "closed":
        return get_pulls_closed()
    elif state == "accepted":
        return get_pulls_accepted()
    elif state == "needs work":
        return get_pulls_needs_work()


def get_pulls_open():
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            params={'per_page': '100'})
    data = response.json()
    open_list = []
    for element in data:
        if element["state"] == "open":
            diction = {
                "num": "x",
                "title": "x",
                "link": "x"
            }
            diction["num"] = element["number"]
            diction["title"] = element["title"]
            diction["link"] = element["html_url"]
            open_list.append(diction)
    open_list = sorted(open_list, key=lambda x: x['num'])
    return open_list


def get_pulls_closed():
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls?state=closed',
                            params={'per_page': '100'})
    data = response.json()
    closed_list = []

    for element in data:
        if element["state"] == "closed":
            diction = {
                "num": "x",
                "title": "x",
                "link": "x"
            }
            diction["num"] = element["number"]
            diction["title"] = element["title"]
            diction["link"] = element["html_url"]
            closed_list.append(diction)
    closed_list = sorted(closed_list, key=lambda x: x['num'])
    return closed_list


def get_pulls_accepted():
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            params={'per_page': '100'})
    data = response.json()
    accepted_list = []

    for element in data:
        if len(element["labels"]) > 0:
            if element["labels"][0]["name"] == "accepted":
                diction = {
                    "num": "x",
                    "title": "x",
                    "link": "x"
                }
                diction["num"] = element["number"]
                diction["title"] = element["title"]
                diction["link"] = element["html_url"]
                accepted_list.append(diction)
    accepted_list = sorted(accepted_list, key=lambda x: x['num'])
    return accepted_list


def get_pulls_needs_work():
    response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls',
                            params={'per_page': '100'})
    data = response.json()
    needs_work_list = []

    for element in data:
        if len(element["labels"]) > 0:
            if element["labels"][0]["name"] == "needs work":
                diction = {
                    "num": "x",
                    "title": "x",
                    "link": "x"
                }
                diction["num"] = element["number"]
                diction["title"] = element["title"]
                diction["link"] = element["html_url"]
                needs_work_list.append(diction)
    needs_work_list = sorted(needs_work_list, key=lambda x: x['num'])
    return needs_work_list
