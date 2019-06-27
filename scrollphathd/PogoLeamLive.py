#!/usr/bin/env python

import dweepy
import requests
import scrollphathd
import time

base_url='https://pogoleam.orangeninja.com/api/1.0/'
begin_end_pause=0.5
scroll_delay=0.01

locationData=requests.get(url=base_url+'locations')
locationNames={}
for location in locationData.json():
    locationNames[location['_id']]=location['name']

pokemon_names=requests.get(url=base_url+'pokemon').json()

displ_width=scrollphathd.get_shape()[0]

for dweet in dweepy.listen_for_dweets_from('pogoleam'):
    task=dweet['content']['task']
    stop_id=dweet['content']['stopID']
    reward=dweet['content']['reward']
    reward_num=dweet['content']['number']
    if reward=='Encounter':
        names=[]
        for dex_num in reward_num:
            names.append(pokemon_names[dex_num-1])
        reward_str='/'.join(names)
    else:
        reward_str=reward_count+' '+reward
    stopName=locationNames[stop_id]
    text=stopName+': '+task+' for '+reward_str
    print text
    # Show message on screen
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

