# spotify-bulk-import
This script reads the ID3 tag of a music file and adds it to your designated spotify playlist by querying it and then adding it.

Steps:
1. Create a playlist on Spotify and note down the playlist ID (the unique URL on your playlist) - if you do this on the web, this would be the url following open.spotify.com/playlist/ 

![image](https://user-images.githubusercontent.com/43486117/131785744-f2fe91a0-43c0-49f7-b8ab-e4fc18a91f4c.png)

2. Head to https://developer.spotify.com/dashboard/ and login and "create an app". Note down client ID, client secret. Click settings and add website and redirect as "http://localhost/" 


![image](https://user-images.githubusercontent.com/43486117/131785681-47de60ee-f858-475e-8618-4a44bc86c6a9.png)


3. Extract the .env, spotify.py and requirements.txt into the directory with all the music.
4. Edit .env with your playlist ID, client ID and client secret. 
5. Create a virtual environment for python by doing "virtualenv venv", if you don't have this installed please install by "apt-get install python3-venv"
6. Then pip install -r requirements.txt 
7. Run "python spotify.py YOUR_USERNAME" 
8. Open link provided in prompt in browser and login and authorize app. 
9. Copy and paste the URL that you're redirected to into the command prompt. i.e. "http://localhost/?code=AQCSrcYT4Aqnh-DSetAZ9714L9UDX38kwYGIBiAEPP_eNqFHaqY7hqz0QH8wMYqARGiLwo781KNn8zJA2y5UjtzwXsaiqVZTAgxYJgK-B9m0rGeqRnf6l1AwE15yLE4NAZp-Aq--akKCKaiHTTFCD0uRWsogttrnAUp-pVZUGUyoGZPTgEx0tkIdca6jM4wc9r4ZtLGeXO1WqaBLPDIp"

![image](https://user-images.githubusercontent.com/43486117/131786010-af3be217-2759-439a-976b-efa70f676194.png)
Don't worry if it looks like this. Simply copy and paste that URL into your terminal. 
![image](https://user-images.githubusercontent.com/43486117/131786170-6c53d2fb-8249-41ad-a67d-92e4070ee9d6.png)

10. Type "deactivate" to get out of virtual environment. 
11. Files with the correct data will be added to the spotify playlist you chose. 
