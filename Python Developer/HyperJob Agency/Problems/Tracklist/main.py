def tracklist(**kwargs):
    for group in kwargs:
        print(group)
        for album in kwargs[group]:
            print('ALBUM:', album, 'TRACK:', kwargs[group][album])


# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love"})