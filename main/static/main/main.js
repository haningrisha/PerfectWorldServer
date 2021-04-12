document.getElementById("about-server-btn").onclick = () => {
    document.getElementById("about-server").scrollIntoView()
}

document.getElementById("login-nav").onclick = () => {
    $("#collapseOne").collapse('show');
    document.getElementById("login-accordion").scrollIntoView()
}

document.getElementById('register-btn').onclick = () => {
    $("#collapseTwo").collapse('show');
    document.getElementById("register-accordion").scrollIntoView()
}

document.getElementById('register-nav').onclick = () => {
   $("#collapseTwo").collapse('show');
    document.getElementById("register-accordion").scrollIntoView()
}