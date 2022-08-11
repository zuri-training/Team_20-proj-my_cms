const ecoms_show = document.getElementById("ecoms");
const blog_show = document.getElementById("blogs");
const portfolio_show = document.getElementById("portfolios");
const blog = document.getElementById("blog_containers");
const ecom = document.getElementById("ecom_containers");
const port = document.getElementById("portfolio_containers");
// hide blog container and show ecom container on click
// console.log("clicked")
function ecomms() {
    ecoms_show.addEventListener("click", () => {
        console.log("clicked")
        blog.style.display = "none";
        port.style.display = "none";
        ecom.style.display = "flex";
    });
}

ecomms();
function blogs() {
    blog_show.addEventListener("click", () => {
        console.log("clicked")
        ecom.style.display = "none";
        port.style.display = "none";
        blog.style.display = "flex";
    });
}
blogs();
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

const clickEcomDropdown = document.getElementById("drop-Ecom")
function clickEcom (){
    clickEcomDropdown.addEventListener("click", () => {
        console.log("clicked")
        blog.style.display = "none";
        port.style.display = "none";
        ecom.style.display = "flex";
    });
}
clickEcom ();
const clickblogDropdown = document.getElementById("drop-blog")
function clickBlog (){
    clickblogDropdown.addEventListener("click", () => {
        console.log("clicked")
        blog.style.display = "flex";
        port.style.display = "none";
        ecom.style.display = "none";
    });
}
clickBlog();

const clickportDropdown = document.getElementById("drop-port")
function clickPort(){
    clickportDropdown.addEventListener("click", () => {
        console.log("clicked")
        blog.style.display = "none";
        ecom.style.display = "none";
        port.style.display = "flex";
    });
}
clickPort();
