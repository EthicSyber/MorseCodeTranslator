# MORSE CODE TRANSMITTER NOTES

<a href=https://en.wikipedia.org/wiki/Morse_code>MORSE CODE WIKI</a>

<a href="https://en.wikipedia.org/wiki/Prosigns_for_Morse_code">MORSE PROSIGN WIKI</a>


## WHAT IS MORSE CODE?


<b style='color:rgb(241, 147, 101)'>Morse Code</b> is a telecommunications method that encodes text in standardized sequences called <em>dits</em> and <em>dahs</em> (or dots and dashes). This encoding scheme was named after <span style='color:skyblue'><strong>Samuel Morse</strong></span>, one of the early developers of the system adopted for electrical telegraphy. It is usually transmitted by on-off keying using a medium such as electric current, radio waves, visible light, or sound waves. This wave (or current) is present during the time period of the dit/dah and absent during the time between them (wikipedia. 2025). 


Samuel Finley Breese Morse 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Samuel_Morse_portrait.tiff/lossless-page1-500px-Samuel_Morse_portrait.tiff.png" width=200px, height=300px>

Date: 1866 (wikipedia)

## MORSE CHART

<img style="background-color: white" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Morse_comparison.svg/960px-Morse_comparison.svg.png" width=500px, hieght=800px>

## REQUIREMENTS GUIDE
* There is <strong>no distinction</strong> between <em>upper and lowercase letters</em>.
* Each code symbol forms a sequence of dits and dahs (duration can vary).
* The duration of a dah is three times the duration of a dit. 
* Each encoded character is followed by a period of signal absence (or space) equal to the dit duration.
* Letters of a word are separated by a duration equal to three dits.
* Words are separated by a space equal to seven dits.

## Suggestions to Start
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
