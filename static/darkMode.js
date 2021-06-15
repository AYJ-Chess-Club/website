const setCookie = (name, value, days) => {
  let expires = ""
  if (days) {
    let date = new Date()
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000))
    expires = "; expires=" + date.toUTCString()
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/"
}

const getCookie = (name) => {
  name += "="
  let ca = document.cookie.split(";")
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
  }
  return null;
}

if (getCookie("isDark") == 1) {
  document.body.classList.add("dark")
  try {
    document.getElementById("footer").classList.add("dark-footer")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("navbar").classList.add("dark-navbar")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("signup-btn").classList.add("dark-auth-buttons")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("login-btn").classList.add("dark-auth-buttons")
  } catch (e) { console.log(e) }
}

const toggleDark = () => {
  document.body.classList.toggle("dark")
  try {
    document.getElementById("signup-btn").classList.toggle("dark-auth-buttons")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("login-btn").classList.toggle("dark-auth-buttons")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("footer").classList.toggle("dark-footer")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("navbar").classList.toggle("dark-navbar")
  } catch (e) { console.log(e) }
  setCookie("isDark", getCookie("isDark") == 1 ? 0 : 1, 7)
}