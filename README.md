# spotify-bulk-import
This script reads the ID3 tag of a music file and adds it to your designated spotify playlist by querying it and then adding it.

Steps:
1. Create a playlist on Spotify and note down the playlist ID (the unique URL on your playlist)
2. Create an app on spotify developer and note down your client ID, client secret. Add a redirect URL as http://localhost/
3. Add the notes to your .env file.
4. Run the script in the location of your music files. 
5. Install dependencies by pip install < requirements.txt
6. Intact files with ID3 values will then appear in your spotify playlist. 

