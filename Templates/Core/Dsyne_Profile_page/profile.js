// Light mode/dark mode toggler
const colorSwitch = document.getElementById('input-color-switch');

colorSwitch.addEventListener('click', checkMode);
function checkMode() {
    console.log('checking')
    if(colorSwitch.checked){
        darkModeOn()
    }else{
        darkModeOff()
    }
}

function darkModeOn(){
    document.body.classList.add("dark-mode")
}
function darkModeOff(){
    document.body.classList.remove("dark-mode")
}


//dropdown
function dropMenu(){
    const drops = document.querySelector('#drop-menu')
    if(drops.style.display == "none"){
        drops.style.display = "flex"
    }else{
        drops.style.display = "none"
    }
}
document.querySelector('#select-field').addEventListener('click', dropMenu)





function dropOptions(){
    const navs = document.querySelector('.nav-menu')
    if(navs.style.display == "none"){
        navs.style.display = "flex"
    }else{
        navs.style.display = "none"
    }
}
document.querySelector('#nav-field').addEventListener('click', dropOptions)



function dropOptions2(){
    const navs2 = document.querySelector('.nav-menu2')
    if(navs2.style.display == "none"){
        navs2.style.display = "flex"
    }else{
        navs2.style.display = "none"
    }
}
document.querySelector('#nav-field2').addEventListener('click', dropOptions2)

             