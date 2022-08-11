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

// switching Up images with dark and light mode
  let darkmode = darkModeOn();
  let imageOne = document.getElementById("settings");
  if (darkmode) {
    imageOne.src = "./images/setting-DM.png"
  }else{
    console.log("no possible");
  }
// let imageOne = document.getElementById("settings");
// let img = true;
// function images(){
// img ? imageOne.src = "./setting-DM.png": console.log("no possible");
// }
// colorSwitch.addEventListener("click", () => {
//   img = !img;
//   images();
// })
// swiping article
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


const goToblog = () => {
  const button = document.getElementsByid("blogs");
  const blog = document.getElementById("blog-templates");
  button.addEventListener("click", ()=>{
      window.scroll({
          left: blog.offset,
          behavior:'smooth'
        });
  });
}
const goToecom = () => {
  const ecomLink = document.getElementsByid("ecom");
  const ecom = document.getElementById("ecom-templates");
  ecomLink.addEventListener("click", ()=>{
      window.scroll({
          left: ecom.offset,
          behavior:'smooth'
        });
  });
}