"""
A script that can download all the albums from an user.
"""
import facebook
import os	# path.exists, makedirs
import sys	# exit

root_dir = './output'
if not os.path.exists(root_dir):
	os.makedirs(root_dir)
if not os.listdir(root_dir):
	print('"{}" is not empty!'.format(root_dir))
	sys.exit()


# Get a temporary token here: https://developers.facebook.com/tools/explorer/
access_token = 'EAACEdEose0cBANRZBm1CDAPA5ni3RAOhpD0gIVmhiMEZAG01zF4irLfugr6iSotdr0qrRQjh1VuNmA0UT0sN7TVYwZAT9IIhhh2FrZBeFLaF1UiHgDwg9lcrUFZAQnSi5dbJI34LWsFletBRKtcPtXVSaoq1WSWvfDNjQVLcxzQZDZD'

def get_album_ids(g, uid):
	"""Retrieve all the album IDs an user have."""
	album_list = []

	conn_name = 'albums'
	while True:
		# Retrieve and parse the album IDs.
		albums = g.get_connections(id=uid, connection_name=conn_name)
		for album in albums['data']:
			album_list.append(album['id'])

		# Continue the loop if next page exists.
		if 'next' in albums['paging']:
			next_cursor = albums['paging']['cursors']['after']
			conn_name = 'albums?after={}'.format(next_cursor)
		else:
			break

	return album_list

def get_album_name(g, aid):
	"""Get the name of the album according to the album ID."""
	pass

def get_photo_ids(g, aid):
	"""Retrieve all the photo IDs in a specified album."""
	photo_list = []

	conn_name = 'photos'
	while True:
		# Retrieve and parse the album IDs.
		photos = graph.get_connections(id=aid, connection_name=conn_name)
		for photo in photos['data']:
			photo_list.append(photo['id'])

		# Continue the loop if next page exists.
		if 'next' in photos['paging']:
			next_cursor = photos['paging']['cursors']['after']
			conn_name = 'photos?after={}'.format(next_cursor)
		else:
			break

	return photo_list

def get_photo_detail(g, pid):
	"""Retrieve the download link and description of a photo."""
	pass

if __name__ == '__main__':
	graph = facebook.GraphAPI(access_token)

	album_list = get_album_ids(graph, 'me')
	n_album = len(album_list)
	print('{} album{} found...'.format(n_album, 's' if n_album > 1 else ''))

	for aid in album_list:
		photo_list = get_photo_ids(graph, aid)
		aname = get_album_name(graph, aid)
		print('ALBUM [{}]'.format(aid))

		# Create a folder for the album.
		apath = os.path.join(rootdir, )
		if not os.path.exists(aname):
			os.makedirs(aname)
		for pid in photo_list:
			print('.. {}'.format(pid))

		n_photo = len(photo_list)
		print('{} photo{} saved...'.format(n_photo, 's' if n_photo > 1 else ''))
