let net;
let contentImg;
let showBox = true;
let showLandmark = true;
let showExpression = true;
let showAgeGender = true;
let intervalID;
let canvasDownload = document.createElement('canvas'); //作为下载图片专用的canvas
let canvasDownloadContext = canvasDownload.getContext('2d');

let resultImg = new Image();
let canvas_show = document.getElementById("canvas_show");
let context = canvas_show.getContext('2d');
let canvasTemp = document.createElement("canvas");

id2class = {0:"有口罩", 1:"无口罩"};

const modelUrl = '127.0.0.1:8000/static/tfjs-models/model.json'
contentImgDefault = document.getElementsByClassName("img-content")[5];

contentImg = new Image();
contentImg.src = contentImgDefault.src;


async function loadModels() {
    net = await aizoo.ssdObjectDetection(modelUrl);
}

// 返回将结果画到图上的img
async function faceAnalysisInternal(img, canvas, drawBox=true) {
    results = await net.detect(img);
    canvas.width = img.width;
    canvas.height = img.height;
    ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);
    for(bboxInfo of results) {
        bbox = bboxInfo[0];
        classID = bboxInfo[1];
        score = bboxInfo[2];

        if (drawBox) {
            ctx.beginPath();
            ctx.lineWidth="4";
            if (classID == 0) {
                ctx.strokeStyle="green";
                ctx.fillStyle="green";
            } else {
                ctx.strokeStyle="red";
                ctx.fillStyle="red";
            }
            
            ctx.rect(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1]);
            ctx.stroke();
        }
        ctx.font="30px Arial";
        
        let content = id2class[classID] + " " + score.toFixed(2)
        ctx.fillText(content, bbox[0], bbox[1] < 20 ? bbox[1] + 30 : bbox[1]-5);
    }
    return canvas;
}



function writeToCanvasDownload(img) {
    canvasDownload.width = img.width;
    canvasDownload.height = img.height;
    canvasDownloadContext.clearRect(0, 0, canvasDownload.width, canvasDownload.height);
    canvasDownloadContext.drawImage(img, 0, 0, img.width, img.height)
    
}

async function faceAnalysis(img) {
    await faceAnalysisInternal(img, canvasTemp, showBox);
    resultImg.src = canvasTemp.toDataURL();
    resultImg.onload = () => {
        writeToCanvasDownload(resultImg);
        cords = calculateLocationInCanvas(canvas_show.width, 
                                                    canvas_show.height, resultImg.width, resultImg.height);
        // console.log(cords);
        context.clearRect(0, 0, canvas_show.width, canvas_show.height);
        context.drawImage(resultImg , cords[0], cords[1], cords[2], cords[3]);
        // })
      }
}

function faceVideoAnalysis(video) {
    if (!video.paused) {
        faceAnalysis(video);
        intervalID = setTimeout(() => {
            faceVideoAnalysis(video);
        });
        // intervalID = setInterval(() => {
        //     faceVideoAnalysis(video);
        // }, 0)
        // faceVideoAnalysis();
    } else {
        return;
    }
}

async function setup() {
    // await loadModels();
    net = await aizoo.ssdObjectDetection(modelUrl);
    $('#loadModelIndictor').hide();
    video = document.createElement('video');
    video.width = 640;
    video.height = 480;
    video.setAttribute("style", "display: none;");
    document.body.appendChild(video);
    
    
    await faceAnalysis(contentImg);
  }
  
//   getAllCamera(videoSources); // 获取所有的摄像头ID
setup();