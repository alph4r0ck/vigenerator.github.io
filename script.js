document.getElementById('generateButton').addEventListener('click', function() {
  var numWords = parseInt(document.getElementById('num_words').value);
  var separator = document.getElementById('separator').value;

  var wordlist = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'jackfruit', 'kiwi'
  ];

  var passphrase = generatePassphrase(wordlist, numWords, separator);
  var password = generatePassword();
  document.getElementById('passphrase').textContent = passphrase;
  document.getElementById('passphraseContainer').style.display = 'block';
  document.getElementById('password').textContent = password;
  document.getElementById('generatedPassword').style.display = 'block';
});

function generatePassphrase(wordlist, numWords, separator) {
  var passphrase = '';
  for (var i = 0; i < numWords; i++) {
    var randomIndex = Math.floor(Math.random() * wordlist.length);
    passphrase += wordlist[randomIndex];
    if (i < numWords - 1) {
      passphrase += separator;
    }
  }
  return passphrase;
}

function generatePassword() {
  var length = 10;
  var charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]\:;?><,./-=';
  var password = '';
  for (var i = 0; i < length; i++) {
    var randomIndex = Math.floor(Math.random() * charset.length);
    password += charset[randomIndex];
  }
  return password;
}
