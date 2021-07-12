var daohang = document.querySelector('.daohang');
var ul = daohang.querySelector('ul');
var lis = ul.querySelectorAll('li');
var ol = document.querySelector('ol');
var index = 0;

for(var i=0;i<lis.length;i++){
    lis[i].addEventListener('click',function(){
        if(this.className != 'gu'){
            for(var j=0;j<lis.length;j++){
                if(lis[j].className != 'gu'){
                    lis[j].className = ' ';
                }
            }
            this.className = 'an';
            if(ol.className == 'xiala'){
                index = 0;
                ol.className = ' ';
            }
        }
        else {
            if(index == 0){
                ol.className = 'xiala';
                index = 1;

            }
            else if(index == 1){
                index = 0;
                ol.className = ' ';
            }
        }
    })
}

var tubiao  = document.querySelector('.tubiao');
var button = tubiao.querySelector('button');
var hezi = document.querySelector('.hezi');
var header = document.querySelector('.header');
var index2 = 0;

button.addEventListener('click',function(){
    if(index2 == 0){
        index2 = 1;
        hezi.style.height = '400' + 'px';
        header.style.height = '421' + 'px';
    }
    else {
        index2 = 0;
        hezi.style.height = '0' + 'px';
        header.style.height = '171' + 'px';
    }
})

var index3 = 0;
var lis2 = hezi.querySelectorAll('li');
var ol2 = hezi.querySelector('ol');
var gun = document.querySelector('.gun');
for(var i=0;i<lis2.length;i++){
    lis2[i].addEventListener('click',function(){
        if(this.className != 'gun'){
            for(var j=0;j<lis.length;j++){
                if(lis2[j].className != 'gun'){
                    lis2[j].className = ' ';
                }
            }
            this.className = 'sec';
            if(ol2.className == 'xiala2'){
                index3 = 0;
                ol2.className = ' ';
                gun.style.height = '40' + 'px';
            }
        }
        else {
            if(index3 == 0){

                gun.style.height = '140' + 'px';
                header.style.height = '521' + 'px';
                ol2.className = 'xiala2';
                index3 = 1;

            }
            else if(index3 == 1){
                gun.style.height = '40' + 'px';
                header.style.height = '421' + 'px';
                index3 = 0;
                ol2.className = ' ';
            }
        }
    })
}