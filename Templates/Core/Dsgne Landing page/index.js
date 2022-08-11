/**
 * It's a function that hides the blog container and shows the ecom container on click.
 */
const colorSwitch = document.getElementById('input-color-switch');
let imageOne = document.querySelector("#one-image");

colorSwitch.addEventListener('click', checkMode);

function checkMode() {
    console.log('checking')
    if(colorSwitch.checked){
        darkModeOn()
        imageOne.src = "./images/dsyne features-DM.png"
    }else{
        darkModeOff();
        imageOne.src = "./images/dsyne features 1.png"
    }
}

function darkModeOn(){
    document.body.classList.add("dark-mode")
}
function darkModeOff(){
    document.body.classList.remove("dark-mode")
}

// switching Up images with dark and light mode
  
  // if (colorSwitch.checked) {
  //   console.log("go girl go")
  // }else{
  //   imageOne.src = "./images/dsyne features-DM.png"
  // }
let imageSources = [
  "./images/articleOne.png",
  "./images/articleTwo.png",
  "./images/articleThree.png",
  "./images/articleFour.png"
]
let index = 0;
setInterval(function(){
  if(index ===imageSources.length){
    index = 0;
  }
  document.getElementById("image").src =imageSources[index];
  index++;
}, 2000);

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

