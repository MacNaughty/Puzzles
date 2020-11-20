// Start with a for-loop from 100 to 200 (inclusive)
for (var i = 100; i <= 200; i++) {

  // First exception: i is a multiple of 3 and not 4
  if ((i % 3 === 0) & (i % 4 !== 0)) {
    console.log("Loopy");
  }
  // Second exception: i is a multiple of 4 and not 3
  else if ((i % 3 !== 0) & (i % 4 === 0)) {
    console.log("Lighthouse");
  }
  // Third exception: i is a multiple of both 3 and 4
  else if ((i % 3 === 0) & (i % 4 === 0)) {
    console.log("LoopyLighthouse");
  }
  else {
    console.log(i);
  }
}
