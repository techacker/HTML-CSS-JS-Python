// Article: https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/

//Method 1
// Title Case a Sentence With a FOR Loop
function titleCase(str) {
    str = str.toLowerCase().split(' ');
    for (var i = 0; i < str.length; i++) {
      str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
    }
    return str.join(' ');
  }
  titleCase("I'm a little tea pot");


// Method 2
// Title Case a Sentence With the map() Method

function titleCase(str) {
    return str.toLowerCase().split(' ').map(function(word) {
      return (word.charAt(0).toUpperCase() + word.slice(1));
    }).join(' ');
  }
  titleCase("I'm a little tea pot");


// Method 3
// Title Case a Sentence With the map() and the replace() Methods

function titleCase(str) {
    return str.toLowerCase().split(' ').map(function(word) {
      return word.replace(word[0], word[0].toUpperCase());
    }).join(' ');
  }
  titleCase("I'm a little tea pot");

