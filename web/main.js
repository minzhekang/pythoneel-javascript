function printit(){
    var data = document.getElementById("cow").value;
    eel.printme(data, data)(callback);
    //python
}

function callback(ret1){
    document.getElementById("TobePrinted").innerHTML = ret1
}