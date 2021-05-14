function generate_details(son=false) {
    if (son) {
        aizoo_wx_official_path = "../public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "../public/aizoo_wx_helper.jpg";
        aizoo_logo_path = "../public/aizoo_logo.png";
    } else {
        aizoo_wx_official_path = "public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "public/aizoo_wx_helper.jpg";
        aizoo_logo_path = "public/aizoo_logo.png";
    }
    content = `
            <div class="row">
                <div class="col-sm-12 col-md-4 col-lg-4 " style="text-align: center">
                    <h4 class="text-white">About</h4>
                    <p class="text-muted"><a href="https://aizoo.com">aizoo.com</a> 致力于打造一个深度学习算法乐园，集合各种有趣的深度学习模型。</p>
                    <p class="text-muted">同时，aizoo.com也展示工业级稳健AI算法，以人工智能，赋能各行各业发展。</p>
                    <p class="text-light">如果您是算法工程师，或者您有算法项目需求，请添加我们的微信号AIZOOTech拉您进我们的群与大家交流。</p>
                </div>

                <div class="col-sm-12 col-md-4 col-lg-4" style="text-align: center">
                    <div class="col-sm-12 " style="text-align: center">
                        <h4 class="text-white">公众号</h4>
                        <div class="thumbnail" >
                            <img src="${aizoo_wx_official_path}" width="120px" class="img-circle">
                            <div class="caption">
                                <h6 style="color:aliceblue" >扫一扫，或搜索"AIZOO"关注我们的公众号AIZOO</h6>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-sm-12 col-md-4 col-lg-4" style="text-align: center">
                    <div class="col-sm-12 " style="text-align: center">
                        <h4 class="text-white">Contact</h4>
                        <div class="thumbnail" >
                            <img src="${aizoo_wx_helper_path}" width="120px" class="img-circle">
                            <div class="caption">
                                <h6 style="color:aliceblue" >扫一扫，或搜索"AIZOOTech"，添加AIZOO小助手与我联系</h6>
                                <h6 style="color:aliceblue">邮箱:contact@aizoo.com</h6>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`
    return content
}

function appendHeader(son=false) {
    if (son) {
        aizoo_wx_official_path = "../public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "../public/aizoo_wx_helper.png";
        aizoo_logo_path = "../public/aizoo_logo.png";
    } else {
        aizoo_wx_official_path = "public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "public/aizoo_wx_helper.png";
        aizoo_logo_path = "public/aizoo_logo.png";
    }
    content = generate_details(son);
    header = `
            <div class="collapse bg-dark" id="navbarHeader">
                <div class="container">
                "${content}"
                </div>
            </div>
            <div class="navbar navbar-dark bg-dark shadow-sm">
                <div class="container d-flex justify-content-between">
                    <a href="https://aizoo.com" class="navbar-brand d-flex align-items-center" >
                        <img src="${aizoo_logo_path}" width="120px"/>
                    </a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </div>
            </div>`
    $('#header').append(header)
}
function appendFooter(son=false) {
    if (son) {
        aizoo_wx_official_path = "../public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "../public/aizoo_wx_helper.png";
    } else {
        aizoo_wx_official_path = "public/aizoo_wx_official.jpg";
        aizoo_wx_helper_path = "public/aizoo_wx_helper.png";
    }
    content = generate_details(son);
    footer = `
        <div class="container" style="text-align: center">

            '${content}'
            <div class='row' style="text-align:center; width:100%">
                <div class='col-lg-12' >
                    <small><a href="http://beian.miit.gov.cn/" style="text-decoration:none; color:white">沪ICP备19038059号</a></small>
                    <small>
                    <a href="#">返回顶部</a>
                    </small>
                </div>
            </div>
        </div>`
    $('#footer').append(footer)
}
