const {
    ipcRenderer
} = require('electron');
const path = require('path');



window.onload=function () {
    let mess = "";
    mess = document.getElementById("message").value;
    console.log(mess);
    ipcRenderer.send("runpyfile", ['./py/prime.py',mess]);
    ipcRenderer.on('getAns',(event,args)=>{
        //console.log(args);
        //console.log(typeof(args));
        document.getElementById("para").innerText = args;
    });

}
