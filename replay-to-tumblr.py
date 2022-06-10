###########################################################################################################
# tumblr: https://www.tumblr.com/docs/en/api/v2                                                           #
# Rate limits:                                                                                            #
#   300 API calls per minute, per IP address.                                                             #
#    18,000 API calls per hour, per IP address.                                                           #
#    432,000 API calls per day, per IP address.                                                           #
#    1,000 API calls per hour, per consumer key.                                                          #
#    5,000 API calls per day, per consumer key.                                                           #
#    250 new posts (including reblogs) per day, per user.                                                 #
#    150 images uploaded per day, per user.                                                               #
#    200 follows per day, per user.                                                                       #
#    1,000 likes per day, per user.                                                                       #
#    10 new blogs per day, per user.                                                                      #
#    20 videos uploaded per day, per user.                                                                #
#    10 minutes of total video uploaded per day, per user.                                                 #
###########################################################################################################

# Import required modules(packages) to ensure that the twitterpost system will work.
import random           # import the random number generator (for science)
import array            # import the array module

import time             # import the time system
import datetime         # import the datetime system
from datetime import date

import os               # import the operating system functions

import re

import json             # import the json package to process files
import pytumblr         # import the pytumblr package

###########################################################################################################
# grab a baseline timeframe before main is called. (Filler)
today = time.strftime("%Y-%m-%d %H:%M")

###########################################################################################################
# list of phrases used in tweet generation (we can keep adding these)
# the idea will be like STREAMER_NAME + COMMENT, so like 'SimmyDizzle is on a roll!' will be generated.
phrases = [
    ' strikes again!',
    ' has struck again!',
    ' is on a roll!',
    ' cannot believe its not butter!',
    ' has something special here.',
    ' needs your approval! Hit that like and follow button!',
    ' cannot believe it!',
    ' would like to your opinion!',
    ' is this the flavour of the month?',
    ' what do you think?',
    ' gamer extroadinaire!',
    ' lover extroadinaire!',
    ' is thinking about an onlyfans page, ya know, for science.',
    ' has let loose something here!',
    ' thinks this is interesting enough to share.',
    ' is out of crazy ideas.'
    ' could fap to this.'
    ' would fap to this.'
    ' has fapped to this.'
    ' has truly gone mad!',
    ' is thinking this is something everyone should see.'
    ' is thinking this is badass.'
    ' is wondering if you could give me your thoughts on this.'
    ' is pontificating existence, and this.',
    ' would like to know what you think of this.',
    ' has a crazy idea.',
    ' had a crazy idea.',
    ' would like you to give a follow.',
    ' would like you to share this around.',
    ' would like you to RT this.',
    ' requires you to fap to this, or RT.',
    ' requires you to fap to this, or RT, choice is yours.',
    ' requests you clickity on that RT button!',
    ' thanks you for your viewership.',
    ' thanks you for being here.',
    ' thanks you for caring.',
    ' is thirsty.',
    ' is live streaming.',
    ' would like to extend his warmest thanks for watching!',
    ' would like you to watch the stream on Facebook Gaming.',
    ' is thinking about you.',
    ' is dreaming about you.',
    ' is wanting you... To watch his stream!',
    ' is a thicc slice of Streamer Pie.',
    ' is the thicc boi of Facebook Gaming!',
    ' can ride his bike with no handlebars.',
    ' cannot believe its not butter.',
    ' is alive and well, or something.',
    ' is live streaming on Facebook!',
    ' is live streaming on Facebook Gaming!',
    ' is streaming, live, now, on Facebook Gaming!',
    ' has no pants on.',
    ' has no pants on, as per the regulations of the No Pants Crew!',
    ' has no pants on, check the underdesk cam for proof! (theres no underdesk cam)',
    ' is secretly batman!',
    ' is ready for more gaming!',
    ' is live streaming!',
    ' is streaming.',
    ' is streaming on Facebook Gaming.',
    ' would like you to visit on Facebook Gaming.',
    ' wants you to visit his page on Facebook Gaming.',
    '...',
]

