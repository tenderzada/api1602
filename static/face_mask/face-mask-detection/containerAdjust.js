// 自动设置canvas的高度
canvas_container = document.getElementById("canvas_container");
canvas_show = document.getElementById("canvas_show");
img_region = document.getElementById("img_region");

function calculate_size() {
  canvas_show.width = canvas_container.offsetWidth * 0.9;
  canvas_show.height = canvas_show.width;
  img_region.style.height = canvas_show.width + "px"
}

calculate_size();

function onload_fun(){
  calculate_size();
}

window.onresize = onload_fun;
window.onload = onload_fun;
