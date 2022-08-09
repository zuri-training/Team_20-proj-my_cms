

//Navbar

function classToggle(){
    const navs = document.querySelectorAll(".nav-bar")
    navs.forEach( nav =>
        nav.classList.toggle('show-nav-on-mobile')
    );
}
document.querySelector('#menu').addEventListener('click', classToggle)

//dropdown
function dropMenu(){
    const drops = document.querySelector('#drop-menu')
    if(drops.style.display == "none"){
        drops.style.display = "block"
    }else{
        drops.style.display = "none"
    }
}
document.querySelector('#select-field').addEventListener('click', dropMenu)