#########################################################################################################
# This block does NOT use the STREAMER_NAME variable at all in the generation, this is just a straight up
# random generation string. (Completed) with the reason of being stuff that should not be randomly generated.
# Basically this is for complete sentences that do not need the streamers name.
captions_to_use = [
    'Crazy times',
    'What up fam!',
    'Check this out fam',
    'What do you guys think?',
    'Is this the flavour of the month?',
    'Thoughts?',
    'Rip or Nah?',
    'Well fam, join me on stream!',
    'Remember to join me on stream!',
    'Remember I stream, so join me!',
    'Drop that follow here, and on stream!',
    'Hit that like and follow button fam!',
    'Captions tend to be random',
    'Sauce?',
    'Tarnations!',
    'Has this made you thirsty for me? It should!',
    'The No Pants Crew and I invite you to check this shit out!',
    'The No Pants Crew and I invite you to check this out!',
    'The No Pants Crew and I invite you to follow us on stream!',
    'The League of Extraordinarily Evil Gamers and I invite you to check this shit out!',
    'The League of Extraordinarily Evil Gamers and I invite you to check this out!',
    'The League of Extraordinarily Evil Gamers and I invite you to follow us on stream!',
    'Git-Sum',
    'Check it out!',
    'Check this out!',
    'Holy hell handbags!',
    'Well, would you look at that.',
    'Another banger!',
    'Absolute mayhem!',
    'Random Caption!',
    'Is that a challenge?',
    'I think that is a challenge.',
    'Caption this',
    'Do not forget to follow!',
    'If you like this, hit that RT and like button!',
    'RT this if you like it!',
    'Do not forget to like this post!',
    'Feedback people?',
    'I\'d like some feedback on this.',
    'Like, follow, subscribe to my page, see my profile for details!',
    'Follow, like, these things are important!',
    'Spread the word!',
    'Hit that RT button!'
    'Share me with your family and friends, awww yeee.',
    'Share me with your family and friends!',
    'Share me with your family, I am a treat!',
    'RT me to your grandma!'
    'What are your thoughts on this?',
    'Hey, what is your take on this?',
    'Fam, serious question, what do you think?',
    'Heresy, this is heresy!',
    'Exterminatus!',
    'I would like to know your opinion on this matter.',
    'Do tell me what you think.',
    'No Pants Crew through and Through!',
    'Founder of NPC reporting in!',
    'Fancy no pantsie!',
    'Blamsauce!',
    'Magic here!',
    'Continued success?',
    'Streaming games is fun!',
    'Streaming games is entertaining!',
    'Video game streaming!',
    'Successful streaming like whaaa!',
    'I am inevitable',
    'I am Iron Pan',
    'Pan, Cast-Iron, Pan.',
    'Is this where the zombie apocalypse starts?',
    'do do do do do... Do do!?',
    'Thank you for looking at this.',
    'Thanks be to you for your viewership!',
    'do dew do do',
    'Want some more?',
    'Would you like more?',
    'If you could, would you want more?',
    'More is better than less, would you like more?',
    'Your thoughts?',
    'What did you think of that?',
    'How about that?',
    'Emoji for your thoughts?',
    'What ya think of this?',
    'Ha!',
    'Follow me for more of this stuff, here, in this. Yeah.',
    'Follow me for more of this!',
    'Give a follow if you like what you see!',
    '[Hypnotoad Eyes] Follow Me, Share Me, subscribe to me [/Hypnotoad Eyes]',
    '[Hypnotoad Eyes] Follow Me, Share Me, subscribe to me [/Hypnotoad Eyes] What was that?',
    '[Hypnotoad Eyes] Follow Me, Share Me, subscribe to me [/Hypnotoad Eyes] Yussssss!',
    'I am just a click away from being followed, give that click, do it, do it do it do it!',
    'I am not wearing pants, or am I. No Pants Crew for Life!',
    'Guess what I was thinking.',
    'Do you know what I was thinking?',
    'Uhh, blamsauce?',
    'Blam to the sauce!',
    'Winner Winner drinking paint thinner!',
    'RT for clout!',
    'RT for prestige!',
    'Retweet for clout!',
    'Retweet for prestige!',
    'Oooh Shiny!',
    'Pizzazz!',
    '...',
    'I suggest recklessness!'
]

#########################################################################################################
# this is the easier way to generate strings for random messages. The messages above while working
# are not always the best bets. This method here is more 'creative' as they generate multiple methods
# of hilarity within the string. Depending how we sculpt this, we could have thousands of possibilities
# with minimal work.
# STREAMER_NAME + rand_1 + rand_2 + rand_3 + rand_4 = caption ?
rand_1 = [
    ' is',
    ' was',
    ' continues',
    ' continued',
    ' persists at',
    ' prevails at',
    ' is proficiently',
    ' cannot be'
    ' the badass is',
    ' the badass was',
    ' the badass continues',
    ' the true badass is',
    ' the simplord is',
    ' the simplord was',
    ' the badass simplord is',
    ' the badass simplord was',
    ' the badass simplord continues',
    ', the pimp, is',
    ', the simp, is',
    ', the pimp, was',
    ', the simp, was',
    '(NPC Founder) was',
    '(NPC Founder) is',
    '(NPC Founder) continues',
    '(NPC Founder) continued',
    '(LeeG Founder) was',
    '(LeeG Founder) is',
    '(LeeG Founder) continues',
    '(LeeG Founder) continued',
    '\'s is here, ',
    '\'s was here, '
]

