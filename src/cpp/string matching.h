/*
 * Author: Muhammadrizo Latifxonov
 * Date:25.10.2023
 * Name:
 */
#include <iostream>
#include <string>

using namespace std;

bool matchWordInSentence(string sentence, string word) {
  size_t found = sentence.find(word);
  if (found != string::npos) {
    return true;
  } else {
    return false;
  }
}

int main() {
  string sentence, word;

  cout << "Enter a sentence: ";
  cin >> sentence;

  cout << "Enter a word: ";
  cin >> word;

  bool match = matchWordInSentence(sentence, word);

  if (match) {
    cout << "The word matches the sentence at index " << sentence.find(word) << endl;
  } else {
    cout << "No match" << endl;
  }

  return 0;
}