// Light mode/dark mode toggler
const colorSwitch = document.getElementById('input-color-switch');

colorSwitch.addEventListener('click', checkMode);
function checkMode() {
    console.log('checking')
    if(colorSwitch.checked){
        console.log('dark mode on babby')
        darkModeOn()
    }else{
        console.log('dark mode off boo')
        darkModeOff()
    }
}

function darkModeOn(){
    document.body.classList.add("dark-mode")
}
function darkModeOff(){
    document.body.classList.remove("dark-mode")
}


//Navbar

function classToggle(){
    const navs = document.querySelector(".nav-bar");
    navs.classList.toggle('show-nav-on-mobile');
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
// document.querySelector('#select-field').addEventListener('click', dropMenu);


const faqs = document.querySelectorAll(".faq");

faqs.forEach((faq) => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("active");
    })
})