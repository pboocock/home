import twitter
api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')

def post_status():
    get_status = raw_input("""
    What would you like to tweet?
    Write here:    """)
    
    if len(get_status) > 140:
        print """I couldn't post your tweet because it's %r characters too long.""" % ((len(get_status) - 140))
        return False
    else:
        status_post = api.PostUpdate(get_status)
        print "Tweet posted!"
        return True

count = 0

while post_status() == False:
    post_status()
    count += 1
    if count > 10:
        break