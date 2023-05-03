// validation\

















// patient val

function loginvalidate(){
    login_id=document.getElementById("id")
     
    if(login_id.value.length!=8)
    {
        id_span.innerHTML="ID Incorrect" 
    id_span.style.color="red"
    return false
}else{
    id_span.value=""
}
p_password=document.getElementById("password")


if(p_password.value.length!=8){
    password_span.innerHTML="Password Incorrect"
    password_span.style.color='red'

}

}