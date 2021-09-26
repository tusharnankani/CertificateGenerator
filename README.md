<!-- <p align="center">
  <b>Certificate Generator</b>
</p> -->
<br><br>
<p align="center">
  <img width ="70%" src="https://user-images.githubusercontent.com/61280281/134729891-673ca940-13dd-4c51-8597-ee576267d374.png">
</p>
<br>
<p align="center"> A simple mass certificate generator script for the community ⚡ </p>

<p align="center">
  <br>
  <a href="main.py">Source Code</a> &nbsp; · &nbsp; 
  <a href="#docs">Docs</a> &nbsp; · &nbsp;
  <a href="https://raw.githubusercontent.com/tusharnankani/CertificateGenerator/main/main.py">Raw Script</a>
  <br>
</p>
<br>


### Docs

All you need

- Certificate
  - Design a [simple template](template.png) on [Canva](https://www.canva.com/)
- Font
  - A .ttf (True-Type Font) file like [this](/font), can simply be downloaded from [here](https://www.google.com/search?q=download+.ttf+fonts).
- Names
  - Finally, a list of names in a .txt format or a .csv format.

<br>

### Pillow module

Using the [pillow module](https://pypi.org/project/Pillow/) to make changes.
<br>

- Calculating and declaring default values.


```python
from PIL import Image, ImageFont, ImageDraw

'''Global Variables'''
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size
```

<br>

- Placing the name on the certificate and saving to a different directory.

```python
def make_certificates(name):
    '''Function to save certificates as a .png file
    Finding the width and height of the text. 
    Placing it in the center, then making some adjustments.
    Saving the certificates in a different directory.
    '''
    
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)
    
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

```

<br>

### Names

- Using `readlines()` method with a `.txt` format.

```python
names = []

with open('names.txt') as f:
    content = f.readlines()
    for item in content:
        names.append(item[:-1].title())
```
<br>

- Using [pandas to read a `.csv` file](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

```python
import pandas
names = pandas.read_csv('names.csv', sep='#')
```

<br>

### Script in action

<br>

Template | Result
--- | ---
<img src="template.png"> | <img src="out/Tushar Nankani.png">

Design Courtesy [@GauravRaj](https://www.instagram.com/gauravraj0510)

<br>

### Future Scope?

- More customisations
- Directly e-mail as certificates are generated
- A web interface?

<br><br>

#### Author

[Tushar Nankani](https://tusharnankani.github.io/about/)

