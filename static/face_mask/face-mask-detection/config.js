foreground = [['face-mask-detection/img/img4.jpg', '武汉加油！中国加油'], ['face-mask-detection/img/img5.jpeg','向白衣天使致敬！'], ['face-mask-detection/img/img3.jpeg','中国必胜'], 
            ['face-mask-detection/img/img6.jpeg','战胜疫情'],['face-mask-detection/img/img8.jpeg','病毒走开'],['face-mask-detection/img/img7.jpeg','终将胜利'],]


function insertForeground() {
    foreground.map(config => {
        item = `<div class="col-4 col-sm-4 col-md-4 col-xl-2">
                    <figure>
                        <img src="${config[0]}" class="img-responsive img-content" style=""/>
                        <figcaption>${config[1]}</figcaption>
                    </figure>
                </div>`
        $('#foreground_images').append(item);
    })
    item = `<div class="col-12 col-sm-6">
                <div class="input-group mb-3">
                    <input type="text" class="form-control" id="contentImgUrlInput" placeholder="从网络URL获取图片" aria-label="Recipient's username" aria-describedby="basic-addon2">
                    <div class="input-group-append">
                    <button class="btn btn-outline-secondary" id="contentImgUrlConfirmBt" type="button">确定</button>
                    </div>
            </div>
            </div>  

            <div class="col-12 col-sm-6">
            <!-- <input type="file" name="上传图片" id="inputGroupFile04vv" placeholder="sss" style="background-color: antiquewhite"> -->
            <div class="input-group">
                <div class="custom-file" style="text-align:left">
                <input type="file" class="custom-file-input" accept="image/*" id="contentImgFileUploadInput" placeholder="上传文件">
                <label class="custom-file-label" for="inputGroupFile04">本地上传</label>
                </div>
            </div>
            </div>  `
    $('#foreground_images').append(item);

}        

insertForeground();