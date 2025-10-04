document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const remember = document.getElementById("rememberMe").checked;

  if (username === "" || password === "") {
    alert("Vui lòng nhập đầy đủ thông tin!");
  } else {
    let message = "Đăng nhập thành công!";
    if (remember) {
      message += " (Đã ghi nhớ đăng nhập)";
    }
    alert(message);
  }
});