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
        port.style.display = "none";
        blog.style.display = "flex";
    });
}
portfolios();
// hide blog container and show ecom container on click