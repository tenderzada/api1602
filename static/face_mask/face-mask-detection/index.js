$(document).ready(function() {
    appendHeader(true);
    appendFooter(true);
})


function isAndroid() {
    const ua = navigator.userAgent.toLowerCase();
    return ua.indexOf("android") > -1; 
}
  
function isiOS() {
const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
return iOS
}

if (isAndroid()) {
    alert("aizoo.com上的深度学习算法都在您本地手机运行，您的数据不会被上传。\n为提高运算速度，推荐在电脑浏览器访问本页面。");
} else if (isiOS()) {
    alert("iOS设备推荐使用Safari浏览器访问，其他浏览器有时不能在浏览器很好的运行深度学习模型。\n aizoo.com上的深度学习算法都在您本地浏览器运行，您的数据不会被上传。\n为提高运算速度，推荐在电脑浏览器访问本页面。");
}