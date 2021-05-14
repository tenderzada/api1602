$(".img-content").click(
    (item) => {
        stopVideo(video);
        contentImg = new Image();
        contentImg.src = item.currentTarget.src;
        
        contentImg.onload = function() {
            faceAnalysis(contentImg, canvasTemp);
        }
})


$('#openCameraBt').click(() => {
  startVideo(video).then( x=> faceVideoAnalysis(video));
});


$('#switchCameraBt').click(() => {
  startVideo(video,switchCamera=true).then(()=> {
    faceVideoAnalysis(video);
  });
})

$('#closeCameraBt').click(()=>stopVideo(video));

$('#saveImgBt').click(() => {
  let downloadLink = document.createElement("a");
  downloadLink.download = 'face.png';
  downloadLink.href = canvasDownload.toDataURL("image/png");
  downloadLink.click();
  downloadLink.remove();
})

$(".switchBt").click( (item) => {
    if (item.target.id == "showBox") {
        showBox = item.target.checked;
    } else if(item.target.id == "showLandmark") {
        showLandmark = item.target.checked;
    }
    else if (item.target.id == "showExpression") {
        showExpression = item.target.checked;
    }
    else if (item.target.id == "showAgeGender") {
        showAgeGender = item.target.checked;
    }
    faceAnalysis(contentImg);
    }
)



$('#contentImgUrlConfirmBt').click(() =>{
    let value = $('#contentImgUrlInput').val()
    // contentImgTemp = new Image();
    contentImg.crossOrigin = "anonymous";
    contentImg.src = value;
    contentImg.onload = async () => {
    //   console.log("图像加载成功");
      faceAnalysis(contentImg);

    }
    contentImg.onerror = () => {alert("您输入的URL被拒绝访问，请换一张图片～");}
  })
  
  
  $('#contentImgFileUploadInput').on('change', ()=> {
    let fileObj = $('#contentImgFileUploadInput').prop('files')[0];
    contentImg.onload = async () => {
        console.log("上传内容图像加载成功");
        faceAnalysis(contentImg);
        // segmentAndCombine(contentImg, contentImg);
    }
    loadImage(
              fileObj,
              (img) => { contentImg.src = img.toDataURL();
                contentImg.width = img.width;
                contentImg.height = img.height;
                console.log("Img width:", contentImg.width, contentImg.height);
              },
              { orientation:true,
                maxWidth:480,
              }
            );
  })