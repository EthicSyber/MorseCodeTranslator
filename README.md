<img width="860" height="350" alt="ascii-text-art" src="https://github.com/user-attachments/assets/c4508d4a-e343-4018-bcf1-b3c15151ec04" />

This project was developed as an initial step to showcasing python skills and learning more about morse code. It does not use anything additional for download as it was developed without any extras (libraries/modules etc.). The current version of the project has a class that represents the translator to and from morse code [I will edit this out later, but I intend to update both the readme and the code to be more presentable at another time].

Below I add some background from Wikipedia on Morse Code and provided some project guidance as well as possible suggestions to get started with morse code to character mapping.

<a href=https://en.wikipedia.org/wiki/Morse_code>MORSE CODE</a>

<a href="https://en.wikipedia.org/wiki/Prosigns_for_Morse_code">MORSE CODE PROSIGN</a>


## WHAT IS MORSE CODE?

<b style='color:rgb(241, 147, 101)'>Morse Code</b> is a telecommunications method that encodes text in standardized sequences called <em>dits</em> and <em>dahs</em> (or dots and dashes). This encoding scheme was named after <span style='color:skyblue'><strong>Samuel Morse</strong></span>, one of the early developers of the system adopted for electrical telegraphy. It is usually transmitted by on-off keying using a medium such as electric current, radio waves, visible light, or sound waves. This wave (or current) is present during the time period of the dit/dah and absent during the time between them (wikipedia. 2025). 


<b>Samuel Finley Breese Morse</b>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Samuel_Morse_portrait.tiff/lossless-page1-500px-Samuel_Morse_portrait.tiff.png" width=350px, height=450px>

Date: 1866 (wikipedia. 2025)

## MORSE CHART

<img style="background-color: white" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Morse_comparison.svg/960px-Morse_comparison.svg.png" width=500px, hieght=800px>

## REQ-GUIDE
* There is <strong>no distinction</strong> between <em>upper and lowercase letters</em>.
* Each code symbol forms a sequence of dits and dahs (duration can vary).
* The duration of a dah is three times the duration of a dit. 
* Each encoded character is followed by a period of signal absence (or space) equal to the dit duration.
* Letters of a word are separated by a duration equal to three dits.
* Words are separated by a space equal to seven dits.

## STARTING SUGGESTIONS
<pre>
1. Python Dictionary | json : using a key=val pair distinct - letter (key) and code (value) for translation
example (recommend string sequence instead of below i.e., '....   .   ---   ---'): 
international = {
    "A": "■ ■■■", 
    "B": "■■■ ■ ■ ■", 
    "C": "■■■ ■ ■■■ ■", 
    "D": "■■■ ■ ■",
    etc..
}

2. Lists and/or tuples: for every item in a list it has a corresponding item in another (the method zip() could be used for this)
example (using string sequence):
morse = [". -", "- . . .", "- . - .", "- . ."]
letter = ["A", "B", "C", "D"]
codebook = list(zip(letter, morse))
result >>> [('A', '. -'), ('B', '- . . .'), ('C', '- . - .'), ('D', '- . .')]
</pre>
