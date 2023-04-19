#!/usr/bin/env python3

#import time
import vk_api
import json
from datetime import datetime
from datetime import timedelta

TOKEN = vk_api.VkApi(token="") # here you must write your API_key 
vk = TOKEN.get_api()

with open('club.json') as f:
    groups = json.load(f)

check_dict={}
class Parse_VK:
    """
    This Class get group vk
    """

    def __init__(self, groups_json):
        self.groups = groups_json
        self.count = 10

    def alanalises(self):
        """
        This fuction breake data on fragments done
        ID post, time post, text post
        """
        for grop in range(len(self.groups['club'])):
            vk_wall = vk.wall.get(count=self.count, owner_id=self.groups['club'][grop])
            id_group = str(self.groups['club'][grop])[1:]
            for post in range(self.count):
                id_post = vk_wall['items'][post]['id']
                date_post = (vk_wall['items'][post]['date'])
                text = vk_wall['items'][post]['text']
                if vk_wall['items'][post].get('is_pinned'):
                    print("we skip post")
                    continue
                else:
                    if (datetime.now()  < datetime.fromtimestamp(date_post)+ timedelta(minutes=15)) :
                        yield  id_group, id_post, date_post, text,
                    else:
                        print("we break get group")
                        break

test = Parse_VK(groups).alanalises()
