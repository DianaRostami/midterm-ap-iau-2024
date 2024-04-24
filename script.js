function generateRandomPassword(length) {
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    let password = "";
  for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * charset.length);
      password += charset[randomIndex];
    }
    return password;
  }
document.getElementById("generateButton").addEventListener("click", function() {
    const passwordLength = 10;
    const generatedPassword = generateRandomPassword(passwordLength);
    document.getElementById("passwordDisplay").value = generatedPassword;
  });
  
