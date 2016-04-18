'''
    the simple udacity project reminds you taking breaks every 2 hour.
    every 2 hour it plays your favourite palylist video/audio on youtube

'''
import webbrowser
import time

playlist = ["https://www.youtube.com/watch?v=KcUfiGgTkbw",
            "https://www.youtube.com/watch?v=wZSjyCXCSeU",
            "https://www.youtube.com/watch?v=7cZDRM28LgM",
            "https://www.youtube.com/watch?v=iwCgBhkD3-o"
            ]


def take_a_break(wishlist):
    for i in wishlist:
        print "waiting for 2 hours"
        time.sleep(2*60*60)  #count when its 2 hour
        webbrowser.open(i)


take_a_break(playlist)