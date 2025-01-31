import requests
import time
import os

README = """<img src="/banner2.png">

<h1 align="center">Hi, I'm Natya Vidhan Biswas AKA Studious Gmaer</h1>
<h3 align="center">A 15-year-old Software, Web and Game Developer from India</h3>

<p align="center"> <a href="https://github.com/studiousgamer/"><img src="https://github-profile-trophy.vercel.app/?username=studiousgamer&theme=darkhub&margin-w=15&margin-h=15&column=7" alt="studiousgamer" /></a> </p>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://dev.to/studiousgamer" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/devto.svg" alt="studiousgamer" height="30" width="40" /></a>
<a href="https://twitter.com/gamerstudious" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="gamerstudious" height="30" width="40" /></a>
<a href="https://linkedin.com/in/natya-vidhan-biswas-741310189" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="natya-vidhan-biswas" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/13450690" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="13450690" height="30" width="40" /></a>
<a href="https://instagram.com/natyavidhan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="natyavidhan" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.electronjs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/electron/electron-original.svg" alt="electron" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://firebase.google.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/firebase/firebase-icon.svg" alt="firebase" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.qt.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="qt" width="40" height="40"/> </a> </p>


### GitHub Stats:

<a href="https://github.com/studiousgamer">
  <img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=studiousgamer&hide=html,css&title_color=ffffff&text_color=c9cacc&icon_color=2bbc8a&bg_color=1d1f21&langs_count=3" />
</a>
<a href="https://github.com/studiousgamer">
  <img align="center" src="https://github-readme-stats.vercel.app/api?username=studiousgamer&show_icons=true&line_height=27&count_private=true&title_color=ffffff&text_color=c9cacc&icon_color=2bbc8a&bg_color=1d1f21" alt="Martin's GitHub Stats" />
</a>

<a href="https://github.com/studiousgamer/ASCII-fy">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=studiousgamer&repo=ASCII-fy&title_color=ffffff&text_color=c9cacc&icon_color=2bbc8a&bg_color=1d1f21" />
</a>


<a href="https://github.com/tyro-inc/tyro-engine">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=tyro-inc&repo=tyro-engine&title_color=ffffff&text_color=c9cacc&icon_color=2bbc8a&bg_color=1d1f21" />
</a>  <br>

"""
    
    
def get_current_track():
    data = requests.get("https://api.lanyard.rest/v1/users/579320358063046682").json()
    is_playing = data['data']['listening_to_spotify']
    if is_playing:
        current_track_info = {
            "id": data['data']['spotify']['track_id'],
            "track_name": data['data']['spotify']['song'],
            "artists": data['data']['spotify']['artist'],
            "link": "https://open.spotify.com/album/" + data['data']['spotify']['track_id'],
            "is_playing": is_playing
        }
    else:
        current_track_info = {
            "is_playing": is_playing
        }

    return current_track_info

def updateRepo(link, music):
    edited = README + link
    open("README.md", 'w').write(edited)
    os.system(f"git add README.md")
    os.system(f'git commit -m "Listening To: {music}"')
    os.system(f"git push origin master")

def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track()
        if current_track_info['is_playing'] == True:
            if current_track_info['id'] != current_track_id:
                current_track_id = current_track_info['id']
                link = f"\n<h2>Listening To: <a href='{current_track_info['link']}'>{current_track_info['track_name']}, By {current_track_info['artists']}</a></h2>"
                try:
                    updateRepo(link, current_track_info['track_name'])
                except Exception as e:
                    print(e)
                    pass
                os.system("cls")
                print(
f"""
Now Playing:
Name: {current_track_info['track_name']}
Artist: {current_track_info['artists']}
Link: {current_track_info['link']}
"""
)
        else:
            if current_track_id != None:
                current_track_id = None
                link = f"\n<h2>Listening To: Nothing</h2>"
                os.system("cls")
                print("Playing Nothing")
                updateRepo(link, "Nothing")
                
        time.sleep(1)


if __name__ == '__main__':
    main()
    # get_current_track()
