import sys
sys.path.insert(0, 'osanddatetime.mod')
import datetime
import os
import json

# anaktester_go(error), byu.id, gridoto_news, facebook_post, instagram_comment, instagram_media, instagram_post, instagram_status, myxl, telkomsel, twitter_status, youtube_comment, youtube_video

starting_filenames = ['anaktester_go(error)', 'byu.id', 'gridoto_news', 'facebook_post', 'instagram_comment', 'instagram_media', 'instagram_post', 'instagram_status', 'myxl', 'telkomsel', 'twitter_status', 'youtube_comment', 'youtube_video']

filenames = []
# get all files in directory raw_json
for filename in os.listdir('raw_json'):
    if filename.endswith('.json'):
        filenames.append(filename)


# social_media, date, count

# Proses agregasi menggunakan social media dan timestamp yang dinormalisasi jadi perhari sebagai acuan agregasi, serta count adalah jumlah post/komentar pada dari social media yang masuk ke acuan tersebut

# start parsing
for filename in filenames:
    # open file
    file = open('raw_json/' + filename, 'r', encoding='utf-8')
    # check the filename contains in starting_filename
    # if not, skip the file
    files_starting_filename = ''
    for starting_filename in starting_filenames:
        if starting_filename in filename:
            files_starting_filename = starting_filename
            break
    if files_starting_filename == '':
        continue
    
    # read file as dictionary
    data = json.load(file)

    # conditionally parse for each social media (same as starting_filenames)

    # byu.id
    if files_starting_filename == 'byu.id':
        SOCIAL_MEDIA = 'byu.id'
        typenames = data['GraphImages']
        for typename in typenames:
            DATE = typename['taken_at_timestamp']
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
            for data in typename["comments"]["data"]:
                DATE = data['created_at']
                # PARSE 1644900422 TO 2021-03-01
                DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
                print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # gridoto_news
    elif files_starting_filename == 'gridoto_news':
        SOCIAL_MEDIA = 'gridoto_news'
        typenames = data['GraphImages']
        for typename in typenames:
            DATE = typename['taken_at_timestamp']
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
            for data in typename["comments"]["data"]:
                DATE = data['created_at']
                # PARSE 1644900422 TO 2021-03-01
                DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
                print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # facebook_post
    elif files_starting_filename == 'facebook_post':
        SOCIAL_MEDIA = 'facebook_post'
        for datum in data:
            for comments in datum['comments']['data']:
                DATE = comments['created_time']
                # PARSE 2021-03-01T04:00:00+0000 TO 2021-03-01
                DATE = DATE.split('T')[0]
                print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # instagram_comment
    elif files_starting_filename == 'instagram_comment':
        SOCIAL_MEDIA = 'instagram_comment'
        for datum in data:
            DATE = int(datum['created_time'])
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # instagram_media
    elif files_starting_filename == 'instagram_media':
        SOCIAL_MEDIA = 'instagram_media'
        for datum in data:
            DATE = int(datum['created_time'])
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            COUNT = str(1 + datum["comment"]["count"])
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + COUNT)
    # instagram_post
    elif files_starting_filename == 'instagram_post':
        SOCIAL_MEDIA = 'instagram_post'
        for datum in data:
            DATE = int(datum['created_time'])
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            COUNT =str(1 + datum["comment"]["count"])
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + COUNT)

    # instagram_status
    elif files_starting_filename == 'instagram_status':
        SOCIAL_MEDIA = 'instagram_status'
        for datum in data:
            DATE = int(datum['created_time'])
            # PARSE 1644900422 TO 2021-03-01
            DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
            COUNT = str(1 + datum["comment"]["count"])
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + COUNT)
    # myxl
    elif files_starting_filename == 'myxl':
        SOCIAL_MEDIA = 'myxl'
        data = data['GraphImages']
        for datum in data:
            comments = datum['comments']['data']
            for comment in comments:
                DATE = int(comment['created_at'])
                # PARSE 1644900422 TO 2021-03-01
                DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
                print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # telkomsel
    elif files_starting_filename == 'telkomsel':
        SOCIAL_MEDIA = 'telkomsel'
        data = data['GraphImages']
        for datum in data:
            comments = datum['comments']['data']
            for comment in comments:
                DATE = int(comment['created_at'])
                # PARSE 1644900422 TO 2021-03-01
                DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
                print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # twitter_status
    elif files_starting_filename == 'twitter_status':
        SOCIAL_MEDIA = 'twitter_status'
        for datum in data:
            DATE = datum['created_at']
            # Fri Jan 01 05:03:05 +0000 2021 parse to 2021-01-01
            DATE = DATE.split(' ')[5] + '-' + DATE.split(' ')[1] + '-' + DATE.split(' ')[2]
            DATE = datetime.datetime.strptime(DATE, '%Y-%b-%d').strftime('%Y-%m-%d')

            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')



        pass
    # youtube_comment
    elif files_starting_filename == 'youtube_comment':
        SOCIAL_MEDIA = 'youtube_comment'
        for datum in data:
            # if doesn't have publishedAt, then skip
            if 'publishedAt' not in datum['snippet']:
                continue
            DATE = datum['snippet']['publishedAt']
            # PARSE 2021-03-01T04:00:00.000Z TO 2021-03-01
            DATE = DATE.split('T')[0]
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
    # youtube_video
    elif files_starting_filename == 'youtube_video':
        SOCIAL_MEDIA = 'youtube_video'
        for datum in data:
            # if doesn't have publishedAt, then skip
            if 'publishedAt' not in datum['snippet']:
                continue
            DATE = datum['snippet']['publishedAt']
            # PARSE 2021-03-01T04:00:00.000Z TO 2021-03-01
            DATE = DATE.split('T')[0]
            print(SOCIAL_MEDIA + '\t' + DATE + '\t' + '1')
