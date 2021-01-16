     
     //导航栏样式
     function menu_click(a) {
        var menu = this.document.getElementById('menu')
        var Li = menu.getElementsByTagName('li')
        for (var j = 0; j < Li.length; j++) {
                Li[j].className = 'menu_ul_li' //还原导航栏样式 
            }
        a.setAttribute ('class','menu_aclick');
    }