document.getElementById("test").onmouseover = function(){mouseOver()};
document.getElementById("test").onmousemove = function() {mouseOut()};

function mouseOver(){
    document.getElementById("test").style.color = "red";
}
function mouseOut(){
    document.getElementById("test").style.color = "white";
}
function calcular_imc(){
    var sit="";
    var peso = document.getElementById("peso").value;

    var altura = document.getElementById("altura").value;

    var imc = ((peso/altura)**2)
    if (imc < 18.5)
        sit = "Voce está com peso baixo!"
    if (imc <= 24.9)
        sit = "Voce está com peso normal!"
    if (imc < 29.9)
        sit = "Voce está com sobrepeso!"
    if (imc < 34.9)
        sit = "Voce está com obesidade grau I!"
    if (imc < 39.9)
        sit = "Voce está com obesidade grau II!"
    else
        sit = "Voce está com obesidade grau III!"
    document.getElementById("imc").value=imc;
    document.getElementById("sit").value=sit;
}
