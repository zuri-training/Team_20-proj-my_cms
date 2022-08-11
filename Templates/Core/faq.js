
// input.onclick = () => {
//     // get the section and toggle theme
//     document.querySelector("section").classList.toggle("dark-theme");
// };
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
//logo

//Navbar

function classToggle(){
    const navs = document.querySelectorAll(".nav-bar")
    navs.forEach( nav =>
        nav.classList.toggle('show')
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



// FAQ ACCORDION
const faqs = document.querySelectorAll(".faq");

faqs.forEach((faq) => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("active");
    })
})

// BG
const bgSwitch = document.getElementById('input-color-switch');

bgSwitch.addEventListener('change', () => {
document.section.classList.toggle('dark');
});
// function checkMode() {
//     console.log('checking')
//     if(colorSwitch.checked){
//         darkModeOn()
//     }else{
//         darkModeOff()
//     }
// }