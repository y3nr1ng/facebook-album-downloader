"""
A script that can download all the albums from an user.
"""
import facebook
import requests

root_dir = '.'

# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBAOFWCxDc0O1mSbiwAQ8QVR3Tv5KcgMlAc6ToyO7vi7CvT6FmwBy5YZAZBVVmDCBuQzebpxgkinFhZB28SGO1yOPZAZByPyJZCABM2eMo2mN1g81eZBDAhP7xFcg3rAkgqierM6w6ZCjClOYhdZBZA0lSvgttEHu6ZBrZBwZDZD'

graph = facebook.GraphAPI(access_token)

album_list = []

# Extracting album list.
has_album = True
next = None
while has_album:
	# Concat the cursor if exists.
	if next:
		conn = 'albums?after={}'.format(next)
	else:
		conn = 'albums'
	
	# Retrieve and parse the IDs.
	albums = graph.get_connections(id='me', connection_name=conn)
	for album in albums['data']:
		album_list.append(album['id'])

	# Identify pagination item.
	if 'next' in albums['paging']:
		next = albums['paging']['cursors']['after']
	else:
		has_album = False
		next = None

n_album = len(album_list)
if n_album > 1:
	postfix = ''
else:
	postfix = 's'
print('{} album{} to retrieve...'.format(n_album, postfix))

# Iterate through the albums.
for id in album_list:
	photos = graph.get_connections(id=str(id), connection_name='photos')
	print(photos)	
