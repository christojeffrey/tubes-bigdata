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
    print('Parsing ' + filename)
    file = open('raw_json/' + filename, 'r')
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
            for data in typename:
                DATE = data['created_at']
                # PARSE 1644900422 TO 2021-03-01
                DATE = datetime.datetime.fromtimestamp(DATE).strftime('%Y-%m-%d')
                

