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
    let user_list = document.getElementsByClassName("users-list-group-item")
    for (let i = 0; i < user_list.length; i++) {
      user_list[i].classList.add("bg-dark")
      user_list[i].classList.add("text-white")
    }
  } catch (e) { console.log(e) }

  try {
    let link_list = document.getElementsByClassName("paginator-page-link-active")
    for (let i = 0; i < link_list.length; i++) {
      link_list[i].classList.add("bg-dark")
      link_list[i].classList.add("text-white")
    }
  } catch (e) { console.log(e) }

  try {
    let link_list = document.getElementsByClassName("paginator-page-link")
    for (let i = 0; i < link_list.length; i++) {
      link_list[i].classList.add("bg-dark")
      link_list[i].classList.add("text-white")
    }
  } catch (e) { console.log(e) }



  try {
    document.getElementById("users-tab").classList.add("bg-dark")
    document.getElementById("users-tab").classList.add("text-white")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("docs-tab").classList.add("bg-dark")
    document.getElementById("docs-tab").classList.add("text-white")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("getting-started-tab").classList.add("bg-dark")
    document.getElementById("getting-started-tab").classList.add("text-white")
  } catch (e) { console.log(e) }
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
  try {
    document.getElementById("fancy-sudo").classList.add("dark-fancy-sudo")
  } catch (e) { console.log(e) }
}

const toggleDark = () => {
  document.body.classList.toggle("dark")
  try {
    let user_list = document.getElementsByClassName("users-list-group-item")
    for (let i = 0; i < user_list.length; i++) {
      user_list[i].classList.toggle("bg-dark")
      user_list[i].classList.toggle("text-white")
    }
  } catch (e) { console.log(e) }

  try {
    let link_list = document.getElementsByClassName("paginator-page-link-active")
    for (let i = 0; i < link_list.length; i++) {
      link_list[i].classList.toggle("bg-dark")
      link_list[i].classList.toggle("text-white")
    }
  } catch (e) { console.log(e) }

  try {
    let link_list = document.getElementsByClassName("paginator-page-link")
    for (let i = 0; i < link_list.length; i++) {
      link_list[i].classList.toggle("bg-dark")
      link_list[i].classList.toggle("text-white")
    }
  } catch (e) { console.log(e) }





  try {
    document.getElementById("users-tab").classList.toggle("bg-dark")
    document.getElementById("users-tab").classList.toggle("text-white")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("docs-tab").classList.toggle("bg-dark")
    document.getElementById("docs-tab").classList.toggle("text-white")
  } catch (e) { console.log(e) }
  try {
    document.getElementById("getting-started-tab").classList.toggle("bg-dark")
    document.getElementById("getting-started-tab").classList.toggle("text-white")
  } catch (e) { console.log(e) }
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
  try {
    document.getElementById("fancy-sudo").classList.toggle("dark-fancy-sudo")
  } catch (e) { console.log(e) }
  setCookie("isDark", getCookie("isDark") == 1 ? 0 : 1, 7)
}