rand_2 = [
    ' gaming',
    ' playing games',
    ' streaming games',
    ' winning games',
    ' streaming',
    ' playing',
    ' crushing',
    ' rocking',
    ' blasting'
    ' dominating',
    ' dominating it',
    ' winning',
    ' losing',
    ' crushing it',
    ' battling',
    ' winning it',
    ' playing it',
    ' rocking it'
]

rand_3 = [
    ' hardcore',
    ' advantageously'
    ', hardcore',
    ' hardcore porn style',
    ', masterfully',
    ' hardcore, 100% masterclass',
    ' masterfully',
    ' with masterclass style',
    ' with skill',
    ' with style',
    ' with clout',
    ' with the right stuff',
    ' with what it takes',
    ' exemplifying skill',
    ' with pizzazz',
    ' with might and main',
    ' exemplifying technique',
    ' famously',
    ' sensationally',
    ' awkwardly',
    ' badly',
    ' poorly',
    ' swimmingly',
    ' swimmingly well',
    ' seemingly well',
    ' well'
]

rand_4 = [
    '.',
    '.',
    '.',
    '.',
    '.',
    '.',
    '!',
    ', thoughts?',
    '?',
    '??',
    '!!',
    '..',
    ', maybe.',
    ', maybe!',
    ', maybe?',
    ', perhaps.',
    ', perhaps!',
    ', perhaps?',
    ', perhaps...',
    '...',
    ', maybe...',
    ', thoughts...',
    ', thoughts?!?',
    ', for your consideration.'
]

hashtag = [
    'LeeG',    'EvilGamers',    'LeagueOfEvil',    'NoPantsCrew',    'NPC',    'SimmyDizzle',
    'Vagabond',    'LiveStream',    'Streamer',    'Streaming',    'StreamClip',    'LiveClip',
    'Clipped',    'ClippedStream',    'Gamer',    'Gaming',    'FBGG',    'CanadianStreamer',
    'OhCanada',    'JusticeForJohnnyDepp',    'AmberTurd',    'CleverGirl',    'ItsClipTime',
    'Clipped',    'StreamingNow',    'NowStreaming',    'Live',    'LiveSimmy',    'FacebookGamer',
    'ClippedStream',    'ClippedLive',    'OldSchoolGamer',    'InstantReplay',    'Replay',
    'ActionReplay',    'HappeningNow',    'BreakingNews',    'Vagrant',    'WannaBe'    'GamerBoi',
    'Gamerboy',    'GamerBoyz',    'GameBoy',    'GameBoi',    'GamerGirl',    'GamerGirlWannabe',
    'Hero',    'SavedTheDay',    'MVP',    'SithLord',    'JediMaster',    'PabloEscobar',    'BadHabits',
    'Video',    'OneOfUs',    'LiveStreamFacebook',    'LiveStreamVideo',    'LiveStreamed',    'LiveStreamGamer',
    'LiveStreamVideoQueen',    'LiveStreamPro',    'GamingPro',    'GamerBro',    'LiveNow',    'StreamingLive',
    'StreamerJunkie',    'LiveStreamClip',    'SmallStreamer',    'GamingCommunity',    'Games',    'VideoGames',
    'FacebookGamingCommunity',    'FBGamer',    'LiveStreamingNow',    'StreamingLive',    'Live_Streaming_Now',
    'NotApache', 'ApexPredator', 'MagicJohnson', 'Fibre1', 'LiveOnFBGG'
]

Intro = [
    'News:',                    'Breaking News:',    'This just in:',    'Check it out:',    'Check this out:',
    'Totally not automated tweet:',    'Absolutely an automated tweet:',    'Not Seen on CNN:',    'Valuable content:',
    'Believe it or not',    'This just happened',    'Entertaining News:',    'Good news everbody:',    'Good news:',
    'Bad News everybody:',    'Bad news:',    'As seen on FBGG:',    'News of the Day:',    'Todays Headline:',
    'Announcement:',    'Reporting live:',    'Live Reporting:',    'Reporting:',    'Communiqué:',    'News Bulletin:',
    'Bulletin:',    'Message from above:',    'Message:',    'Statement:',    'Offical Statement:',    'Gossip:',
    'Rumour:',    'Exposé:',    'News Flash:', 'Press Release:', 'The Latest:'
]

