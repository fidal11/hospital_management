// validation\

















// patient val

function loginvalidate() {
    login_id = document.getElementById("id")

    if (login_id.value == "") {
        id_span.innerHTML = "Please Enter ID"
        id_span.style.color = "red"

    }

    else if (login_id.value.length != 8) {
        id_span.innerHTML = "ID Incorrect"
        id_span.style.color = "red"
        return false
    } else {
        id_span.value = ""
    }
    p_password = document.getElementById("password")


    if (p_password.value == "") {
        password_span.innerHTML = "Please Enter Your Password"
        password_span.style.color = 'red'


    }
    else if (p_password.value.length != 8) {
        password_span.innerHTML = "Incorrect Password"
        password_span.style.color = 'red'
    }
    else {
        password_span.innerHTML = ""
    }
}