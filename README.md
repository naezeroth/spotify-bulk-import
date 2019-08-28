# spotify-bulk-import
This script reads the ID3 tag of a music file and adds it to your designated spotify playlist by querying it and then adding it.

Steps:
1. Create a playlist on Spotify and note down the playlist ID (the unique URL on your playlist) - if you do this on the web, this would be the url following open.spotify.com/playlist/
2. Create an app on spotify developer and note down your client ID, client secret. Add a redirect URL as http://localhost/ - you can find this here: https://developer.spotify.com/dashboard
3. Add the client ID, client secret, and playlist ID to your .env file.
4. Install dependencies by pip install < requirements.txt 
5. Run the script in the location of your music files. 
6. Files with the correct data will be added to the spotify playlist you chose. 
