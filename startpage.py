import re
"""
The variables that you are meant to change are those that are defined in the first block here before the function definitions.
Note that this is just plaintext that gets inserted into the string below. It's not elegant, but it works. 
That also means that you can somewhat style some of these strings by entering them with valid HTML syntax should you want to do so.
"""
TabTitle='Startpage'                                    # The title that the tab will have in your Browser.
TitleText='Startpage template...'                       # The title that the window will have. 
SubText='Have a nice day.'                              # The text that is displayed in the small area below the title.
# Note that if you want to use a Windows path for the following, you either need to escape every backslash (\\) or use a raw string (r''). Use normal slashes on Linux.
importPath=r'pathTo\content.txt'                        # Where to find the file with the site data.
outputPath=r"pathTo\index.html"                         # Where to place the index.html output file. If you change this you either need to change others paths in the css too or add resources as a subfolder to that directory.
hourOffset=0                                            # Apply permanent offset to clock. For more information look into readme.


def importContent():
    with open(importPath,"r") as file:
        return file.read()
    

def parseContents(contents):
    while contents[0]=='\n':
        contents=contents[1:]
    while contents[-1]=='\n':
        contents=contents[:-1]
    contents=re.sub('\n{3,}','\n\n',contents)
    contents=contents.split('\n\n')
    return [x.split('\n') for x in contents]
    
def makeDoc(data):
    with open(outputPath,'w') as file:
        page='''<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>'''+TabTitle+'''</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="main.css">
<body>
    <div class="bg-image"></div>
    <div class="window-bg">
        <div class="front-img"></div>
        <div class="titlediv">
            <div id=titleb>'''+TitleText+'''</div>
            <div id="clock"></div>
        </div>
        <div class="windowbackgroundarea1"><div id="Subtitle">'''+SubText+'''</div></div>
        <div class="windowbackgroundarea2">
        <div class="centerDivs">
            <div class="category">
'''
        for category in data:
            page+='                <div class="categorytitle">'+category[0]+'</div>\n'
            page+='                <div class="categorycontent">'
            linelength=0
            for entry in category[1:]:
                name,link=entry.split(' | ')
                linelength+=len(name)+3
                if linelength>50:
                    page=page[:-3]+'</div><div class="categorycontent">'
                    page+='<a href="'+link+'">'+name+'</a> - '
                    linelength=len(name)
                else:
                    page+='<a href="'+link+'">'+name+'</a> - '
            if page[-3:]==' - ':
                page=page[:-3]+'</div>\n'
            else:
                page+='</div>\n'
        page+='''            </div>
        </div>
        </div>
    </div>
    <div class="pixeloverlay"></div>
    <div class="vignette"></div>
    <script>
        var clock=document.getElementById("clock");
        function updateClock(){
            var date=new Date();
            date.setHours(date.getHours()+'''+str(hourOffset)+''')
            var hours = date.getHours().toString();
            var minutes = date.getMinutes().toString();
            var seconds = date.getSeconds().toString();
            if (hours.length==1){
                hours="0"+hours
            }
            if (minutes.length==1){
                minutes="0"+minutes
            }
            if (seconds.length==1){
                seconds="0"+seconds
            }
            clock.innerHTML=hours+":"+minutes+":"+seconds;
        }
        updateClock();
        setInterval(updateClock,1000);
    </script>
    </body>
    </html>'''
        file.write(page)

if __name__=="__main__":
    print('Importing data...',end="")
    data=importContent()
    print('Done.\nParsing data from import file...',end='')
    data=parseContents(data)
    print('Done.\nCreating HTML startpage...',end='')
    makeDoc(data)
    print('Done.')
    print('Finished. New startpage has been created.')
