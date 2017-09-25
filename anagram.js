// Check if 2 words are anagrams

/**
 * Returns `true` iff `word1` is an anagram of `word2`.
 */
function checkAnagram(word1, word2) {
  // check non-existence
  if (word1 === null || word1 === undefined || word2 === null || word2 ===
    undefined) {
    return false;
  }

  // anagrams must be the same length
  if (word1.length !== word2.length) {
    return false;
  }

  // Create a hash table storing all the letters in word 1
  var frequencyTable = {};
  for (var i = 0; i < word1.length; i++) {
    // if there's already one such letter, increment the count
    if (frequencyTable[word1[i]] !== undefined) {
      frequencyTable[word1[i]] += 1;
    } else {
      // otherwise, start it at 0
      frequencyTable[word1[i]] = 1;
    }
  }

  // Start counting down with the letters in word 2
  // If there are ever not enough of the matching letter left, word 2 is
  // not an anagram
  for (var i = 0; i < word2.length; i++) {
    if (frequencyTable[word2[i]] > 0) {
      frequencyTable[word2[i]] -= 1;
    } else {
      // not enough letters left! Therefore, word 1 doesn't have all
      // the letters contained in word 2.
      return false;
    }
  }

  // if we get this far without exiting, the words must be anagrams
  return true;
}

/**
 * Tests the `checkAnagrams` function.
 */
function runTests() {
  // check length
  console.assert(checkAnagram("long", "short") === false);

  // check non-match case
  console.assert(checkAnagram("butter", "batter") === false);

  // check simple case
  console.assert(checkAnagram("ring", "grin") === true);

  // check case sensitivty
  console.assert(checkAnagram("Evil", "vile") === false);

  // check support for non-alphabetic characters
  console.assert(checkAnagram("July 4, 1776!", "1776! 4, July") === true);

  // check edge cases
  console.assert(checkAnagram("", "") === true);
  console.assert(checkAnagram("hi", null) === false);
}