###########################################################################################################
##                               CONFIGURATIONAL SETTINGS FOR THE TWEET                                  ##
###########################################################################################################

# CHANGE ME -- This is the folder where your new files will be scraped from!
PATHS = ['C:/Videos']       # Future

# Streamer-Name
STREAMER_NAME = "LiveSimmy"             #Put your streamername here

# Website-Name
WEBSITE_NAME = "https://fb.gg/livesimmy"

# do we want to use the 'random' phrases we generated below?
USE_PHRASES = False

# enabled for debugging purposes (True/False)
DEBUG_MODE = True

# tweepyControl (Disable this if you want to test thins without posting them to twitter)
# works best when DEBUG_MODE is enable and this is disabled (you'll see logs of things being
# detected/changed without posting to twitter)
TWEEPY_CONTROL = False

# do we want to use a series of Retweet bots to push our data out
# this should be disabled when you have a large following as it will
# get VERY spammy to those who follow you. Use with caution.
USE_RT = True

# Tumblr tags automatically assigned to the post
tags_to_use = ["LiveSimmy", "SimmyDizzle", "Streaming", "Streamer", "Games", "ok", "FacebookGaming", "FBGG",
               "Facebook", "LiveStream", "NextLevel", "video games", "video", "gaming", "Xbox", "XboxSeriesX",
               "HitLike", "Gamer", "Stream", "NowStreaming", "BreakingNews", "StreamingLive", "LiveStreamVideo",
               "GamingCommunity", "LiveNow", "SmallStreamer", "LiveStreamFacebook"]


# people we intend to @
handles_to_tag = [
        'CC_RTs', 'SmallStreamersR', 'SmallStreamersC', 'Ohficial92', 'MickeysTV_', 'APACHE_N4SIR',
        'LiveSimmy', 'WhirlingDerv', 'Uncletony92', 'FileBayInc', 'blackwolfz1', 'blusiren', 'NickkyTesla',
        'ScrappyReborn', 'Grantie_Tv'
    ]

###########################################################################################################

# Logger function, tracks the current time of the log-entry, and the log message so long as DEBUG_MODE is enabled.
# designed to allow for debugging purposes. Obviously we want to minimize all output to maintain minimal footprint.
def Logger(str):
    if DEBUG_MODE:
        print("{%s} %s" % (time.strftime("%Y-%m-%d %H:%M"), str))

# finding a string within a string? you got it dude!
# https://stackoverflow.com/questions/4154961/find-substring-in-string-but-only-if-whole-words
def string_found(string1, string2):
    if string1.find(string2) > 0:
        return True

    return False


