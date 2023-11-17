import pytest
from television import Television

#test __init__, power, channel_up, channel_down, volume_up, volume_down, mute

def test_init():
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__muted == False
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True
    tv.power()
    assert tv._Television__status == False

def test_mute():
    tv = Television()
    tv.mute()
    assert tv._Television__muted == False
    tv.power()
    tv.mute()
    assert tv._Television__muted == True
    tv.mute()
    assert tv._Television__muted == False

def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    assert tv._Television__channel == 2
    tv.channel_up()
    assert tv._Television__channel == 3
    tv.channel_up()
    assert tv._Television__channel == 0

def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert tv._Television__channel == 3
    tv.channel_down()
    assert tv._Television__channel == 2
    tv.channel_down()
    assert tv._Television__channel == 1
    tv.channel_down()
    assert tv._Television__channel == 0

def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.volume_up()
    assert tv._Television__volume == 2
    tv.volume_up()
    assert tv._Television__volume == 2

def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert tv._Television__volume == 0
    tv.volume_down()
    assert tv._Television__volume == 0
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 2


