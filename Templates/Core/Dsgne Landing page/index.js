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

// hide templates container on click
// const hideb = () => {
//   const hide = document.getElementById("templates-container");
//   hide.addEventListener("click", () => {
//     hide.style.display = "none";
//   });
// }

// declaring variables for the templates containers
const ecoms_show = document.getElementById("ecoms");
const blog_show = document.getElementById("blogs");
const portfolio_show = document.getElementById("portfolios");
const blog = document.getElementById("blog_containers");
const ecom = document.getElementById("ecom_containers");
const port = document.getElementById("portfolio_containers");


// hide blog, portfolio container and show ecom container on click
function ecomms() {
    ecoms_show.addEventListener("click", () => {
        console.log("clicked")
        blog.style.display = "none";
        port.style.display = "none";
        ecom.style.display = "flex";
    });
}

ecomms();

// hide ecom, portfolio container and show blog container on click
function blogs() {
    blog_show.addEventListener("click", () => {
        console.log("clicked")
        ecom.style.display = "none";
        port.style.display = "none";
        blog.style.display = "flex";
    });
}
blogs();

// hide blog, ecom container and show portfolio container on click
function portfolios() {
    portfolio_show.addEventListener("click", () => {
        console.log("clicked")
        ecom.style.display = "none";
        port.style.display = "flex";
        blog.style.display = "none";
    });
}
portfolios();
// hide blog container and show ecom container on click