###########################################################################################################
# Prostitute the mission, I mean, execute the script function.
if __name__ == '__main__':

    ###########################################################################################################
    # Consumer keys and access tokens, used for OAuth
    # you will need to generate these on tumblr.com

    Logger("--------------------------------------------------------------------------------")
    Logger("Loading credentials")
    with open('tumblr_credentials.json', 'r') as f:
        credentials = json.loads(f.read())
        client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_token_secret'])

    Logger("--------------------------------------------------------------------------------")
    Logger (json.dumps(client.info(), indent=4))
    Logger("--------------------------------------------------------------------------------")

    today = time.strftime("%Y-%m-%d %H:%M") # Year-Month-Day Hour:Minute

    currentDate = date.today()              # change the currentDate value

    # pick a random status
    x = random.randrange(0,30)

    # Set the stage for things to come (potentially)
    status = Intro[random.randrange(0, len(Intro)-1)] + " "

    try:
        # Randomly generate a status message, between this and a random caption this should cause
        # the services like tumblr and twitter from encountering issues with using the same message
        # more than once. Preventing their systems from blocking 'spam' (not that this is spam)
        # This fills the 'tweet' block, which is not-used unless you have your tumblr autoposting to your twitter
        # which does *NOT* always work. This is why IFTTT has been used in this.
        if(x == 0):
            status = status + "(" + today + ") " + STREAMER_NAME + " is live over on #FacebookGaming. \n\n" + WEBSITE_NAME
        elif(x==1):
            status = status + "(" + today + ") " + STREAMER_NAME + " is gaming over on " + WEBSITE_NAME + ".\n\n"
        elif(x==2):
            status = status + "(" + today + ") Visit " + STREAMER_NAME + ", currently streaming on @FacebookGaming. \n\n" + WEBSITE_NAME
        elif(x==3):
            status = status + "(" + today + ") Visit " + STREAMER_NAME + " over on #FacebookGaming. \n\n" + WEBSITE_NAME
        elif(x==6):
            status = status + "(" + today + ") Visit Big Daddy D on #FacebookGaming. \n\n" + WEBSITE_NAME
        elif(x==8):
            status = status + "(" + today + ") " + STREAMER_NAME + " on ze #FacebookGaming. \n\n" + WEBSITE_NAME
        elif(x==9):
            status = status + captions_to_use[random.randrange(0, len(captions_to_use)-1)]
        elif(x==12):
            status = captions_to_use[random.randrange(0, len(captions_to_use)-1)]
        elif(x==14):
            status = status + STREAMER_NAME + phrases[random.randrange(0, len(phrases)-1)]
        elif(x==16):
            status = STREAMER_NAME + phrases[random.randrange(0,len(phrases)-1)]
        elif(x==18):
            status = status + STREAMER_NAME + rand_1[random.randrange(0, len(rand_1)-1)] + rand_2[random.randrange(0,len(rand_2)-1)] + rand_3[random.randrange(0,len(rand_3)-1)] + rand_4[random.randrange(0,len(rand_3)-1)] + ' ' + "(" + today + ") "
        elif(x==20):
            status = STREAMER_NAME + rand_1[random.randrange(0, len(rand_1)-1)] + rand_2[random.randrange(0,len(rand_2)-1)] + rand_3[random.randrange(0,len(rand_3)-1)] + rand_4[random.randrange(0,len(rand_3)-1)] + ' ' + "(" + today + ") "
        elif(x==22):
            status = status + "(" + today + ") " + captions_to_use[random.randrange(0, len(captions_to_use)-1)]
        elif(x==23):
            status = status + "(" + today + ") " + STREAMER_NAME + phrases[random.randrange(0,len(phrases)-1)]
        elif(x==26):
            status = status + "(" + today + ") " + STREAMER_NAME + rand_1[random.randrange(0, len(rand_1)-1)] + rand_2[random.randrange(0,len(rand_2)-1)] + rand_3[random.randrange(0,len(rand_3)-1)] + rand_4[random.randrange(0,len(rand_3)-1)] + ' ' + "(" + today + ") "
        elif(x==29):
            status = status + "(" + today + ") Visit " + STREAMER_NAME + " over on #FacebookGaming. \n\n" + WEBSITE_NAME
        else:
            # Generate a new, tweet following a series of possible outcomes, a random string of joy
            names=["He","The Crew","SimmyDizzle","LiveSimmy", "Dave", "David", "Big Daddy D", "The OG Simmy D", "The true Canadian Zombie", "The Canadian",
                   "That Canadian Gamer", "That Facebook Streamer, LiveSimmy,", "The one and only LiveSimmy", "The Gaming Zombie, SimmyDizzle,", "Hip Streamer Dave",
                   "OG Daddy D", "OG LiveSimmy", "Entertainer, LiveSimmy", "Entertainer, SimmyDizzle", "Comedic Legend, LiveSimmy", "Comedy Legend, LiveSimmy",
                   "Comedy Legend, SimmyDizzle", "Comedic Legend, SimmyDizzle", "No Pants Crew Founder, SimmyDizzle,", "No Pants Crew Founder, LiveSimmy",
                   "Founder of League of Extraordinarily Evil Gamers, LiveSimmy","Founder of League of Extraordinarily Evil Gamers, SimmyDizzle",
                   "The powerful, LiveSimmy", "Super Seductive love master, SimmyDizzle", "Big Dick Energy, Little Dick Dave", "Papa Dave",
                   "Mr. LiveSimmy", "Mr. SimmyDizzle", "Old Man Dizzle", "PTSD Bombshell SimmyD", "Facebook Level up Streamer, LiveSimmy",
                   "LiveSimmy, master of baiting", "LiveSimmy baiter of the master", "B.A.M.F. LiveSimmy", "B.A.M.F. SimmyDizzle",
                   "Vagrant, LiveSimmy",
                   ]
            verbs=["was", "has", "has been", "have been", "is", "are", "were"]
            nouns=["playing a game", "streaming a game", "live streaming", "streaming live", "streaming on Facebook Gaming", "streaming on FBGG",
                   "watching devastation", "talking", "dancing", "speaking", "enduring combat", "battling", "ensuring victory", "rising to the challenge",
                   "winning", "victorious", "triumphant", "successful", "undefeated", "unvanquished", "randomly generated", "complete", "on a roll", "prospering", "flourishing",
                   "thriving", "vigorously clambering for the top", "clambering for the top", "aiming for the top", "entertaining", "vying for the win",
                   "vying for love", "hitting the spot", "trying hard", "struggling over this", "struggling with this", "undertaking gaming lessons", "streaming for you",
                   "streaming for the masses", "making the effort", "putting the work in", "endeavoring to be better", "vexing his enemies", "vexed his nemesis",
                   "completely lost his mind", "complete lost it"]
            ends=[".", "!", "..", "!!", "!!!", "..."]
            status = status + names[random.randrange(0,len(names)-1)]+" "+verbs[random.randrange(0,len(verbs)-1)]+" "+nouns[random.randrange(0,len(nouns)-1)] + ends[random.randrange(0, len(ends)-1)]

        # assign a random Hashtag to the end of the status
        status = status + "\n\n #" + hashtag[random.randrange(0, len(hashtag)-1)]

        # Status Length Check -- Add RT Bots here
        x = 0                                                                                                                                          
        while(x < len(handles_to_tag)-1):
            # 0,1,2 = automatically tagged so long as we are under 240 characters.
            if (x<3):
                if(len(status) < 240):
                    status = status + ' @' + handles_to_tag[x] + '\n'
                    x += 1
                    continue

            # under 260 characters, we attempt to select at random
            # if we will use person to tag.
            if(len(status) < 260):
                if(random.randrange(0,5) == 3):
                    status = status + ' @' + handles_to_tag[x] + '\n'
            #increment and continue
            x+=1
            continue;
            

        # assign the caption to use (for science)
        rx = random.randrange(0,3);
        if(rx == 0):
            the_caption = captions_to_use[random.randrange(0, len(captions_to_use)-1)]
        elif(rx == 1):
            the_caption = STREAMER_NAME + phrases[random.randrange(0, len(phrases)-1)]
        elif(rx == 2):
            the_caption = STREAMER_NAME + rand_1[random.randrange(0, len(rand_1)-1)] + rand_2[random.randrange(0,len(rand_2)-1)] + rand_3[random.randrange(0,len(rand_3)-1)] + rand_4[random.randrange(0,len(rand_3)-1)]
        else:
            the_caption = captions_to_use[random.randrange(0, len(captions_to_use)-1)]

        ####################################################################################################
        # add our website to the caption to link back to the OG content.
        the_caption = the_caption + ' (' + WEBSITE_NAME + ')'

        imagePath = PATHS[0] + '/Buffer Replay .mp4'       # get the image/video path

        # blank response is key
        response = '{}'

        if (string_found(imagePath, 'png') != False):
            Logger("Attempting to queue photo post:")
            response = client.create_photo('livesimmy.tumblr.com', state="published", tags=tags_to_use, caption=the_caption, tweet=status, data=imagePath)
        elif (string_found(imagePath, 'mp4') != False):
            Logger("Attempting to queue video post:")
            response = client.create_video('livesimmy.tumblr.com', state="published", tags=tags_to_use, caption=the_caption, tweet=status, data=imagePath)
        else:
            response = '{UNKNOWN TYPE PROVIDED - Skipping}'

        print("--------------------------------------------------------------------------------")

        # the state is in the response? It should read transcoding to be accurate.
        if "state" in response:
            Logger("File state: %s" % response['state'])
        elif "errors" in response:
            Logger("An error was encountered (details below), pushing the imagePath to the back of the array.")
            Logger(response['errors'])
            if "8009" in response['errors']:
                # 8009 is used when videos encounter an issue on upload.
                Logger('')
            elif "8011" in response['errors']:
                # error 8011 is when we have exceeded our daily quota for videos
                Logger('')
            else:
                Logger('')
                # Unnknown error state
        else:
            Logger("Unknown state has been reached, expect an exception below.");

        # Response should always be from tumblr
        Logger("JSON Response from Tumblr:")
        Logger(json.dumps(response, indent=4))

        Logger("--------------------------------------------------------------------------------")
    except Exception as e:
        Logger("Error occured:")
        Logger(e)


###########################################################################################################
#EOF
