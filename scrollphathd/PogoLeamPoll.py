#!/usr/bin/env python

import requests
import scrollphathd
import time

base_url='https://pogoleam.orangeninja.com/api/1.0/'
begin_end_pause=0.5
scroll_delay=0.01

# Load static data from server
locationData=requests.get(url=base_url+'locations')
locationNames={}
for location in locationData.json():
    locationNames[location['_id']]=location['name']
pokemon_names=requests.get(url=base_url+'pokemon').json()

displ_width=scrollphathd.get_shape()[0]

def display_text(text):
    print text
    t_len=scrollphathd.write_string(text, brightness=0.05)
    scrollphathd.show()
    time.sleep(begin_end_pause)
    for x in range(t_len - displ_width):
        scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(scroll_delay)
    time.sleep(begin_end_pause)
    scrollphathd.clear()
    scrollphathd.show()

def display_update(dweet):
    task=dweet['task']
    stop_id=dweet['stopID']
    reward=dweet['reward']
    reward_num=dweet['number']
    if reward=='Encounter':
        names=[]
        for dex_num in reward_num:
            names.append(pokemon_names[dex_num-1])
        reward_str='/'.join(names)
    else:
        reward_str=str(reward_num)+' '+reward
    stopName=locationNames[stop_id]
    text=stopName+': '+task+' for '+reward_str
    display_text(text)

last_time=0
while True:
    response=requests.get('https://dweet.io/get/latest/dweet/for/pogoleam').json()
    latest=response['with'][0]
    timestamp=latest['created']
    if timestamp != last_time:
        last_time = timestamp
        dweet=latest['content']
        if 'raw_text' in dweet:
            display_text(dweet['raw_text'])
        else:
            display_update(dweet)
    time.sleep(10)

