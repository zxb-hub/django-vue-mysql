     
     //导航栏样式
     function menu_click() {
            var menu = this.document.getElementById('fristMenu')
            var Li = menu.getElementsByTagName('li')
            var span = menu.getElementsByTagName('span')
            var oPoint =document.elementsFromPoint(event.clientX, event.clientY);
            
            menu.addEventListener('click', function () {
                for (var j = 0; j < Li.length; j++) {
                    Li[j].className = 'menu_ul_li' //还原导航栏样式 
                }
                oPoint[1].className = 'menu_aclick';
            })

        }