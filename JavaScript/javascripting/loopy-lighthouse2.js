function loopyLighthouse(range, multiples, words){
  var lowerlimit = range[0];
  var upperlimit = range[1];
  var multipleA = multiples[0];
  var multipleB = multiples[1];
  var firstWord = words[0];
  var secondWord = words[1];


  for (var i = lowerlimit; i <= upperlimit; i++) {

    // First exception: i is a multiple of A and not B
    if ((i % multipleA === 0) & (i % multipleB !== 0)) {
      console.log(firstWord);
    }
    // Second exception: i is a multiple of B and not 4
    else if ((i % multipleA !== 0) & (i % multipleB === 0)) {
      console.log(secondWord);
    }
    // Third exception: i is a multiple of both A and B
    else if ((i % multipleA === 0) & (i % multipleB === 0)) {
      console.log(firstWord + secondWord);
    }
    else {
      console.log(i);
    }
  }
}