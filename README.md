<h1>String Comparison Algorithm</h1>

<h2>A (let's hope) quick and simple algorithm that compares 2 strings and returns the % of how similar they are</h2>
<img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg"> 
<img src="https://forthebadge.com/images/badges/made-with-python.svg">
<img src="https://forthebadge.com/images/badges/powered-by-black-magic.svg">
<img src="https://forthebadge.com/images/badges/fo-real.svg">
<img src="https://forthebadge.com/images/badges/certified-cousin-terio.svg">
<h2>How it works:</h2>

This is the first string, it's a very simple string and has nothing special

This is the second string, it's a very simple string as well and has nothing special

->  The string scoring system takes all the KEY words and compares each and every one of the first with each and 
    every one of the second

Example :

(Removes some unecessary words such as "this, or, beacause, thing, is, the")

KEY WORDS (string1) : first string very simple string nothing special

KEY WORDS (string2) : second string very simple string well nothing special

Which of the 2 has more words? : --strring2-- with --8-- words

so the score is 6/8 so 75% similar 

HOWEVER:
-this algorithm needs to be trained so we can figure out the perfect % to assign as a suitable similarity value

-this algorithm compares the words between each other one after another and not each and every one of the first with each and every word of the second


<h2>TODO :</h2>

- [x] Currently the function "keythis" does not work 100%, needs a remake (WORKS)
- [ ] The algorithm works 100% but it compares the words between individually alligned, must be changed
