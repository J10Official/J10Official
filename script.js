var tablinks= document.getElementsByClassName('tab');
var tabcontents= document.getElementsByClassName('tab-contents');

function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove('active');
    }
    for(tabcontent of tabcontents){
        tabcontent.classList.remove('active-tab');
    }
    event.currentTarget.classList.add('active');
    document.getElementById(tabname).classList.add('active-tab');
}

var icon= document.getElementById('icon');
            icon.onclick= function(){
                document.body.classList.toggle('light-theme');
                if(document.body.classList.contains("light-theme")){
                    icon.src="images/moon.png";
                }
                else{
                    icon.src="images/sun.png";
                }
            }