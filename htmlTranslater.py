import os
import mtranslate
from bs4 import BeautifulSoup

#This code translate html file to another language.
#Html file should be in your local device.
#It can translate multiple file.

def Translater(folder): #Write html file direction ex: <C:/My Web Sites>
    for top,top_down,inside in os.walk(folder):
        os.chdir(top)
        for file in inside:
            if file.endswith("html"):
                #It is going to read your HTML file.
                with open(file, "r", encoding="utf-8") as f:
                    html = f.read()
                    soup = BeautifulSoup(html, "html.parser")
                    tags = soup.find_all(
                        ['h1', 'h2', 'h3', 'h4', 'p', "a", "svg", "span", "strong", "button", 'title'])
                    for tag in tags:
                        text = tag.get_text()
                        if tag.string is not None:
                            translated_text = mtranslate.translate(text, "en") #Write target language.
                            tag.string.replace_with(translated_text)

                    # Write the translated HTML to a new file or you can use the same file.
                    with open(file, "w", encoding="utf-8") as f:
                        f.write(str(soup))
