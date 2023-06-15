This repository is for encoding text and decoding text. The file sus.py is a python file which shows a gui using tkinter which allows someone to encode text and also decode it.
To use it, import tkinter using pip in terminal.
How it works:
It works by showing two buttons, encode and decode. Pressing either buttons opens up a new window.
Pressing the encode button will open up a window where you have to enter the text you want to encode and then press the button encode and it will show the encoded text.
The window shown after pressing the decode button works the same way as encode except it decodes the text encoded by encode. The scrolledtextwidget in encode is a global variable and the function,sus(), takes the input from the widget and encodes it. The output widget is also a global variable which allows the function to insert and show the encoded text to the user. The decode function works exactly the same way but it does the opposite to encode.
The best part about this is that you can edit how you want your text to be encoded.
There is a extremely big dictionary in the function sus(),you can go and edit the key-value pairs so that you can have your own custom encoding.
Just remember that the changes you make to the dictionary in sus(),you also have to change the key-value pairs in sussybaka() or else you won't be able to decode your text and 
you will have a error.
