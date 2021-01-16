function adminHp(){
    var sign=this.document.getElementById('admin_sign')
    var userModify=this.document.getElementById('admin_userModify')
    var article = this.document.getElementById('admin_article')
    var menu = this.document.getElementById('adminMenu_body')
    var menuSign = this.document.getElementById("menuSign")
    var menuModify =  this.document.getElementById("menuModify")
    var menuArticle =  this.document.getElementById("menuArticle")

    menuSign.addEventListener('click',function(){
        menuSign.className='menu_click';
        menuModify.className='';
        menuArticle.className='';
        sign.style.display='block';
        userModify.style.display='none';
        article.style.display='none';
    })
    menuModify.addEventListener('click',function(){
        menuModify.className='menu_click';
        menuSign.className='';
        menuArticle.className='';
        userModify.style.display='block';
        sign.style.display='none';
        article.style.display='none';
    })
    menuArticle.addEventListener('click',function(){
        menuArticle.className='menu_click';
        menuSign.className='';
        menuModify.className='';
        article.style.display='block';
        userModify.style.display='none';
        sign.style.display='none';
    })
}

function userModify(){
    var authority = document.getElementById('userNub')
    authority.innerHTML = authority;

}